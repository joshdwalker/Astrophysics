from OpenGL.GL import *
import numpy as np

class Attribute(object):
    def __init__(self, data_type, data):
        #type of elements in data array:
        # int | float | vec2 | vec3 | vec4
        self.data_type = data_type

        #array of data tp be stored in buffer
        self.data = data

        #reference of available buffer from GPU
        self.buffer = glGenBuffers(1)

        #upload data immediately
        self.upload_data()

    #upload this data to a GPU buffer
    def upload_data(self):
        #convert data to numpy array format
        #convert numbers to 32 bit floats
        data = np.array(self.data).astype(np.float32)

        #select buffer used by the following functions
        glBindBuffer(GL_ARRAY_BUFFER, self.buffer)

        #store data in currently bound buffer
        glBufferData(GL_ARRAY_BUFFER, data.ravel(), GL_STATIC_DRAW)

    #associate variable in program with this buffer
    def associate_variable(self, program, variable_name):
        #get reference for program variable with given name
        variable = glGetAttribLocation(program, variable_name)

        #if the program does not reference the variable, then exit
        if variable == -1:
            return
        
        #select buffer used by the following functions
        glBindBuffer(GL_ARRAY_BUFFER, self.buffer)

        #specify how data will be read from the currently bound buffer into the specified variable
        if self.data_type == 'int':
            glVertexAttribPointer(variable, 1, GL_INT, False, 0, None)
        elif self.data_type == 'float':
            glVertexAttribPointer(variable, 1, GL_FLOAT, False, 0, None)
        elif self.data_type == 'vec2':
            glVertexAttribPointer(variable, 2, GL_FLOAT, False, 0, None)
        elif self.data_type == 'vec3':
            glVertexAttribPointer(variable, 3, GL_FLOAT, False, 0, None)
        elif self.data_type == 'vec4':
            glVertexAttribPointer(variable, 4, GL_FLOAT, False, 0, None)
        else:
            raise Exception('Attribute ' + variable + ' has unknown type ' + self.data_type)
        
        #indicate that the data will be streamed to this variable
        glEnableVertexAttribArray(variable)