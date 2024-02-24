from classes.item import Item
class Key(Item):
    def __init__(self, valid_squares, occupied_squares):
        super().__init__()
        self.x = None
        self.y = None
        self.key_found = False
        self.create_item(valid_squares, occupied_squares)