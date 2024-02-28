import pygame
from classes.sprite_assigner import Sprite_Assigner

class BaseState(Sprite_Assigner):
    def __init__(self):
        super(BaseState, self).__init__()
        self.done = False
        self.quit = False
        self.next_state = None
        self.screen_rect = pygame.display.get_surface().get_rect()
        self.persist = {}
        self.font = pygame.font.Font(None, 24)
        self.done_once = False
        

    def startup(self, persistent):
        self.persist = persistent 

    def do_once(self):
        pass

    def get_event(self, event):
        pass

    def update(self, dt):
        pass

    def draw(self, surface):
        pass