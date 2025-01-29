from Position import Position


class Kratka:
    instance_counter = 0

    def __init__(self,Position, value=None, parent=None):
        self.position = Position
        self.value = value
        self.parent = parent
        self.name = "kratka" + str(self.position.x_value) + str(self.position.y_value)
        self.number_of_parents = parent.number_of_parents + 1 if parent else 0
        self.id = Kratka.instance_counter
        Kratka.instance_counter += 1

    def set_value(self, h):
        self.value = h

    def change_position(self, move):
        self.position = Position.change_position(self.position, move)

    def __str__(self):
        #return f"Kratka(name={self.name}, position=({self.position.x_value}, {self.position.y_value}), parent={self.parent}, value={self.value}, id={self.id})"
        return f"Kratka(position=({self.position.x_value}, {self.position.y_value}))"