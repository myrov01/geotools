import math
import geopandas as gpd

def calculate_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:

    R: float = 6371000
    phi1: float = math.radians(lat1)
    phi2: float = math.radians(lat2)
    delta_phi: float = math.radians(lat2 - lat1)
    delta_lambda: float = math.radians(lon2 - lon1)

    a: float = math.sin(delta_phi / 2) ** 2 + \
        math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2

    c: float = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance: float = R * c
    return distance