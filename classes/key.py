from classes.item import Item
class Key(Item):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.key_found = False