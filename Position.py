class Position:
    def __init__(self, x_value, y_value):
        self.x_value = x_value
        self.y_value = y_value

    def change_position(self, move):
        match move:
            case "up":
                self.y_value = self.y_value + 1
                return self.y_value
            case "down":
                self.y_value = self.y_value - 1
                return self.y_value
            case "left":
                self.x_value = self.x_value - 1
                return self.x_value
            case "right":
                self.x_value = self.x_value + 1
                return self.x_value
