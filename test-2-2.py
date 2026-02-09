from core.base import Base
from core.openGL_utils import OpenGL_utils
from OpenGL.GL import *

#render a single point
class Test(Base):
    def initialize(self):
        print("Initializing progam...")

        ## initialize program ##

        #vertex shader code
        vertex_shader_code = '''
        void main(void) {
            gl_Position = vec4(0.0, 0.0, 0.0, 1.0);
        }
        '''

        #fragment shader code
        fragment_shader_code = '''
        out vec4 frag_color;
        void main(void) {
            frag_color = vec4(1.0, 1.0, 0.0, 1.0);
        }
        '''

        #send code to GPU and compile; store program reference
        self.program = OpenGL_utils.initialize_program(vertex_shader_code, fragment_shader_code)

        ## set up vertex array object ##
        vao = glGenVertexArrays(1)
        glBindVertexArray(vao)

        ## render settings (optional) ##
        #set point width and height
        glPointSize(10)
    
    def update(self):
        #select program to use when rendering
        glUseProgram(self.program)

        #render geometric objects using selected program
        glDrawArrays(GL_POINTS, 0, 1)

#instantiate class and run program
test = Test()
test.run()