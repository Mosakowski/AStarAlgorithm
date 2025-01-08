from Kratka import Kratka
from Position import Position


def grid(file_path):
    with open(file_path) as file:
        file_content = file.read().replace(' ', '')
        grid = file_content.split('\n')
    return grid

def move_on_grid(grid):
    open_list = []
    closed_list = []
    kratka_startowa = Kratka(Position(0,0))
    closed_list.append(kratka_startowa)
    def check_and_add_around(kratka, open_list):
        moves = ("up", "down", "left", "right")
        for x in moves:
            match x:
                case "up":
                    kratka2 = Kratka(Position(kratka.position.x_value, kratka.position.y_value),)



def print_grid(path):
    with open(path) as file:
        file_content = file.read()
        print(file_content)

if __name__ == '__main__':
    grid = grid("grid.txt")

    move_on_grid(grid)



