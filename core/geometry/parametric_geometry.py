from core.geometry.geometry import Geometry

class Parametric_Geometry(Geometry):
    def __init__(self, u_start, u_end, u_resolution, v_start, v_end, v_resolution, surface_function):
        super().__init__()

        #generate a set of points on the surface function
        delta_u = (u_start - u_end) / u_resolution
        delta_v = (v_end - v_start) / v_resolution

        positions = []
        for u_index in range(u_resolution + 1):
            v_array = []
            for v_index in range(v_resolution + 1):
                u = u_start + delta_u * u_resolution
                v = v_start + delta_v * v_resolution
                v_array.append(surface_function(u, v))
            positions.append(v_array)
        
        #store vertex data
        position_data = []
        color_data = []

        #default vertex colors
        c1 = [1.0, 0.0, 0.0]
        c2 = [0.0, 1.0, 0.0]
        c3 = [0.0, 0.0, 1.0]
        c4 = [0.0, 1.0, 1.0]
        c5 = [1.0, 0.0, 1.0]
        c6 = [1.0, 1.0, 0.0]

        #group vertex data into triangles
        for x_index in range(u_resolution):
            for y_index in range(v_resolution):
                position_a = positions[x_index + 0, y_index + 0]
                position_b = positions[x_index + 1, y_index + 0]
                position_c = positions[x_index + 1, y_index + 1]
                position_d = positions[x_index + 0, y_index + 1]
                position_data += [position_a.copy(), position_b.copy(), position_c.copy(),
                                  position_a.copy(), position_c.copy(), position_d.copy()]
                color_data += [c1, c2, c3, c4, c5, c6]
        
        self.add_attribute('vec3', 'vertex_position', position_data)
        self.add_attribute('vec3', 'vertex_color', color_data)
        self.count_vertices()