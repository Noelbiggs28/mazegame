import pygame
from classes.sprite_assigner import Sprite_Assigner
class Player(Sprite_Assigner):
    def __init__(self, x, y, maze):
        super(Player, self).__init__()
        self.x = x
        self.y = y
        self.cell_size = 40
        self.maze = maze
        self.wall_hit_sound = pygame.mixer.Sound("images/wall_hit.wav")
        self.player_image = self.player_right
        self.has_key = False
        self.has_flashlight = False
        self.walkable_squares = [6,7,12]
        self.sight = 4
        self.step_counter = 1

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy
# check if square your trying to go to is in maze perimeter and not a wall and sets self xy there
        if 0 <= new_x < 20 and 0 <= new_y < 20 and self.maze[new_y][new_x] in self.walkable_squares:
            self.x = new_x
            self.y = new_y
            #shift image based on direction
        else:
            self.wall_hit_sound.play()
        if dx > 0:
            self.player_image = self.player_right
        elif dx < 0:
            self.player_image = self.player_left
        elif dy < 0:
            self.player_image = self.player_up
        elif dy > 0:
            self.player_image = self.player_down
        self.step_counter +=1
            
# draws player
    def draw(self, surface):
        if self.x >= 0 and self.y >= 0:

            surface.blit(self.player_image, (self.x * self.cell_size, self.y * self.cell_size))