import geopandas as gpd


def geom_calc(geom):
    if geom.is_empty:
        return 0
    elif geom.geom_type == "Polygon":
        exterior_points = len(geom.exterior.coords)
        interior_points = sum(len(interior.coords) for interior in geom.interiors)
        return exterior_points + interior_points
    elif geom.geom_type == "MultiPolygon":
        return sum(geom_calc(polygon) for polygon in geom.geoms)

    return 0


if __name__ == '__main__':
    gdf = gpd.read_file("./vegetation-polygon.gpkg")

    geom = gdf["geometry"]

    point_count = geom_calc(geom)

    total_points = point_count.sum()

    print(f"Total points: {total_points}")
