from core.geometry.geometry import Geometry
from math import sin, cos, pi

class Polygon_Geometry(Geometry):
    def __init__(self, sides = 3, radius = 1):
        super().__init__()

        position_data = []
        color_data = []

        for i in range(sides):
            position_data.append([0.0, 0.0, 0.0])
            position_data.append([radius * cos(i * 2 * pi / sides), radius * sin(i * 2 * pi / sides), 0.0])
            position_data.append([radius * cos((i + 1) * 2 * pi / sides), radius * sin((i + 1) * 2 * pi / sides), 0.0])
            color_data.append([1.0, 1.0, 1.0])
            color_data.append([1.0, 0.0, 0.0])
            color_data.append([0.0, 0.0, 1.0])

            self.add_attribute('vec3', position_data)
            self.add_attribute('vec3', color_data)
            self.count_vertices()