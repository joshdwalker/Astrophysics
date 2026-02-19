from core.attribute import Attribute

class Geometry(object):
    def __init__(self):
        #store Attribute objects, indexed by name of associated variable in shader
        #shader variable associations set up later and stored in vertex array object in Mesh
        self.attributes = {}

        #number of vertices
        self.vertex_count = None
    
    def add_attribute(self, data_type, variable_name, data):
        self.attributes[variable_name] = Attribute(data_type, data)
    
    def count_vertices(self):
        #number of vertices may be calculated from the length of any Attribute object's array of data
        attribute = list(self.attributes.values())[0]
        self.vertex_count = len(attribute.data)