import pygame
import random
from pygame.locals import *
from .base import BaseState
from classes.generate_maze import Maze_Generator
from classes.player import Player

from classes.player_loader_saver import Player_Data
from classes.key import Key
from classes.flashlight import Flashlight
class Gameplay(BaseState):
    def __init__(self):
        super(Gameplay, self).__init__()
        # set variables
        
        self.maze_height = 20
        self.maze_width = 20
        self.cell_size = 40
        self.score = 0
        self.health = 3
        self.map_cypher = {5:self.dark_image,6:self.dirt_image,7:self.exit_image,8:self.wall_image,9:self.door_image,12:self.cracked_door_image}
        # load sounds
        self.wrong_sound = pygame.mixer.Sound("images/wrong.wav")
        self.right_sound = pygame.mixer.Sound("images/right.wav")
        # select next state
        self.next_state = "GAME_OVER"
    
        # make maze and set exit
        self.maze_and_exit = Maze_Generator.generate_maze()
        self.occupied_cells = [(self.maze_and_exit[1][0],self.maze_and_exit[1][1])]
       
        #pick player position
        self.valid_cells = [(x, y) for y in range(self.maze_height) for x in range(self.maze_width) if self.maze_and_exit[0][y][x] == 6]
        player_x, player_y = random.choice(self.valid_cells)
        self.occupied_cells.append((player_x,player_y))
        self.key = Key()
        self.occupied_cells = self.key.place_item(self.valid_cells, self.occupied_cells)
        self.flashlight = Flashlight()
        self.occupied_cells = self.flashlight.place_item(self.valid_cells, self.occupied_cells)
        # create player
        self.player = Player(player_x, player_y, self.maze_and_exit[0])

        #do things once on startup
        self.done_once = False
        # setup questions
        self.trivia_frequency = 25
        self.current_question = None
        self.player_answer = ''
        self.hovered_choice = None
        self.text_input_rect = pygame.Rect(300, 400, 200, 30)
        self.text_input_active = False
        self.mouse_input_active = False
        self.trivia_questions = None
        self.text_input_font = pygame.font.Font(None, 24)
        self.answer_choices = None
        self.choice = None

    # do things once 
    def do_once(self):
        # puts profile selected stats into player
        self.player.profile = self.persist['profile']
        self.player.update_player_with_profile()
        # if sound is checked in option play sounds and music
        if self.persist['sound']:
            pygame.mixer.music.load("images/maze_music.wav") 
            pygame.mixer.music.set_volume(0.1) #make it quieter
            pygame.mixer.music.play(-1) 
            pygame.mixer.set_num_channels(1)
        # if unchecked no sound
        else: 
            pygame.mixer.set_num_channels(0)
        # take questions in from persistant data
        self.trivia_questions = self.persist['questions']
        self.done_once = True

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True

        #get mouse user input for answering multiple choice questions
        elif self.persist['multiple_choice'] and self.current_question:
            if event.type == pygame.MOUSEMOTION:
                # Check if the mouse cursor is positioned over any answer choice
                for i, choice in enumerate(self.answer_choices):
                    choice_surface = self.text_input_font.render(f"{chr(65+i)}. {choice}", True, pygame.Color('white'))
                    choice_rect = pygame.Rect(
                        self.screen_rect.width // 2 - choice_surface.get_width() // 2,
                        self.screen_rect.height// 2 + i * 30,
                        choice_surface.get_width(),
                        choice_surface.get_height()
                    )
                    if choice_rect.collidepoint(event.pos):
                        self.hovered_choice = choice
                        break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.hovered_choice:
                        self.player_answer = self.hovered_choice
                        if self.player_answer:
                            correct_answer = self.current_question['correct_answer']
                            if self.player_answer == correct_answer:
                                self.score += 1
                                self.right_sound.play()
                            else:
                                self.health -= 1
                                self.wrong_sound.play()
                                if self.health == 0:
                                    pygame.mixer.music.stop()
                                    self.done = True

                            self.player.step_counter += 1
                        # Reset the player's answer and question
                        self.player_answer = ''
                        self.current_question = None
                        self.mouse_input_active = False
                        # break 



        elif event.type == pygame.KEYUP:
            if event.key == K_ESCAPE:
                self.quit = True
            # gets answers for single choice questions
            elif event.key == K_RETURN: #submits answer
                if self.text_input_active:
                    # Check if the player has answered the question and process the answer
                    if self.current_question and self.player_answer:
                        correct_answer = self.current_question['answer']
                        if self.player_answer.lower() == correct_answer.lower():
                            self.score +=1
                            self.right_sound.play()
                        else:
                            self.health -= 1
                            self.wrong_sound.play()
                            if self.health == 0:
                                pygame.mixer.music.stop()
                                self.done = True
                        self.player.step_counter += 1
                    # Reset the player's answer and question
                        self.player_answer = ''
                        self.current_question = None
                        self.text_input_active = False

            elif self.text_input_active: #deletes letter
                if event.key == K_BACKSPACE:
                    self.player_answer = self.player_answer[:-1]
                else:
                    # Add the pressed character to the player's answer
                    self.player_answer += event.unicode
            # players movement
            elif event.key == K_UP or event.key == K_w:
                self.player.move(0, -1)
            elif event.key == K_DOWN or event.key == K_s:
                self.player.move(0, 1)
            elif event.key == K_LEFT or event.key == K_a:
                self.player.move(-1, 0)
            elif event.key == K_RIGHT or event.key == K_d:
                self.player.move(1, 0)
            elif event.key ==K_p:
                print(self.player.profile)
            # print persist for testing
            elif event.key == K_p:
                print(self.maze_and_exit)

        # if player lands on the key. make the square that had doors be able to be walked on
        if self.player.x == self.key.x and self.player.y == self.key.y:
            self.player.has_key = True
            # changes shut door to cracked door
            doors = self.maze_and_exit[2]
            self.maze_and_exit[0][doors[0][0]][doors[0][1]] = 12
            self.maze_and_exit[0][doors[1][0]][doors[1][1]] = 12

        # if player lands on flashlight
        if self.player.x == self.flashlight.x and self.player.y == self.flashlight.y:
            self.player.sight += 1
            self.occupied_cells = self.flashlight.move_item(self.valid_cells, self.occupied_cells)

        # if player has reached the exit
        if self.player.x == self.maze_and_exit[1][0] and self.player.y == self.maze_and_exit[1][1]:
            #updates and saves exp
            self.persist['profile'][0]['exp'] = Player_Data.change_num_stat(self.persist['profile'][0],'exp',1)
            level = self.player.get_level()
            self.persist['profile'][0]['level'] = level
            Player_Data.save_player_stats(self.persist['profile'][0]['path'] ,self.persist['profile'])
            pygame.mixer.music.stop()
            # changes next state to high schore state if you made it to the top 5
            if (len(self.persist['high_scores']) < 5 or self.score > self.persist['high_scores'][-1][1]):
                self.next_state = "Add_High_Score"
            self.persist['score'] = self.score
            self.done = True

    def draw(self, surface):
        #draw maze
        for y in range(self.maze_height):
            for x in range(self.maze_width):
                #checks squares around player in 3x3 grid or sight distance
                if abs(x - self.player.x) <= self.player.sight and abs(y - self.player.y) <= self.player.sight: 
                    #draws maze in the sight grid
           
                    surface.blit(self.map_cypher[self.maze_and_exit[0][y][x]], (x * self.cell_size, y * self.cell_size)) 
                #print darkness if not in sight
                else:
                    surface.blit(self.dark_image, (x * self.cell_size, y * self.cell_size))

        #draw player
        self.player.draw(surface)

        # draw flashlight
        self.flashlight.draw_if_in_sight(self.player, surface, self.flashlight_image)

        #draws key if in sight and not already taken
        if self.player.has_key == False:
            self.key.draw_if_in_sight(self.player, surface, self.key_image)

        # draw key on top if obtained
        if self.player.has_key:
            key_rect = pygame.Rect(self.screen_rect.width - 250, 10, 40, 40)
            surface.blit(self.key_image, key_rect)

        # Mark the exit as gate
        surface.blit(self.exit_image, (self.maze_and_exit[1][0] * self.cell_size, self.maze_and_exit[1][1] * self.cell_size))

        #draw health screen width/ heart width/ hearts/ doesnt block exit
        heart_x = self.screen_rect.width - (50) * 3 - 40
        for _ in range(self.health):
            heart_rect = pygame.Rect(heart_x, 10, 40, 40)
            surface.blit(self.heart_image, heart_rect)
            heart_x += 50    
        score_font = pygame.font.Font(None, 24)

        # draw score
        score_text = f"Score: {self.score}"
        score_surface = score_font.render(score_text, True, pygame.Color('white'))
        surface.blit(score_surface, (self.screen_rect.width // 2 - score_surface.get_width() - 10, 10))

        # Check if it's time to ask a trivia question
        if self.player.step_counter % self.trivia_frequency == 0 and not self.text_input_active and not self.mouse_input_active:
            self.current_question = random.choice(self.trivia_questions)
            if self.persist['multiple_choice']:
                self.mouse_input_active = True
            else:
                self.text_input_active = True
            
#mc          # Shuffle the answer choices only once when a new question is presented
            if self.persist['multiple_choice']:    
                self.answer_choices = [self.current_question['correct_answer']] + self.current_question['wrong_answers']
                random.shuffle(self.answer_choices)

#mc        # draw multiple choice qustions
        if self.persist['multiple_choice']:
            if self.current_question:
                question_text = self.current_question['question']


                # Display the question
                question_surface = self.text_input_font.render(question_text, True, pygame.Color('white'))
                surface.blit(question_surface, (self.screen_rect.width // 2 - question_surface.get_width() // 2, self.screen_rect.height // 2 - 50))

                # Display the answer choices
                choice_rects=[]
                for i, choice in enumerate(self.answer_choices):
                    choice_surface = self.text_input_font.render(f"{chr(65+i)}. {choice}", True, pygame.Color('white'))
                    choice_rect = pygame.Rect(
                    self.screen_rect.width // 2 - choice_surface.get_width() // 2,
                    self.screen_rect.height // 2 + i * 30,
                    choice_surface.get_width(),
                    choice_surface.get_height()
                    )
                    choice_rects.append(choice_rect)
                    if choice == self.hovered_choice:
                        pygame.draw.rect(surface, pygame.Color('darkgreen'), choice_rect)  # Highlight the selected choice

                    surface.blit(choice_surface, (self.screen_rect.width // 2 - choice_surface.get_width() // 2, self.screen_rect.height // 2 + i * 30))
        
#sc     # # Draw the trivia question on the SCREEN
        if self.persist['multiple_choice'] == False:
            if self.current_question:
                question_text = self.current_question['question']
                question_surface = self.text_input_font.render(question_text, True, pygame.Color('white'))
                surface.blit(question_surface, (self.screen_rect.width // 2 - question_surface.get_width() // 2, self.screen_rect.height // 2 - 50))

                # Draw the player's answer text input box
                pygame.draw.rect(surface, pygame.Color('white'), self.text_input_rect, 2)
                text_surface = self.text_input_font.render(self.player_answer, True, pygame.Color('white'))
                surface.blit(text_surface, (self.text_input_rect.x + 5, self.text_input_rect.y + 5))