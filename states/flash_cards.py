import pygame
from pygame.locals import *
from .base import BaseState
import random

class FlashCards(BaseState):
    def __init__(self):
        super(FlashCards, self).__init__()
        self.trivia_questions = None
        self.done = False
        self.quit = False
        self.done_once = False
        self.current_question = None
        self.index = 0
        self.text_input_font = pygame.font.Font(None, 24)
        self.answer_choices = None
        self.hovered_choice = None
        self.score = 0
        self.player_answer = None
        self.next_state = "MENU"
        
        self.screen_height = self.screen_rect[2]
        self.screen_width = self.screen_rect[3]

    def do_once(self):
        self.trivia_questions = self.persist['questions']
        random.shuffle(self.trivia_questions)
        self.done_once = True

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif self.persist['multiple_choice'] and self.current_question:
            #get mouse user input for answering questions
            if event.type == pygame.MOUSEMOTION:
                # Check if the mouse cursor is positioned over any answer choice
                for i, choice in enumerate(self.answer_choices):
                    choice_surface = self.text_input_font.render(f"{chr(65+i)}. {choice}", True, pygame.Color('white'))
                    choice_rect = pygame.Rect(
                        self.screen_width // 2 - choice_surface.get_width() // 2,
                        self.screen_height // 2 + i * 30,
                        choice_surface.get_width(),
                        choice_surface.get_height()
                    )
                    if choice_rect.collidepoint(event.pos):
                        self.hovered_choice = choice
                        break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button ==1:
                    if self.index != 3:
                        self.index += 1
                    else:
                        self.index == 0
                    if self.index == 1:
                        pass
                    if self.index == 2:    
                        if self.hovered_choice:
                            self.player_answer = self.hovered_choice
                        if self.player_answer:
                            correct_answer = self.current_question['correct_answer']
                            if self.player_answer == correct_answer:
                                self.score += 1
                            #     self.right_sound.play()
                            # else:
                            #     self.wrong_sound.play()


                        # Reset the player's answer and question
                    if self.index == 3:
                        self.player_answer = ''
                        self.current_question = None
                        self.index = 0


                
        if event.type == pygame.KEYUP:
            if event.key == K_ESCAPE:
                self.quit = True
            elif event.key == K_SPACE:
                self.done = True
            elif event.key ==K_p:
                print(self.screen_height)


    def draw(self, surface):
        surface.fill(pygame.Color("black"))
        #draw score
        score_text = f"Score: {self.score}"
        score_surface = self.text_input_font.render(score_text, True, pygame.Color('white'))
        surface.blit(score_surface, (self.screen_width // 2 - score_surface.get_width() - 10, 10))


        directions_text = "Press space to return to menu"
        directions_surface = self.text_input_font.render(directions_text, True, pygame.Color('white'))
        surface.blit(directions_surface, (self.screen_width // 2 - directions_surface.get_width()/2, self.screen_height -50))

        #if asking a question stage
        #set question
        if self.index == 0:
            if self.current_question == None:
                self.current_question = random.choice(self.trivia_questions)
        #mix em up if multiple choice
            if self.persist['multiple_choice']:    
                self.answer_choices = [self.current_question['correct_answer']] + self.current_question['wrong_answers']
                random.shuffle(self.answer_choices)

            if self.persist['multiple_choice']:                
                question_text = self.current_question['question']
                # Display the question
                question_surface = self.text_input_font.render(question_text, True, pygame.Color('white'))
                surface.blit(question_surface, (self.screen_width // 2 - question_surface.get_width() // 2, self.screen_height // 2 - 50))
                
        elif self.index == 1:
            if self.persist['multiple_choice']:                
                question_text = self.current_question['question']
                # Display the question
                question_surface = self.text_input_font.render(question_text, True, pygame.Color('white'))
                surface.blit(question_surface, (self.screen_width // 2 - question_surface.get_width() // 2, self.screen_height // 2 - 50))
                # Display the answer choices
                choice_rects=[]
                padding = 10
                for i, choice in enumerate(self.answer_choices):
                    choice_surface = self.text_input_font.render(f"{chr(65+i)}. {choice}", True, pygame.Color('white'))
                    choice_rect = pygame.Rect(
                    self.screen_width // 2 - choice_surface.get_width() // 2 - padding,
                    self.screen_height // 2 + i * 30 - padding,
                    choice_surface.get_width()+2*padding,
                    choice_surface.get_height()+2*padding
                    )
                    choice_rects.append(choice_rect)
                    if choice == self.hovered_choice:
                        pygame.draw.rect(surface, pygame.Color('darkblue'), choice_rect)  # Highlight the selected choice

                    surface.blit(choice_surface, (self.screen_width // 2 - choice_surface.get_width() // 2, self.screen_height // 2 + i * 30))

        elif self.index == 2:
            if self.persist['multiple_choice']:                
                question_text = self.current_question['question']
                # Display the question
                question_surface = self.text_input_font.render(question_text, True, pygame.Color('white'))
                surface.blit(question_surface, (self.screen_width // 2 - question_surface.get_width() // 2, self.screen_height // 2 - 50))
                # Display the answer choices
                choice_rects=[]
                for i, choice in enumerate(self.answer_choices):
                    choice_surface = self.text_input_font.render(f"{chr(65+i)}. {choice}", True, pygame.Color('white'))
                    choice_rect = pygame.Rect(
                    self.screen_width // 2 - choice_surface.get_width() // 2,
                    self.screen_height // 2 + i * 30,
                    choice_surface.get_width(),
                    choice_surface.get_height()
                    )
                    choice_rects.append(choice_rect)
                    
                    if self.player_answer == choice:
                        if choice != self.current_question['correct_answer']:
                            pygame.draw.rect(surface, pygame.Color('red'), choice_rect)
                    if choice == self.current_question['correct_answer']:
                        pygame.draw.rect(surface, pygame.Color('darkgreen'), choice_rect)  # Highlight the selected choice

                    surface.blit(choice_surface, (self.screen_width // 2 - choice_surface.get_width() // 2, self.screen_height // 2 + i * 30))




 