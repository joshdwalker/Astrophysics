from core.geometry.ellipsoid_geometry import Ellipsoid_Geometry
from math import sin, cos, pi

class Sphere_Geometry(Ellipsoid_Geometry):
    def __init__(self, radius = 1, radius_segments = 32, height_segments = 16):
        super().__init__(2 * radius, 2 * radius, 2 * radius, radius_segments, height_segments)