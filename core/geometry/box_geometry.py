from core.geometry.geometry import Geometry

class Box_Geometry(Geometry):
    def __init__(self, width = 1, height = 1, depth = 1):
        p0 = [-width / 2, -height / 2, -depth / 2]
        p1 = [ width / 2, -height / 2, -depth / 2]
        p2 = [-width / 2,  height / 2, -depth / 2]
        p3 = [ width / 2,  height / 2, -depth / 2]
        p4 = [-width / 2, -height / 2,  depth / 2]
        p5 = [ width / 2, -height / 2,  depth / 2]
        p6 = [-width / 2,  height / 2,  depth / 2]
        p7 = [ width / 2,  height / 2,  depth / 2]
        #colors for faces in order: x+, x-, y+, y-, z+, z-
        c1 = [1, 0.5, 0.5]
        c2 = [0.5, 0, 0]
        c3 = [0.5, 1, 0.5]
        c4 = [0, 0.5, 0]
        c5 = [0.5, 0.5, 1]
        c6 = [0, 0, 0.5]
        position_data = [p5, p1, p3, p5, p3, p7,
                         p0, p4, p6, p0, p6, p2,
                         p6, p7, p3, p6, p3, p2,
                         p0, p1, p5, p0, p5, p4,
                         p4, p5, p7, p4, p7, p6,
                         p1, p0, p2, p1, p2, p3]
        color_data = [c1] * 6 + [c2] * 6 + [c3] * 6 + [c4] * 6 + [c5] * 6 + [c6] * 6
        self.add_attribute('vec3', 'vertex_position', position_data)
        self.add_attribute('v3c3', 'vertex_color', color_data)
        self.count_vertices()