from core.base import Base
from core.openGL_utils import OpenGL_utils
from core.attribute import Attribute
from core.uniform import Uniform
from OpenGL.GL import *

#render two triangles with different positions and colors
class Test(Base):
    def initialize(self):
        print("Initializing program...")

        vertex_shader_code = '''
        in vec3 position;
        uniform vec3 translation;
        void main(void) {
            vec3 translated_position = position + translation;
            gl_Position = vec4(translated_position.x, translated_position.y, translated_position.z, 1.0);
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

        ### set up vertex array object ###
        vao = glGenVertexArrays(1)
        glBindVertexArray(vao)

        ### set up the vertex attribute ###
        position_data = [[0.0, 0.2, 0.0],
                         [0.2, -0.2, 0.0],
                         [-0.2, -0.2, 0.0]]
        self.vertex_count = len(position_data)
        position_attribute = Attribute('vec3', position_data)
        position_attribute.associate_variable(self.program, 'position')

        ### set up uniforms ###
        self.translation1 = Uniform('vec3', [-0.5, 0.0, 0.0])
        self.translation1.locate_variable(self.program, 'translation')

        self.translation2 = Uniform('vec3', [0.5, 0.0, 0.0])
        self.translation2.locate_variable(self.program, 'translation')

        self.base_color1 = Uniform('vec3', [1.0, 0.0, 0.0])
        self.base_color1.locate_variable(self.program, 'base_color')

        self.base_color2 = Uniform('vec3', [0.0, 0.0, 1.0])
        self.base_color2.locate_variable(self.program, 'base_color')
    
    def update(self):
        glUseProgram(self.program)

        #draw the first triangle
        self.translation1.upload_data()
        self.base_color1.upload_data()
        glDrawArrays(GL_TRIANGLES, 0, self.vertex_count)

        #draw the second triangle
        self.translation2.upload_data()
        self.base_color2.upload_data()
        glDrawArrays(GL_TRIANGLES, 0, self.vertex_count)

#instantiate the test object and run it
test = Test()
test.run()