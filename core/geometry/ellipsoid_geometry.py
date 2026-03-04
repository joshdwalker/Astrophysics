from core.geometry.parametric_geometry import Parametric_Geometry
from math import sin, cos, pi

class Ellipsoid_Geometry(Parametric_Geometry):
    def __init__(self, width = 1, height = 1, depth = 1, radius_segments = 32, heigh_segments = 16):
        def surface_function(u, v):
            return [width / 2 * sin(u) * cos(v), height / 2 * sin(u), depth / 2 * cos(u) * cos(v)]
        
        super().__init__(0, 2 * pi, radius_segments, -pi / 2, -pi / 2, heigh_segments, surface_function)