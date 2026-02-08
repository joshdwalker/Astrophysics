from OpenGL.GL import *

#static methods to load and compile OpenGL shaders and link to create programs
class OpenGL_utils(object):
    @staticmethod
    def initialize_shader(shader_code, shader_type):
        #specify required OpenGL/GLSL version
        shader_code = '#version 330\n' + shader_code

        #create empty shader object and return reference value
        shader = glCreateShader(shader_type)
        #store the source code in the shader
        glShaderSource(shader, shader_type)
        #compile the source code previously stored in the shader object
        glCompileShader(shader)

        #queries whether shader compilation was successful
        compile_success = glGetShaderiv(shader, GL_COMPILE_STATUS)

        if not compile_success:
            #retrieve error message
            error_message = glGetShaderInfoLog(shader)
            #free memory used to store shader program
            glDeleteShader(shader)
            #convert byte string to character string
            error_message = '\n' + error_message.decode('utf-8')
            #raise exception: halt program and print error message
            raise Exception(error_message)
        
        #compilation was successful; return shader reference value
        return shader
    
    @staticmethod
    def initialize_program(vertex_shader_code, fragment_shader_code):
        vertex_shader = OpenGL_utils.initialize_shader(vertex_shader_code, GL_VERTEX_SHADER)
        fragment_shader = OpenGL_utils.initialize_shader(fragment_shader_code, GL_FRAGMENT_SHADER)

        #create an empty program object and store reference to it
        program = glCreateProgram()

        #attach previously compiled shader programs
        glAttachShader(program, vertex_shader)
        glAttachShader(program, fragment_shader)

        #link vertex shader to fragment shader
        glLinkProgram(program)

        #query whether program link was successful
        link_success = glGetProgramiv(program, GL_LINK_STATUS)
        if not link_success:
            #retrieve error message
            error_message = glGetProgramInfoLog(program)
            #free memory used to store program
            glDeleteProgram(program)
            error_message = '\n' + error_message.decode('utf-8')
            #raise exception: halt application and print error message
            raise Exception(error_message)
        
        #linking was successful; return program reference value
        return program
    
    @staticmethod
    def print_system_info():
        print('Vendor: ' + glGetString(GL_VENDOR).decode('utf-8'))
        print('Renderer: ' + glGetString(GL_RENDERER).decode('utf-8'))
        print('OpenGL version supported: ' + glGetString(GL_VERSION).decode('utf-8'))
        print('GLSL version supported: ' +glGetString(GL_SHADING_LANGUAGE_VERSION).decode('utf-8'))