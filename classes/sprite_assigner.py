import pygame

class Sprite_Assigner():
    def __init__(self):
        pass
    @staticmethod
    def make_sheet():
        # Load the sprite sheet image
        sprite_sheet = pygame.image.load("images/sprite_sheet.png")
        # Define the dimensions of individual sprites in the sheet
        sprite_width = 40
        sprite_height = 40
        # Define the positions of individual sprites in the sheet
        num_columns = sprite_sheet.get_width() // sprite_width
        num_rows = sprite_sheet.get_height() // sprite_height
        sprites = []
        for row in range(num_rows):
            for col in range(num_columns):
                x = col * sprite_width
                y = row * sprite_height
                sprite = sprite_sheet.subsurface(pygame.Rect(x, y, sprite_width, sprite_height))
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
# 11 = key
# 12 = cracked door
# 13 = flashlight