import geopandas as gpd
import gpxpy
from utils import calculate_distance

def load_gpx_as_geodataframe(gpx_file_path):
    with open(gpx_file_path, "r") as gpx_file:
        gpx = gpxpy.parse(gpx_file)

    for track in gpx.tracks:
        track_distance = 0
        for segment in track.segments:
            last_point = None
            for point in segment.points:
                if last_point:
                    dist = calculate_distance.calculate_distance(
                        last_point.latitude,
                        last_point.longitude,
                        point.latitude,
                        point.longitude,
                    )
                    track_distance += dist
                last_point = point
                # print(f'Point at ({point.latitude},{point.longitude}) -> {point.elevation}')
        print(track_distance)
    lines = []

    return lines


if __name__ == "__main__":
    # gpx_file = gpd.read_file("../track_example.gpx")

    gpx_file_path = "./track_example.gpx"

    gdf_lines = load_gpx_as_geodataframe(gpx_file_path)

    print("\nTracks:")
    print(gdf_lines)
