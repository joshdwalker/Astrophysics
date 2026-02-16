from core.base import Base
from core.openGL_utils import OpenGL_utils
from core.attribute import Attribute
from core.uniform import Uniform
from core.matrix import Matrix
from OpenGL.GL import *
from math import pi
import numpy as np

class Test(Base):
    def initialize(self):
        print("Initializing program...")

        vertex_shader_code = '''
        in vec3 position;
        uniform mat4 model;
        uniform mat4 perspective;
        void main(void) {
            gl_Position = perspective * model * vec4(position, 1.0);
        }
        '''

        fragment_shader_code = '''
        uniform vec3 base_color;
        out vec4 frag_color;
        void main(void) {
            frag_color = vec4(base_color, 1.0);
        }
        '''

        self.program = OpenGL_utils.initialize_program(vertex_shader_code, fragment_shader_code)

        #render settings
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glEnable(GL_DEPTH_TEST)

        #set up vao object
        vao = glGenVertexArrays(1)
        glBindVertexArray(vao)

        position_data = [[0.0, 0.2, 0.0],
                         [0.1, -0.2, 0.0],
                         [-0.1, -0.2, 0.0]]
        self.vertex_count = len(position_data)
        position_attribute = Attribute('vec3', position_data)
        position_attribute.associate_variable(self.program, 'position')

        #set up uniforms
        self.model_matrix = Uniform('mat4', Matrix.make_translation(0.0, 0.0, -1.0))
        self.model_matrix.locate_variable(self.program, 'model')

        self.projection_matrix = Uniform('mat4', Matrix.make_perspective())
        self.projection_matrix.locate_variable(self.program, 'perspective')

        self.base_color = Uniform('vec3', [0.0, 1.0, 0.0])
        self.base_color.locate_variable(self.program, 'base_color')

        #movement speed in units per second
        self.movement_speed = 0.5
        #rotation speed in radians per second
        self.rotation_speed = 90 * (pi / 180)

    def update(self):
        #update data
        displacement = self.movement_speed * self.delta_time
        angle_displacement = self.rotation_speed * self.delta_time

        #global translation
        if self.input.is_key_pressed('w'):
            temp_matrix = Matrix.make_translation(0.0, displacement, 0.0)
            self.model_matrix.data = np.matmul(temp_matrix, self.model_matrix.data)
        if self.input.is_key_pressed('s'):
            temp_matrix = Matrix.make_translation(0.0, -displacement, 0.0)
            self.model_matrix.data = np.matmul(temp_matrix, self.model_matrix.data)
        if self.input.is_key_pressed('a'):
            temp_matrix = Matrix.make_translation(-displacement, 0.0, 0.0)
            self.model_matrix.data = np.matmul(temp_matrix, self.model_matrix.data)
        if self.input.is_key_pressed('d'):
            temp_matrix = Matrix.make_translation(displacement, 0.0, 0.0)
            self.model_matrix.data = np.matmul(temp_matrix, self.model_matrix.data)
        if self.input.is_key_pressed('z'):
            temp_matrix = Matrix.make_translation(0.0, 0.0, displacement)
            self.model_matrix.data = np.matmul(temp_matrix, self.model_matrix.data)
        if self.input.is_key_pressed('x'):
            temp_matrix = Matrix.make_translation(0.0, 0.0, -displacement)
            self.model_matrix.data = np.matmul(temp_matrix, self.model_matrix.data)
        
        #global rotation
        if self.input.is_key_pressed('q'):
            temp_matrix = Matrix.make_rotation_z(angle_displacement)
            self.model_matrix.data = np.matmul(temp_matrix, self.model_matrix.data)
        if self.input.is_key_pressed('e'):
            temp_matrix = Matrix.make_rotation_z(-angle_displacement)
            self.model_matrix.data = np.matmul(temp_matrix, self.model_matrix.data)
        
        #local translation
        if self.input.is_key_pressed('i'):
            temp_matrix = Matrix.make_translation(0.0, displacement, 0.0)
            self.model_matrix.data = np.matmul(self.model_matrix.data, temp_matrix)
        if self.input.is_key_pressed('k'):
            temp_matrix = Matrix.make_translation(0.0, -displacement, 0.0)
            self.model_matrix.data = np.matmul(self.model_matrix.data, temp_matrix)
        if self.input.is_key_pressed('j'):
            temp_matrix = Matrix.make_translation(-displacement, 0.0, 0.0)
            self.model_matrix.data = np.matmul(self.model_matrix.data, temp_matrix)
        if self.input.is_key_pressed('l'):
            temp_matrix = Matrix.make_translation(displacement, 0.0, 0.0)
            self.model_matrix.data = np.matmul(self.model_matrix.data, temp_matrix)
        
        #local rotation
        if self.input.is_key_pressed('u'):
            temp_matrix = Matrix.make_rotation_z(angle_displacement)
            self.model_matrix.data = np.matmul(self.model_matrix.data, temp_matrix)
        if self.input.is_key_pressed('o'):
            temp_matrix = Matrix.make_rotation_z(-angle_displacement)
            self.model_matrix.data = np.matmul(self.model_matrix.data, temp_matrix)

        #render scene
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.program)
        self.model_matrix.upload_data()
        self.projection_matrix.upload_data()
        self.base_color.upload_data()
        glDrawArrays(GL_TRIANGLES, 0, self.vertex_count)
    
#instantiate the class and run the program
test = Test()
test.run()