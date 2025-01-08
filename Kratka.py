from Position import Position


class Kratka:
    def __init__(self, Position, value=None, parent=None):
        self.position = Position
        self.value = value
        self.parent = parent

    def change_position(self, move):
        self.position = Position.change_position(self.position, move)