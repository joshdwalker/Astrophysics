from core.base import Base
from core.openGL_utils import OpenGL_utils
from core.attribute import Attribute
from core.uniform import Uniform
from OpenGL.GL import *
from math import cos, sin

class Test(Base):
    def initialize(self):
        print("Initializing program...")

        vertex_shader_code = '''
        in vec3 position;
        uniform vec3 translation;
        void main(void) {
            vec3 pos2 = position + translation;
            gl_Position = vec4(pos2.x, pos2.y, pos2.z, 1.0);
        }
        '''

        fragment_shader_code = '''
        uniform vec3 base_color;
        out vec4 frag_color;
        void main(void) {
            frag_color = vec4(base_color.r, base_color.g, base_color.b, 1.0);
        }
        '''

        self.program = OpenGL_utils.initialize_program(vertex_shader_code, fragment_shader_code)

        glClearColor(0.0, 0.0, 0.0, 0.0)

        vao = glGenVertexArrays(1)
        glBindVertexArray(vao)

        position_data = [[0.2, 0.0, 0.0],
                         [0.0, 0.34, 0.0],
                         [-0.2, 0.0, 0.0]]
        self.vertex_count = len(position_data)
        position_attribute = Attribute('vec3', position_data)
        position_attribute.associate_variable(self.program, 'position')

        self.translation = Uniform('vec3', [0.8, 0.0, 0.0])
        self.translation.locate_variable(self.program, 'translation')

        self.base_color = Uniform('vec3', [0.0, 1.0, 0.0])
        self.base_color.locate_variable(self.program, 'base_color')
    
    def update(self):
        glUseProgram(self.program)

        self.translation.data[0] = 0.8 * cos(self.time)
        self.translation.data[1] = 0.8 * sin(self.time) - 0.17

        self.base_color.data[1] = 0.5 + 0.5 * cos(2 * self.time)

        glClear(GL_COLOR_BUFFER_BIT)

        self.translation.upload_data()
        self.base_color.upload_data()
        glDrawArrays(GL_TRIANGLES, 0, self.vertex_count)

test = Test()
test.run()