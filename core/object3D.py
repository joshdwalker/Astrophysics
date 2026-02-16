from core.matrix import Matrix
import numpy as np

class Object3D(object):
    def __init__(self):
        self.transform = Matrix.make_identity()
        self.parent = None
        self.children = []
    
    def add(self, child):
        self.children.append(child)
        child.parent = self
    
    def remove(self, child):
        self.children.remove(child)
        child.parent = None
    
    #calculate transformation of this Object3D relative to the root Object3D of the scene graph
    def get_world_matrix(self):
        if self.parent == None:
            return self.transform
        return np.matmul(self.parent.get_world_matrix(), self.transform)
    
    #return a single list containing all descendants
    def get_descendant_list(self):
        #master list of all descendant nodes
        descendants = []
        #nodes to be added to descendants list, and whose children will be added to this list
        nodes_to_process = [self]
        while len(nodes_to_process) > 0:
            #remove first node from list
            node = nodes_to_process.pop(0)
            #add this node to descendant list
            descendants.append(node)
            #children of this node must also be processed
            nodes_to_process = node.children + nodes_to_process
        return descendants
    
    #apply geometric transformations
    def apply_matrix(self, matrix, local_transformation = True):
        if local_transformation:
            self.transform = np.matmul(self.transform, matrix)
        else:
            self.transform = np.matmul(matrix, self.transform)
    
    def translate(self, x, y, z, local_transformation = True):
        matrix = Matrix.make_translation(x, y, z)
        self.apply_matrix(matrix, local_transformation)
    
    def rotate_x(self, angle, local_transformation = True):
        matrix = Matrix.make_rotation_x(angle)
        self.apply_matrix(matrix, local_transformation)
    
    def rotate_y(self, angle, local_transformation = True):
        matrix = Matrix.make_rotation_y(angle)
        self.apply_matrix(matrix, local_transformation)
    
    def rotate_z(self, angle, local_transformation = True):
        matrix = Matrix.make_rotation_z(angle)
        self.apply_matrix(matrix, local_transformation)
    
    def scale(self, scalar, local_transformation = True):
        matrix = Matrix.make_scale(scalar)
        self.apply_matrix(matrix, local_transformation)
    
    #get/set position components of transform
    def get_position(self):
        return [self.transform.item((0, 3)),
                self.transform.item((1, 3)),
                self.transform.item((2, 3))]
    
    def get_world_position(self):
        world_transform = self.get_world_matrix()
        return [world_transform.item((0, 3)),
                world_transform.item((1, 3)),
                world_transform.item((2, 3))]
    
    def set_position(self, position):
        self.transform.itemset((0, 3), position[0])
        self.transform.itemset((1, 3), position[1])
        self.transform.itemset((2, 3), position[2])