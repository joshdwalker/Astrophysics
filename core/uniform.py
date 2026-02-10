from OpenGL.GL import *

class Uniform(object):
    def __init__(self, data_type, data):
        #type of datat
        # int | bool | float | vec2 | vec3 | vec4
        self.data_type = data_type

        #data to be sent to uniform variable
        self.data = data

        #reference for variable location in the program
        self.variable = None
    
    #get and store reference for program variable with given name
    def locate_variable(self, program, variable_name):
        self.variable = glGetUniformLocation(program, variable_name)
    
    #store data in uniform variable previously located
    def upload_data(self):
        #if the program does not reference the variable, then exit
        if self.variable == -1:
            return
        
        if self.data_type == 'int':
            glUniform1i(self.variable, self.data)
        elif self.data_type == 'bool':
            glUniform1i(self.variable, self.data)
        elif self.data_type == 'float':
            glUniform1f(self.variable, self.data)
        elif self.data_type == 'vec2':
            glUniform2f(self.variable, self.data[0], self.data[1])
        elif self.data_type == 'vec3':
            glUniform3f(self.variable, self.data[0], self.data[1], self.data[2])
        elif self.data_type == 'vec4':
            glUniform4f(self.variable, self.data[0], self.data[1], self.data[2], self.data[3])