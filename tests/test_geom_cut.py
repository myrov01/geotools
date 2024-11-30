import os
import geopandas as gpd
from geotools.geom_cut import process_polygon


def get_geometries():
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "data", "testlayer.gpkg")
    gdf = gpd.read_file(file_path)

    geometries = []
    for index, row in gdf.iterrows():
        geom = row["geometry"]
        geometries.append(geom)
    return geometries


def test_simple_process_polygon():
    geometries = get_geometries()

    all_geoms_length = 0

    for geom in geometries:
        if geom:        
            divided_parts = process_polygon(geom, 2)
            all_geoms_length += len(divided_parts)

    assert all_geoms_length == 2

def test_no_process_polygon():
    geometries = get_geometries()

    all_geoms_length = 0

    for geom in geometries:
        if geom:        
            divided_parts = process_polygon(geom, 6)
            all_geoms_length += len(divided_parts)

    assert all_geoms_length == 1
