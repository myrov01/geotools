import os
import geopandas as gpd
from geotools.geom_cut import process_polygon


def get_geometries(path):
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(
        base_path, "data", path)
    gdf = gpd.read_file(file_path)

    geometries = []
    for index, row in gdf.iterrows():
        geom = row["geometry"]
        geometries.append(geom)
    return geometries


def test_simple_process_polygon():
    geometries = get_geometries("testlayer3_without_holes.gpkg")

    all_geoms_length = 0

    for geom in geometries:
        if geom:
            divided_parts = process_polygon(geom, 4)
            all_geoms_length += len(divided_parts)

    assert all_geoms_length == 2


def test_no_process_polygon():
    geometries = get_geometries("testlayer3_without_holes.gpkg")

    all_geoms_length = 0

    for geom in geometries:
        if geom:
            divided_parts = process_polygon(geom, 16)
            all_geoms_length += len(divided_parts)

    assert all_geoms_length == 1


def test_polygon_one_holes_process_polygon():
    geometries = get_geometries("testlayer4_one_hole.gpkg")

    all_geoms_length = 0

    for geom in geometries:
        if geom:
            divided_parts = process_polygon(geom, 4)
            all_geoms_length += len(divided_parts)

    assert all_geoms_length == 5


def test_rectangle_process_polygon():
    geometries = get_geometries("testlayer7_rectangle.gpkg")

    all_geoms_length = 0

    for geom in geometries:
        if geom:
            divided_parts = process_polygon(geom, 4)
            all_geoms_length += len(divided_parts)

    assert all_geoms_length == 2
