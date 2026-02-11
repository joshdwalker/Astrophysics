import pygame

class Input(object):
    def __init__(self):
        #lists to store key states
        #down, up: discrete events; lasts for one iteration
        #pressed: continuous event; between down and up events
        self.key_down_list = []
        self.key_pressed_list = []
        self.key_up_list = []

        #has the user quit the application?
        self.quit = False
    
    def update(self):
        #reset discrete key states
        self.key_down_list = []
        self.key_up_list = []

        #iterate over all user input events (such as keyboard or mouse)
        # that occured since the last time events were checked
        for event in pygame.event.get():
            #check for keydown and keyup events; get name of key from event and
            # append to or remove from corresponding list
            if event.type == pygame.KEYDOWN:
                key_name = pygame.key.name(event.key)
                self.key_down_list.append(key_name)
                self.key_pressed_list.append(key_name)
            if event.type == pygame.KEYUP:
                key_name = pygame.key.name(event.key)
                self.key_pressed_list.remove(key_name)
                self.key_up_list.append(key_name)
            #quit event occurs by clicking button to close window
            if event.type == pygame.QUIT:
                self.quit = True
    
    def is_key_down(self, key):
        return key in self.key_down_list
    def is_key_pressed(self, key):
        return key in self.key_pressed_list
    def is_key_up(self, key):
        return key in self.key_up_list