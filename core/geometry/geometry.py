from core.attribute import Attribute
import numpy as np

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

    #transform the data in an attribute using a matrix
    def apply_matrix(self, matrix, variable_name = 'vertex_position'):
        old_position_data = self.attributes[variable_name].data
        new_position_data = []
        
        for old_position in old_position_data:
            #avoid changing list references
            new_position = old_position.copy()
            #add homogeneous fourth coordinate
            new_position.append(1)
            #multiply by matrix
            new_position = np.matmul(matrix, new_position)
            #remove homogeneous coordinate
            new_position = list(new_position[0:3])
            #add to new data list
            new_position_data.append(new_position)
        
        self.attributes[variable_name].data = new_position_data
        #new data must be uploaded
        self.attributes[variable_name].upload_data()
    
    #merge data from attributes of other geometry into this object
    #requires both geometries to have attributes with the same names
    def merge(self, other_geometry):
        for variable_name, attribute_object in self.attributes.items():
            attribute_object.data += other_geometry.attributes[variable_name].data
            #new data must be uploaded
            attribute_object.upload_data()
        
        #update the number of vertices
        self.count_vertices()