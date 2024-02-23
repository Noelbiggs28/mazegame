import sys
import pygame
from states.menu import Menu
from states.gameplay import Gameplay
from states.game_over import GameOver
from states.splash import Splash
from states.settings import Settings
from states.add_high_score import Add_High_Score
from states.select_profile import Select_Profile
from game import Game
from states.flash_cards import FlashCards


pygame.init()
# set screen dimensions
screen = pygame.display.set_mode((800, 800))
# all states go here to pass into game
states = {
    "MENU": Menu(),
    "SPLASH": Splash(),
    "SELECT_PROFILE": Select_Profile(),
    "SETTINGS": Settings(),
    "GAMEPLAY": Gameplay(),
    "GAME_OVER": GameOver(),
    "Add_High_Score": Add_High_Score(),
    "FLASH_CARDS":FlashCards()
    
}

# create game object with(dimensions/all states/starting state)
game = Game(screen, states, "SPLASH")
# run game
game.run()

pygame.quit()
sys.exit()
