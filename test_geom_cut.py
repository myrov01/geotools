import geopandas as gpd
from geom_cut import process_polygon


def geom_input():
    gdf = gpd.read_file("./tests/data/testdata.gpkg")
    return gdf


def test_process_polygon():
    input_file = geom_input()
    geoms, = process_polygon(input_file, process_polygon(4))
    assert len(geoms) == 7
