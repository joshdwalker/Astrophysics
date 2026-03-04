from core.geometry.parametric_geometry import Parametric_Geometry

class Plane_Geometry(Parametric_Geometry):
    def __init__(self, width, height, width_segments, height_segments):
        def surface_function(u, v):
            return [u, v, 0]
        
        super().__init__(-width / 2, width / 2, width_segments, -height / 2, height / 2, height_segments, surface_function)