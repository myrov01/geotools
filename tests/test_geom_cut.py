import os
import geopandas as gpd
from geotools.geom_cut import process_polygon


def get_geometry_and_attributes(path):
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "data", path)
    gdf = gpd.read_file(file_path)
    return [(row["geometry"], {key: value for key, value in row.items() if key != "geometry"}) for _, row in gdf.iterrows()]


def calculate_processed_geometry(file_name, max_vertices):
    data = get_geometry_and_attributes(file_name)
    result = []
    for geom, attr in data:
        if geom:
            processed_parts = process_polygon(geom, max_vertices)
            result.extend([(part, attr) for part in processed_parts])
    return result


def get_attributes_consistency(file_name, max_vertices):
    original_data = get_geometry_and_attributes(file_name)
    processed_data = calculate_processed_geometry(file_name, max_vertices)

    original_attributes = [attr for _, attr in original_data]
    processed_attributes = [attr for _, attr in processed_data]

    total_original = len(original_attributes)
    total_processed = len(processed_attributes)

    inconsistent_attributes = []
    for idx, attr in enumerate(processed_attributes):
        if attr not in original_attributes:
            inconsistent_attributes.append((idx, attr))

    print(f"Total original polygons: {total_original}")
    print(f"Total processed polygons: {total_processed}")
    print(f"Number of inconsistent attributes: {len(inconsistent_attributes)}")

    if inconsistent_attributes:
        print("\nInconsistent attributes details:")
        for idx, attr in inconsistent_attributes:
            print(f"- Processed polygon index: {idx}, Attribute: {attr}")
        return False

    print("All attributes are consistent!")
    return True


def test_simple_process_polygon():
    result = calculate_processed_geometry("testlayer_without_holes.gpkg", 4)
    assert len(result) == 2


def test_no_process_polygon():
    result = calculate_processed_geometry("testlayer_without_holes.gpkg", 5)
    assert len(result) == 1


def test_one_hole_polygon_process():
    result = calculate_processed_geometry("testlayer_one_hole.gpkg", 4)
    assert len(result) == 3


def test_two_holes_polygon_process():
    result = calculate_processed_geometry("testlayer_two_holes.gpkg", 4)
    assert len(result) == 8


def test_rectangle_process():
    result = calculate_processed_geometry("testlayer_rectangle.gpkg", 4)
    assert len(result) == 3


def test_c_process():
    result = calculate_processed_geometry("testlayer_c.gpkg", 4)
    assert len(result) == 8


def test_attribute_consistency():
    result = get_attributes_consistency("testlayer_c.gpkg", 4)
    assert result, "Test FAILED: Attributes are not consistent!"
