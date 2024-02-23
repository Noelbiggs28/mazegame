import pygame
from .base import BaseState
from classes.high_scores import High_Scores


class Splash(BaseState):
    def __init__(self):
        super(Splash, self).__init__()
        self.title = self.font.render("Maze Game", True, pygame.Color("blue"))
        self.title_rect = self.title.get_rect(center=self.screen_rect.center)
        self.author = self.font.render("By Noel Biggs", True, pygame.Color("blue"))
        self.author_rect = self.title.get_rect(center=(self.screen_rect.centerx -12, self.screen_rect.centery + 50))
        # sets next state to menu
        self.next_state = "SELECT_PROFILE"
        self.time_active = 0
        high_scores_list = High_Scores()
        high_scores_list.load_high_scores('high_scores.txt')
        # set default options
        self.persist = {'multiple_choice': True, 'sound': True, 'high_scores': high_scores_list.high_scores}

    def update(self, dt):
        # updates clock every dt 
        self.time_active += dt
        # >= 1 second
        if self.time_active >= 1000:
            # if self.done == True game=>update=>flipstate
            self.done = True

    def draw(self, surface):
        surface.fill(pygame.Color("black"))
        surface.blit(self.title, self.title_rect)
        surface.blit(self.author, self.author_rect)
