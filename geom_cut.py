import geopandas as gpd
from shapely.ops import split
from shapely.geometry import MultiPolygon, LineString
from geom_calc import geom_calc


def divide_polygon(polygon, max_vertices, direction='vertical'):

    length_polygon = geom_calc(polygon)

    if length_polygon <= max_vertices:
        return [polygon]

    min_x, min_y, max_x, max_y = polygon.bounds

    if direction == 'vertical':
        mid_x = (min_x + max_x) / 2
        cutting_line = LineString([(mid_x, min_y), (mid_x, max_y)])
        next_direction = 'horizontal'
    else:
        mid_y = (min_y + max_y) / 2
        cutting_line = LineString([(min_x, mid_y), (max_x, mid_y)])
        next_direction = 'vertical'

    split_result = split(polygon, cutting_line)

    parts = list(split_result) if isinstance(
        split_result, MultiPolygon) else [split_result]

    valid_parts = []

    for part in parts:
        valid_polygon = divide_polygon(part, max_vertices, next_direction)
        valid_parts.extend(valid_polygon)

    return valid_parts


def process_polygon(geom, max_vertices=200000):

    valid_geometries = []

    if geom.is_empty:
        print(f"Object {index}: the empty geometry is skipped.")
        return []
    if geom.geom_type == 'Polygon':
        divided_polygon = divide_polygon(geom, max_vertices)
        valid_geometries.extend(divided_polygon)
    elif geom.geom_type == 'MultiPolygon':
        for subpolygon in geom.geoms:
            divided_polygon = divide_polygon(subpolygon, max_vertices)
            valid_geometries.extend(divided_polygon)
    else:
        print(f"Object {index}: invalid geometry type({geom.geom_type}).")
    return valid_geometries


if __name__ == "__main__":

    gdf = gpd.read_file("./vegetation-polygon.gpkg")

    all_geometries = []
    all_attributes = []

    for index, row in gdf.iterrows():
        geom = row["geometry"]

        divided_parts = process_polygon(geom, 200000)

        for part in divided_parts:
            all_geometries.append(part)
            all_attributes.append(row.drop("geometry"))

        if (quantity_parts := len(divided_parts)) > 1:
            print(quantity_parts)

    result_gdf = gpd.GeoDataFrame(
        all_attributes, geometry=all_geometries, crs=gdf.crs)

    result_gdf.to_file("output_file.gpkg",
                       layer='quantity_parts', driver="GPKG")
