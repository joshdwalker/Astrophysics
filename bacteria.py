from core.base import Base
from core.openGL_utils import OpenGL_utils
from core.attribute import Attribute
from core.uniform import Uniform
from OpenGL.GL import *
from math import sqrt

class Bacteria(Base):
    def replicate(self, bacteria):
        if bacteria not in self.bacteria_list:
            return False
        right_bacteria = bacteria.copy()
        up_bacteria = bacteria.copy()
        right_bacteria[0] += 1
        up_bacteria[1] += 1
        if right_bacteria not in self.bacteria_list and up_bacteria not in self.bacteria_list:
            self.bacteria_list.remove(bacteria)
            self.bacteria_list.append(right_bacteria)
            self.bacteria_list.append(up_bacteria)
            self.move_selected_bacteria('')
            self.moves += 1
            print(f'used {self.moves} moves so far')
            return True
        else:
            return False

    def move_selected_bacteria(self, direction):
        #can't move cursor when there's only one bacteria (or none)
        if len(self.bacteria_list) in [0, 1]:
            return
        new_bacteria_list = self.bacteria_list.copy()
        cursor = self.selected_bacteria.copy()
        if self.selected_bacteria in new_bacteria_list:
            new_bacteria_list.remove(self.selected_bacteria)
        if direction == 'left' or direction == 'a':
            cursor[0] -= 1
        if direction == 'up' or direction == 'w':
            cursor[1] += 1
        if direction == 'right' or direction == 'd':
            cursor[0] += 1
        if direction == 'down' or direction == 's':
            cursor[1] -= 1
        distances = [sqrt((bacteria[0] - cursor[0]) ** 2 + (bacteria[1] - cursor[1]) ** 2) for bacteria in new_bacteria_list]
        self.selected_bacteria = new_bacteria_list[distances.index(min(distances))]


    def initialize(self):
        #handle bacteria-related things
        self.moves = 0
        self.selected_bacteria = [0.0, 0.0, 0.0]
        self.bacteria_list = [[0.0, 0.0, 0.0]]
        self.grid_list = [[0.0, 0.0, 0.0],
                          [1.0, 0.0, 0.0],
                          [2.0, 0.0, 0.0],
                          [3.0, 0.0, 0.0],
                          [0.0, 1.0, 0.0],
                          [1.0, 1.0, 0.0],
                          [2.0, 1.0, 0.0],
                          [3.0, 1.0, 0.0],
                          [0.0, 2.0, 0.0],
                          [1.0, 2.0, 0.0],
                          [2.0, 2.0, 0.0],
                          [3.0, 2.0, 0.0],
                          [0.0, 3.0, 0.0],
                          [1.0, 3.0, 0.0],
                          [2.0, 3.0, 0.0],
                          [3.0, 3.0, 0.0]]

        print("Initializing program...")

        vertex_shader_code = '''
        in vec3 position;
        void main(void) {
            gl_Position = vec4(position.x, position.y, position.z, 1.0);
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

        #settings: larger more visible point size
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glPointSize(10)

        #initalize grid vao
        self.grid_vao = glGenVertexArrays(1)
        glBindVertexArray(self.grid_vao)

        self.grid_attribute = Attribute('vec3', list(self.grid_list))
        self.grid_attribute.associate_variable(self.program, 'position')

        self.grid_color = Uniform('vec3', [1.0, 1.0, 1.0])
        self.grid_color.locate_variable(self.program, 'base_color')

        #initalize selected bacteria vao
        self.selected_bacteria_vao = glGenVertexArrays(1)
        glBindVertexArray(self.selected_bacteria_vao)

        self.selected_bacteria_attribute = Attribute('vec3', [self.selected_bacteria])
        self.selected_bacteria_attribute.associate_variable(self.program, 'position')

        self.selected_bacteria_color = Uniform('vec3', [0.0, 0.0, 1.0])
        self.selected_bacteria_color.locate_variable(self.program, 'base_color')

        #initalize bacteria vao
        self.bacteria_vao = glGenVertexArrays(1)
        glBindVertexArray(self.bacteria_vao)

        self.bacteria_attribute = Attribute('vec3', self.bacteria_list)
        self.bacteria_attribute.associate_variable(self.program, 'position')

        self.bacteria_color = Uniform('vec3', [0.0, 1.0, 0.0])
        self.bacteria_color.locate_variable(self.program, 'base_color')

        self.flag = 0

    def update(self):
        #try to replicate a bacteria
        if self.input.is_key_down('e'):
            if not self.replicate(self.selected_bacteria):
                print('Selected bacteria does not have space to replicate')
        
        #move the cursor
        elif len(self.input.key_down_list) > 0:
            self.move_selected_bacteria(self.input.key_down_list[0])

        #use program
        glUseProgram(self.program)
        
        #clear the screen
        glClear(GL_COLOR_BUFFER_BIT)

        #update all the data in each attribute to normalize to the screen
        gmin = min([self.grid_list[i // 3][i % 3] for i in range(3 * len(self.grid_list))])
        gmax = max([self.grid_list[i // 3][i % 3] for i in range(3 * len(self.grid_list))])
        bmin = min([self.bacteria_list[i // 3][i % 3] for i in range(3 * len(self.bacteria_list))])
        bmax = max([self.bacteria_list[i // 3][i % 3] for i in range(3 * len(self.bacteria_list))])
        minimum = min(gmin, bmin) - 1
        maximum = max(gmax, bmax) + 1
        self.grid_attribute.data = [[(2 * x - maximum - minimum) / (maximum - minimum) for x in y] for y in self.grid_list]
        self.bacteria_attribute.data = [[(2 * x - maximum - minimum) / (maximum - minimum) for x in y] for y in self.bacteria_list]
        self.selected_bacteria_attribute.data = [(2 * x - maximum - minimum) / (maximum - minimum) for x in self.selected_bacteria]

        #draw grid
        glBindVertexArray(self.grid_vao)
        self.grid_attribute.upload_data()
        self.grid_color.upload_data()
        glDrawArrays(GL_POINTS, 0, len(self.grid_list))
        
        #update bacteria data and draw bacteria
        glBindVertexArray(self.bacteria_vao)
        self.bacteria_attribute.upload_data()
        self.bacteria_color.upload_data()
        glDrawArrays(GL_POINTS, 0, len(self.bacteria_list))

        #update selected bacteria data
        glBindVertexArray(self.selected_bacteria_vao)
        self.selected_bacteria_attribute.upload_data()
        self.selected_bacteria_color.upload_data()
        glDrawArrays(GL_POINTS, 0, 1)

b = Bacteria()
b.run()