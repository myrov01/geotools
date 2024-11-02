import geopandas as gpd
from shapely.geometry import MultiPolygon, Polygon


gdf = gpd.read_file(
    r"C:\Users\user\Desktop\vegetation-polygon_1\vegetation-polygon.gpkg")


def geom_calc(geom):
    if geom.is_empty:
        return 0
    elif geom.geom_type == 'Polygon':
        exterior_points = len(geom.exterior.coords)
        interior_points = sum(len(interior.coords)
                              for interior in geom.interiors)
        return exterior_points + interior_points
    elif geom.geom_type == 'MultiPolygon':
        return sum(geom_calc(polygon) for polygon in geom.geoms)
    else:
        return 0


gdf['point_count'] = gdf['geometry'].apply(geom_calc)

total_points = gdf['point_count'].sum()

print(f"Общее кол-во точек: {total_points}")

# if __name__ == '__main__':
#     geodataframe = geopandas.read_file(
#         r"C:\Users\user\Desktop\vegetation-polygon_1\vegetation-polygon.gpkg")
#     # geom_calc(geometry)


# def geom_calc(geometry):

#     return len(geometry.coords)
#     pass
