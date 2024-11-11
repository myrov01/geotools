import geopandas as gpd
from geom_calc import geom_calc


if __name__ == "__main__":
    gdf = gpd.read_file("./vegetation-polygon.gpkg")

    geometry = gdf["geometry"]

    total_points = 0

    for geom in geometry:
        point_count = geom_calc(geom)
        total_points += point_count

        threshold_value = 500

        if point_count >= threshold_value:
            print(f"The number of points in the polygon: {point_count}")

    print(f"Total points: {total_points}")
