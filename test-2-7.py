from core.base import Base
from core.openGL_utils import OpenGL_utils
from core.attribute import Attribute
from core.uniform import Uniform
from OpenGL.GL import *

class Test(Base):
    def initialize(self):
        print('Initializing program...')

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

        ### render settings (optional) ###
        #specify the color to be used when clearning
        glClearColor(0.0, 0.0, 0.0, 1.0)

        ### set up vao ###
        vao = glGenVertexArrays(1)
        glBindVertexArray(vao)

        ### set up vertex attributes ###
        position_data = [[0.0, 0.2, 0.0],
                         [0.2, -0.2, 0.0],
                         [-0.2, -0.2, 0.0]]
        self.vertex_count = len(position_data)
        position_attribute = Attribute('vec3', position_data)
        position_attribute.associate_variable(self.program, 'position')

        ### set up uniforms ###
        self.translation = Uniform('vec3', [-0.5, 0.0, 0.0])
        self.translation.locate_variable(self.program, 'translation')

        self.base_color = Uniform('vec3', [1.0, 0.0, 0.0])
        self.base_color.locate_variable(self.program, 'base_color')
    
    def update(self):
        ### update date ###
        #increase x-coordinate of translation
        self.translation.data[0] += 0.01
        #if triangle passes off-screen on the right, change it so it appears on the left
        if self.translation.data[0] > 1.2:
            self.translation.data[0] = -1.2
        
        ### render scene ###
        #reset color buffer with specified color
        glClear(GL_COLOR_BUFFER_BIT)

        glUseProgram(self.program)
        self.translation.upload_data()
        self.base_color.upload_data()
        glDrawArrays(GL_TRIANGLES, 0, self.vertex_count)

#instantiate test object and run
test = Test()
test.run()