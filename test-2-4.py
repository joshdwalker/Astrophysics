from core.base import Base
from core.openGL_utils import OpenGL_utils
from core.attribute import Attribute
from OpenGL.GL import *

#render two shapes
class Test(Base):
    def initialize(self):
        print('Initializing program...')

        vertex_shader_code = '''
        in vec3 position;
        void main(void) {
            gl_Position = vec4(position.x, position.y, position.z, 1.0);
        }
        '''

        fragment_shader_code = '''
        out vec4 frag_color;
        void main(void) {
            frag_color = vec4(1.0, 1.0, 0.0, 1.0);
        }
        '''

        self.program = OpenGL_utils.initialize_program(vertex_shader_code, fragment_shader_code)

        #render settings
        glLineWidth(4)

        ### set up vao - triangle ###
        self.vao_triangle = glGenVertexArrays(1)
        glBindVertexArray(self.vao_triangle)
        position_data_triangle = [[-0.5, 0.8, 0.0],
                                  [-0.2, 0.2, 0.0],
                                  [-0.8, 0.2, 0.0]]
        self.vertex_count_triangle = len(position_data_triangle)
        position_attribute_triangle = Attribute('vec3', position_data_triangle)
        position_attribute_triangle.associate_variable(self.program, 'position')

        ##set up vao - square ##
        self.vao_square = glGenVertexArrays(1)
        glBindVertexArray(self.vao_square)
        position_data_square = [[0.8, 0.8, 0.0],
                                [0.8, 0.2, 0.0],
                                [0.2, 0.2, 0.0],
                                [0.2, 0.8, 0.0]]
        self.vertex_count_square = len(position_data_square)
        position_attribute_square = Attribute('vec3', position_data_square)
        position_attribute_square.associate_variable(self.program, 'position')

    def update(self):
        #using same program to render both shapes
        glUseProgram(self.program)
        glBindVertexArray(self.vao_triangle)
        glDrawArrays(GL_LINE_LOOP, 0, self.vertex_count_triangle)

        glBindVertexArray(self.vao_square)
        glDrawArrays(GL_LINE_LOOP, 0, self.vertex_count_square)

test = Test()
test.run()