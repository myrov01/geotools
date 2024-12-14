import geopandas as gpd
from shapely.ops import split
from shapely.geometry import LineString
from geotools.geom_calc import geom_calc
import argparse
import os


def divide_polygon(polygon, max_vertices, direction="vertical"):

    length_polygon = geom_calc(polygon)

    if length_polygon <= max_vertices or length_polygon <= 4:
        return [polygon]

    min_x, min_y, max_x, max_y = polygon.bounds

    if direction == "vertical":
        mid_x = (min_x + max_x) / 2
        cutting_line = LineString([(mid_x, min_y), (mid_x, max_y)])
        next_direction = "horizontal"
    else:
        mid_y = (min_y + max_y) / 2
        cutting_line = LineString([(min_x, mid_y), (max_x, mid_y)])
        next_direction = "vertical"

    split_result = split(polygon, cutting_line)

    valid_parts = []

    for part in split_result.geoms:
        valid_polygon = divide_polygon(
            part, max_vertices, next_direction)
        valid_parts.extend(valid_polygon)

    return valid_parts


def process_polygon(geom, max_vertices=200000):

    valid_geometries = []

    if geom.is_empty:
        print(f"Object is empty, skipping.")
        return []

    if geom.geom_type == "Polygon":
        divided_polygon = divide_polygon(geom, max_vertices)
        valid_geometries.extend(divided_polygon)
    elif geom.geom_type == "MultiPolygon":
        for subpolygon in geom.geoms:
            divided_polygon = divide_polygon(subpolygon, max_vertices)
            valid_geometries.extend(divided_polygon)
    else:
        print(f"Invalid geometry type {geom.geom_type}, skipping.")

    return valid_geometries


def main():

    initial_polygon_count = 0
    split_count = 0
    parser = argparse.ArgumentParser(
        description="Upload and process vector files.")

    parser.add_argument(
        "files", nargs="+", help="Paths to vector files for processing."
    )
    parser.add_argument(
        "--output_folder",
        default=".",
        help="Folder to save processed files (default: current directory)",
    )
    parser.add_argument(
        "--max_vertices",
        type=int,
        default=200000,
        help="Maximum number of vertices for a polygon before splitting (default: %(default)s)",
    )
    parser.add_argument(
        "--suffix",
        default="_processed",
        help="Suffix to add to the output file name (default: %(default)s)",
    )

    args = parser.parse_args()

    all_geometries = []
    all_attributes = []

    for file_path in args.files:
        if not os.path.isfile(file_path):
            print(
                f"The file {
                    file_path} does not exist or the path is incorrect."
            )
            continue

        print(f"Processing file: {file_path}")

        try:
            gdf = gpd.read_file(file_path)
        except Exception as e:
            print(f"Error reading the file {file_path}: {e}")
            continue

        initial_polygon_count += len(gdf)

        for index, row in gdf.iterrows():
            geom = row["geometry"]

            divided_parts = process_polygon(geom, args.max_vertices)

            for part in divided_parts:
                all_geometries.append(part)
                all_attributes.append(row.drop("geometry"))

    result_gdf = gpd.GeoDataFrame(
        all_attributes, geometry=all_geometries, crs=gdf.crs)

    final_polygon_count = len(result_gdf)

    base_name = os.path.basename(args.files[0])
    name, extension = os.path.splitext(base_name)
    output_file = os.path.join(
        args.output_folder,
        f"{name}{
            args.suffix}{extension}",
    )

    try:
        result_gdf.to_file(output_file, layer="result", driver="GPKG")
        print(f"Result saved successfully to {output_file}")
    except Exception as e:
        print(
            f"Error saving the file: {
                e}. Ensure the output folder exists and has write permissions."
        )

    print(f"Initial number of polygons: {initial_polygon_count}")
    print(f"Number of polygons that were split: {split_count}")
    print(f"Number of polygons after processing: {final_polygon_count}")


if __name__ == "__main__":
    main()
