from classes.item import Item
class Key(Item):
    def __init__(self):
        super().__init__()
        self.x = None
        self.y = None
        self.key_found = False
        