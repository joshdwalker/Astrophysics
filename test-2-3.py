from core.base import Base
from core.openGL_utils import OpenGL_utils
from core.attribute import Attribute
from OpenGL.GL import *

#render 6 points in a hexagon arrangement
class Test(Base):
    def initialize(self):
        print('Initializing program...')

        ## initialize program ##
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

        ## render settings (optional) ##
        glLineWidth(1)

        ## set up vertex array object ##
        vao = glGenVertexArrays(1)
        glBindVertexArray(vao)

        ## set up vertex attribute ##
        position_data = [[0.8, 0.0, 0.0],
                         [0.4, 0.6, 0.0],
                         [-0.4, 0.6, 0.0],
                         [-0.8, 0.0, 0.0],
                         [-0.4, -0.6, 0.0],
                         [0.4, -0.6, 0.0]]
        self.vertex_count = len(position_data)
        position_attribute = Attribute('vec3', position_data)
        position_attribute.associate_variable(self.program, 'position')
    
    def update(self):
        glUseProgram(self.program)
        glDrawArrays(GL_TRIANGLE_FAN, 0, self.vertex_count)

#instantiate this class and run the program
test = Test()
test.run()