from Kratka import Kratka
from Position import Position
import math


def grid(file_path):
    with open(file_path) as file:
        file_content = file.read().replace(' ', '')
        grid = file_content.split('\n')
        grid.reverse()
    return grid

def move_on_grid(grid):
    row_length = len(grid[0][:])
    column_length = len(grid[:][0])
    open_list = []
    closed_list = []
    objective_kratka = Kratka(Position(19,19))
    kratka_startowa = Kratka(Position(0,3))
    closed_list.append(kratka_startowa)
    for element in closed_list:
        add_to_open_list(element, objective_kratka, open_list, row_length, column_length)
        print_list(open_list)
        lowest_kratka = open_list[0]
        for i in open_list:
            if lowest_kratka.value <= i.value:
                lowest_kratka = i
            if lowest_kratka.value == i.value:
                if i.id < lowest_kratka.id:
                    lowest_kratka = i
        closed_list.append(i)

def add_to_open_list(kratka_current, objective_kratka, open_list, row_length, column_length):
    moves = ("up", "down", "left", "right")
    kratka_x_value = kratka_current.position.x_value
    kratka_y_value = kratka_current.position.y_value
    for move in moves:
        match move:
            case "up":
                kratkaup = Kratka(Position(kratka_x_value, kratka_y_value + 1),
                                  calculate_value(objective_kratka, kratka_x_value, kratka_y_value, kratka_current), kratka_current)
                # print(kratkaup," dla up")
                if kratkaup.x_value
                if is_possible(kratkaup,row_length, column_length): open_list.append(kratkaup)
            case "down":
                kratkaup = Kratka(Position(kratka_x_value, kratka_y_value - 1), calculate_value(objective_kratka, kratka_x_value, kratka_y_value, kratka_current), kratka_current)
                # print(kratkaup, " dla down")
                if is_possible(kratkaup,row_length, column_length): open_list.append(kratkaup)
            case "left":
                kratkaup = Kratka(Position(kratka_x_value - 1, kratka_y_value), calculate_value(objective_kratka, kratka_x_value, kratka_y_value, kratka_current), kratka_current)
                # print(kratkaup, " dla left")
                if is_possible(kratkaup,row_length, column_length): open_list.append(kratkaup)
            case "right":
                kratkaup = Kratka(Position(kratka_x_value + 1, kratka_y_value), calculate_value(objective_kratka, kratka_x_value, kratka_y_value, kratka_current), kratka_current)
                # print(kratkaup, " dla right")
                if is_possible(kratkaup,row_length, column_length): open_list.append(kratkaup)
    return open_list




def is_possible(kratka_temp, row_length, column_length):
    if (row_length > kratka_temp.position.x_value >= 0) and (column_length > kratka_temp.position.y_value >= 0):
        if int(grid[kratka_temp.position.y_value][kratka_temp.position.x_value]) != 5: return 1
        return 0
    return 0

def acces_kratka(kratka_name, list):
    for kratka in list:
        if kratka.name == kratka_name:
            return kratka

def print_grid(path):
    with open(path) as file:
        file_content = file.read()
        print(file_content)

def print_list(list):
    for o in list:
        print(o)

def calculate_value(objective_kratka, x_value, y_value, current_kratka):
    h = math.sqrt((pow(x_value - objective_kratka.position.x_value, 2))
                  + pow(y_value - objective_kratka.position.y_value, 2))
    h = int(h + current_kratka.number_of_parents)
    return h

if __name__ == '__main__':
    grid_path = "C:/Users/kubam/szkoła/ElementyRobotyki/grid.txt"
    grid = grid(grid_path)

    move_on_grid(grid)

    print_grid(grid_path)



