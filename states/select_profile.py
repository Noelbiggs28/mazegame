import pygame
from .base import BaseState
from classes.search_for_csv import Display_csv
from classes.player_loader_saver import Player_Data


class Select_Profile(BaseState):
    def __init__(self):
        super(Select_Profile, self).__init__()
        self.next_state = "MENU"
        self.display_csv = Display_csv()   

    def handle_action(self, csv_file):
        profile_data = Player_Data.load_player_stats(csv_file)
        self.persist['profile'] = profile_data
        self.persist['profile'][0]['path'] = csv_file

    def draw(self, surface):
        surface.fill(pygame.Color("black"))


        # Display the prompt
        prompt_text = self.font.render("Select your profile:", True, pygame.Color("white"))
        prompt_rect = prompt_text.get_rect(center=(self.screen_rect.centerx, 150))
        surface.blit(prompt_text, prompt_rect)

        # Display the CSV file options
        # grabs all csv files from profile folder
        csv_file = self.display_csv.display_csv_options('profiles', surface, self.font)

        # save profile info and path to persistant data for updating throughout game
        if csv_file:
            self.handle_action(csv_file)
        
        surface.fill(pygame.Color("black"))
        # Display the prompt
        prompt_text = self.font.render("Select questions file:", True, pygame.Color("white"))
        prompt_rect = prompt_text.get_rect(center=(self.screen_rect.centerx, self.screen_rect.centery - 250))
        surface.blit(prompt_text, prompt_rect)

        # Display the CSV file options from questions folder
        question_csv_file = self.display_csv.display_csv_options('questions', surface, self.font)

        # sets questions in persistant data equal to questions
        self.persist['questions_path'] = question_csv_file
        

        self.done = True
