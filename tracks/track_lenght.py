import geopandas as gpd
import gpxpy


def load_gpx_as_geodataframe(gpx_file_path):
    with open(gpx_file_path, 'r') as gpx_file:
        gpx = gpxpy.parse(gpx_file)

    lines = []

    print(gpx.tracks)
    return lines


if __name__ == "__main__":
    # gpx_file = gpd.read_file("../track_example.gpx")

    gpx_file_path = "../track_example.gpx"

    gdf_lines = load_gpx_as_geodataframe(gpx_file_path)

    print("\nTracks:")
    print(gdf_lines)
