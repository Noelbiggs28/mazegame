from classes.item import Item

class Flashlight(Item):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.has_flashlight = False

