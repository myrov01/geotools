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
    geometries = get_geometries("testlayer_without_holes.gpkg")

    all_geoms_length = 0

    for geom in geometries:
        if geom:
            divided_parts = process_polygon(geom, 4)
            all_geoms_length += len(divided_parts)

    assert all_geoms_length == 2


def test_no_process_polygon():
    geometries = get_geometries("testlayer_without_holes.gpkg")

    all_geoms_length = 0

    for geom in geometries:
        if geom:
            divided_parts = process_polygon(geom, 5)
            all_geoms_length += len(divided_parts)

    assert all_geoms_length == 1


def test_one_hole_polygon_process():
    geometries = get_geometries("testlayer_one_hole.gpkg")

    all_geoms_length = 0

    for geom in geometries:
        if geom:
            divided_parts = process_polygon(geom, 4)
            all_geoms_length += len(divided_parts)

    assert all_geoms_length == 5


def test_two_holes_polygon_process():
    geometries = get_geometries("testlayer_two_holes.gpkg")

    all_geoms_length = 0

    for geom in geometries:
        if geom:
            divided_parts = process_polygon(geom, 4)
            all_geoms_length += len(divided_parts)

    assert all_geoms_length == 8


def test_rectangle_process():
    geometries = get_geometries("testlayer_rectangle.gpkg")

    all_geoms_length = 0

    for geom in geometries:
        if geom:
            divided_parts = process_polygon(geom, 4)
            all_geoms_length += len(divided_parts)

    assert all_geoms_length == 3


def test_c_process():
    geometries = get_geometries("testlayer_c.gpkg")

    all_geoms_length = 0

    for geom in geometries:
        if geom:
            divided_parts = process_polygon(geom, 4)
            all_geoms_length += len(divided_parts)

    assert all_geoms_length == 8
