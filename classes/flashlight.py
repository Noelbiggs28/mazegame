from classes.item import Item

class Flashlight(Item):
    def __init__(self, valid_squares, occupied_squares):
        super().__init__()
        self.x = None
        self.y = None
        self.has_flashlight = False
        self.create_item(valid_squares, occupied_squares)

