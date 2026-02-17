from core.object3D import Object3D
from OpenGL.GL import *

class Mesh(Object3D):
    def __init__(self, geometry, material):
        super().__init__()

        self.geometry = geometry
        self.material = material

        #should this object be rendered?
        self.visible = True

        #set up associations between attributes stored in geometry and shader program stored in material
        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)
        for variable_name, attribute in geometry.attributes.items():
            attribute.associate_variable(material.program, variable_name)
        #unbind this vertex array
        glBindVertexArray(0)