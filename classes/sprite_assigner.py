import pygame

class Sprite_Assinger():
    def __init__(self):
    # Load the sprite sheet image
        self.sprite_sheet = pygame.image.load("images/sprite_sheet.png")
        # Define the dimensions of individual sprites in the sheet
        self.sprite_width = 40
        self.sprite_height = 40
        # Define the positions of individual sprites in the sheet
        self.num_columns = self.sprite_sheet.get_width() // self.sprite_width
        self.num_rows = self.sprite_sheet.get_height() // self.sprite_height

    def make_sheet(self):
        sprites = []
        for row in range(self.num_rows):
            for col in range(self.num_columns):
                x = col * self.sprite_width
                y = row * self.sprite_height
                sprite = self.sprite_sheet.subsurface(pygame.Rect(x, y, self.sprite_width, self.sprite_height))
                sprites.append(sprite)
        return sprites



# 0 = player facing left
# 1 = player facing right
# 2 = player facing back
# 3 = player facing forward
# 4 = victory ProcessLookupError
# 5 = darkness
# 6 = dirt
# 7 = gate 
# 8 = wall
# 9 = door
# 10 = heart