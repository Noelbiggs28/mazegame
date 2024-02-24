from classes.item import Item

class Flashlight(Item):
    def __init__(self):
        super().__init__()
        self.x = None
        self.y = None
        self.has_flashlight = False
        

