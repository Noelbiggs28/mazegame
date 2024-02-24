import random
class Item():
    def __init__(self):
        pass
    
    def move_item(self, valid_squares, occupied_squares):
        item_position = occupied_squares[0]
        while item_position in occupied_squares:
            item_x, item_y = random.choice(valid_squares)
            item_position = (item_x,item_y)
        occupied_squares.append(item_position)
        occupied_squares.remove((self.x, self.y))
        self.x = item_position[0]
        self.y = item_position[1]
        return occupied_squares
    