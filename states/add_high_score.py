import pygame
from .base import BaseState
from classes.high_scores import High_Scores

class Add_High_Score(BaseState):
    def __init__(self):
        super(Add_High_Score, self).__init__()
        # congrats words
        self.title = self.font.render("Congrats", True, pygame.Color("white"))
        title_center = (self.screen_rect.center[0], self.screen_rect.center[1] - 100)
        self.title_rect = self.title.get_rect(center=title_center)
        self.instructions = self.font.render("Press space to start again, or enter to go to the menu", True, pygame.Color("white"))
        instructions_center = (self.screen_rect.center[0], self.screen_rect.center[1] -  50)
        self.instructions_rect = self.instructions.get_rect(center=instructions_center)
        #add high score words
        self.add_score = self.font.render("Enter name and press enter", True, pygame.Color("white"))
        self.add_score_rect = self.add_score.get_rect(center=instructions_center)
        self.text_input_rect = pygame.Rect(300, 400, 200, 30)  # Define the text input box
        self.text_input_active = True
        self.player_name =''
        self.high_scores = ''
        
    def do_once(self):
        if self.done_once == False:
            self.high_scores = self.persist['high_scores']
            self.done_once = True

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYUP:
            if self.text_input_active:
                if event.key == pygame.K_RETURN:
                    high_scores_class = High_Scores()
                    self.high_scores.append((self.player_name, self.persist['score'])) 
                    self.high_scores.sort(key=lambda x: x[1], reverse=True)
                    self.high_scores = self.high_scores[:5]
                    high_scores_class.save_high_scores('high_scores.txt',self.high_scores)
                    self.text_input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    self.player_name = self.player_name[:-1]
                else:
                    self.player_name += event.unicode
            elif event.key == pygame.K_RETURN:
                self.next_state = "MENU"
                self.text_input_active = True
                self.done = True
            elif event.key == pygame.K_SPACE:
                self.next_state = "GAMEPLAY"
                self.text_input_active = True
                self.done = True
            elif event.key == pygame.K_ESCAPE:
                self.quit = True

    def draw(self, surface):
        surface.fill(pygame.Color("black"))
        if self.text_input_active:
            # Draw the text input box
            pygame.draw.rect(surface, pygame.Color("white"), self.text_input_rect, 2)
            # Render and display the player name inside the text input box
            player_name_text = self.font.render(self.player_name, True, pygame.Color("white"))
            surface.blit(player_name_text, self.text_input_rect.move(5, 5))
            surface.blit(self.add_score, self.add_score_rect)
        else:
            surface.blit(self.title, self.title_rect)
            surface.blit(self.instructions, self.instructions_rect)

