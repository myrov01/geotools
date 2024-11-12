import geopandas as gpd


if __name__ == "__main__":
    # gdf = gpd.read_file("./track_example.gpx", layer='tracks')

    geometry = gdf["geometry"]

    print(geometry)