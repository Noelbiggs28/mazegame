
import pygame
from .base import BaseState
from classes.load_questions import Trivia
from classes.player_loader_saver import Player_Data

class Menu(BaseState):
    def __init__(self):
        super(Menu, self).__init__()
        self.active_index = 0
        self.options = ["Start Game", "Flash Cards", "Settings", "Save Game", "Quit Game"]
        self.next_state = "GAMEPLAY"

    def render_text(self, index):
        color = pygame.Color("white")
        return self.font.render(self.options[index], True, color)

    def get_text_position(self, text, index):
        center = (self.screen_rect.centerx, self.screen_rect.centery + (index * 50))
        return text.get_rect(center=center)

    def handle_action(self, index):
        # if start game is selected, set next state to game. load questions selected before and end menu state.
        if index == 0:
            self.next_state = "GAMEPLAY"
            path = self.persist['questions_path']
            if self.persist['multiple_choice']:
                question_list = Trivia.load_multiple_questions(path)
            else:
                question_list = Trivia.load_solo_questions(path)
            self.persist['questions'] = question_list
            self.done = True
        # if flashcards is selected, set next state to flashcards. load questions selected before and end menu state.
        elif index ==1:
            self.next_state = "FLASH_CARDS"
            path = self.persist['questions_path']
            if self.persist['multiple_choice']:
                question_list = Trivia.load_multiple_questions(path)
            else:
                question_list = Trivia.load_solo_questions(path)
            self.persist['questions'] = question_list
            self.done = True
        # if settings is selected set next state to settings and end menu state
        elif index == 2:
            self.next_state = "SETTINGS"
            self.done = True
        # if save game is selected. save player info to csv
        elif index == 3:
            Player_Data.save_player_stats(self.persist['profile'][0]['path'] ,self.persist['profile'])
        # quis game
        elif index == 4:
            self.quit = True

    def handle_click(self, mouse_pos):
        for index, option in enumerate(self.options):
            text_position = self.get_text_position(self.render_text(index), index)
            if text_position.collidepoint(mouse_pos):
                self.handle_action(index)
                break

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYUP:
            # testing exp
            if event.key == pygame.K_a:
                print(self.persist['profile'][0])
            elif event.key == pygame.K_z:
                self.persist['profile'][0]['exp'] = Player_Data.change_num_stat(self.persist['profile'][0],'exp',1)
        elif event.type == pygame.MOUSEBUTTONUP:
            self.handle_click(pygame.mouse.get_pos())

    def draw(self, surface):
        surface.fill(pygame.Color("black"))
        for index, option in enumerate(self.options):
            text_render = self.render_text(index)
            text_position = self.get_text_position(text_render, index)

            if text_position.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(surface, pygame.Color("red"), text_position)
            else:
                pygame.draw.rect(surface, pygame.Color("black"), text_position)

            surface.blit(text_render, text_position)
