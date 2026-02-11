import pygame
import sys
from core.input import Input

class Base(object):
    def __init__(self, screen_size = [512, 512]):
        #initialize all pygame modules
        pygame.init()
        #indicate rendering details
        display_flags = pygame.DOUBLEBUF | pygame.OPENGL
        #initialize buffers to perform antialiasing
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1)
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLESAMPLES, 4)
        #use a core OpenGL profile for cross-platform compatability
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)
        #create and display the window
        self.screen = pygame.display.set_mode(screen_size, display_flags)
        #set the text that appears in the title bar of the window
        pygame.display.set_caption('Graphics Window')

        #running state determines if main loop is active
        self.running = True
        self.clock = pygame.time.Clock()

        #manage user input
        self.input = Input()

        #number of seconds the application has been running
        self.time = 0

    #this will be implemented by a child class
    def initialize(self):
        pass
    
    #this will be implemented by a child class
    def update(self):
        pass

    def run(self):
        ## startup ##
        self.initialize()

        ## main loop ##
        while self.running:
            ## process input ##
            self.input.update()
            if self.input.quit:
                self.running = False

            ## update ##
            #seconds since iterations of run loop
            self.delta_time = self.clock.get_time() / 1000
            #incremenet the time that the application has been running
            self.time += self.delta_time
            self.update()

            ## render ##
            #display image on screen
            pygame.display.flip()

            #pause if necessary to achieve 60 fps
            self.clock.tick(60)
        
        ## shut down ##
        pygame.quit()
        sys.exit()