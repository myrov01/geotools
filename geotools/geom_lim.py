import geopandas as gpd
from geom_calc import geom_calc


if __name__ == "__main__":
    gdf = gpd.read_file("./vegetation-polygon.gpkg")
    geometry = gdf["geometry"]

    point_counts = []
    total_points = 0
    max_poligon_points = 0

    for geom in geometry:
        point_count = geom_calc(geom)
        point_counts.append(point_count)
        total_points += point_count

        if max_poligon_points < point_count:
            max_poligon_points = point_count

        threshold_value = 500

        if point_count >= threshold_value:
            print(f"The number of points in the polygon: {point_count}")

    sorted_list = point_counts[:]
    sorted_list.sort()

    three_max_poligon_points = sorted_list[-3:]

    for index, count in enumerate(three_max_poligon_points):
        print(f"\nPolygon {index} with {count} points")

    print(f"\nMax poligon points: {max_poligon_points}")
    print(f"\nTotal points: {total_points}")
