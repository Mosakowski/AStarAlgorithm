from Kratka import Kratka
from Position import Position
import math
import tkinter as tk
import time


def grid(file_path):
    with open(file_path) as file:
        file_content = file.read().replace(' ', '')
        grid = file_content.split('\n')
        grid.reverse()
    return grid

def move_on_grid(grid, start, cel):
    row_length = len(grid[0][:])
    column_length = len(grid[:][0])
    open_list = []
    closed_list = []
    objective_kratka = Kratka(cel)
    kratka_startowa = Kratka(start)
    closed_list.append(kratka_startowa)
    for element in closed_list:
        add_to_open_list(element, objective_kratka, open_list, row_length, column_length, closed_list)
        if not open_list:
            return 0
        lowest_kratka = open_list[0]
        # iterowanie po liscie otwartej w celu znalezienia obiektu z najmniejszą wartością
        for i in open_list:
            if lowest_kratka.value > i.value:
                lowest_kratka = i
            # spośród obiektów o tej samej wartości wybieramy ten dodany później
            if lowest_kratka.value == i.value:
                if i.id > lowest_kratka.id:
                    lowest_kratka = i
        closed_list.append(lowest_kratka)

        #print(lowest_kratka)
        open_list.remove(lowest_kratka)
        if objective_kratka.position.x_value == lowest_kratka.position.x_value and objective_kratka.position.y_value == lowest_kratka.position.y_value:

            return closed_list

def add_to_open_list(kratka_current, objective_kratka, open_list, row_length, column_length, closed_list):
    moves = ("up", "down", "left", "right")
    kratka_x_value = kratka_current.position.x_value
    kratka_y_value = kratka_current.position.y_value

    for move in moves:
        match move:
            case "up":
                new_kratka_value = calculate_value(objective_kratka, kratka_x_value, kratka_y_value + 1, kratka_current)
                kratkaup = Kratka(Position(kratka_x_value, kratka_y_value + 1), new_kratka_value, kratka_current)
                if is_possible(kratkaup, row_length, column_length):
                    if is_avalaible(kratkaup, closed_list):
                        isin = 0
                        for e in open_list:
                            if e.position.y_value == kratkaup.position.y_value and e.position.x_value == kratkaup.position.x_value:
                                if new_kratka_value < e.value:
                                    open_list.remove(e)
                                    open_list.append(kratkaup)
                                    isin += 1
                                    break
                                else:
                                    isin =+ 1
                        if isin == 0:
                            open_list.append(kratkaup)


            case "down":
                new_kratka_value = calculate_value(objective_kratka, kratka_x_value, kratka_y_value - 1, kratka_current)
                kratkadown = Kratka(Position(kratka_x_value, kratka_y_value - 1), new_kratka_value, kratka_current)
                if is_possible(kratkadown, row_length, column_length):
                    if is_avalaible(kratkadown, closed_list):
                        isin = 0
                        for e in open_list:
                            if e.position.y_value == kratkadown.position.y_value and e.position.x_value == kratkadown.position.x_value:
                                if new_kratka_value < e.value:
                                    open_list.remove(e)
                                    open_list.append(kratkadown)
                                    isin += 1
                                    break
                                else:
                                    isin =+ 1
                        if isin == 0:
                            open_list.append(kratkadown)

            case "left":
                new_kratka_value = calculate_value(objective_kratka, kratka_x_value - 1, kratka_y_value, kratka_current)
                kratkaleft = Kratka(Position(kratka_x_value - 1, kratka_y_value), new_kratka_value, kratka_current)
                if is_possible(kratkaleft, row_length, column_length):
                    if is_avalaible(kratkaleft, closed_list):
                        isin = 0
                        for e in open_list:
                            if e.position.y_value == kratkaleft.position.y_value and e.position.x_value == kratkaleft.position.x_value:
                                if new_kratka_value < e.value:
                                    open_list.remove(e)
                                    open_list.append(kratkaleft)
                                    isin+=1
                                    break
                                else:
                                    isin =+ 1
                        if isin == 0:
                            open_list.append(kratkaleft)


            case "right":
                new_kratka_value = calculate_value(objective_kratka, kratka_x_value + 1, kratka_y_value, kratka_current)
                kratkaright = Kratka(Position(kratka_x_value + 1, kratka_y_value), new_kratka_value, kratka_current)
                if is_possible(kratkaright, row_length, column_length):
                    if is_avalaible(kratkaright, closed_list):
                        isin = 0
                        for e in open_list:
                            if e.position.y_value == kratkaright.position.y_value and e.position.x_value == kratkaright.position.x_value:
                                if new_kratka_value < e.value:
                                    open_list.remove(e)
                                    open_list.append(kratkaright)
                                    isin +=1
                                    break
                                else:
                                    isin =+ 1
                        if isin == 0:
                            open_list.append(kratkaright)
    return open_list


def is_avalaible(kratka, closed_list):
    for i in closed_list:
        if kratka.position.x_value == i.position.x_value and kratka.position.y_value == i.position.y_value:
            return 0
    return 1

def is_it_in_stepbro(closed_list, objective_kratka):
    for i in closed_list:
        if objective_kratka.position.x_value == i.position.x_value and objective_kratka.position.y_value == i.position.y_value:
            return 1
    return 0

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

def print_list_lepiej(list):
    for o in list:
        print(o)

def calculate_value(objective_kratka, x_value, y_value, current_kratka):
    h = math.sqrt((pow(x_value - objective_kratka.position.x_value, 2))
                  + pow(y_value - objective_kratka.position.y_value, 2))
    h = float(h + current_kratka.number_of_parents + 1)
    return h

def koncowka(grid, start, cel):
    lista = move_on_grid(grid, start, cel)
    if not lista:
        return 0

    lastListItem = lista[len(lista)-1]
    droga = []

    def getParent(kratka, droga):
        droga.append(kratka)
        if(kratka.parent!=None):
            getParent(kratka.parent, droga)
        else:
            return droga

    getParent(lastListItem, droga)
    print("najkrótsza ścieżka: ")
    print_list_lepiej(droga)

    # Wyświetlenie wizualizacji na koniec
    display_grid(grid, start, cel, droga)

    return 0


def display_grid(grid, start, cel, path=None):
    root = tk.Tk()
    root.title("Algorytm A*")

    cell_size = 30
    canvas = tk.Canvas(root, width=len(grid[0]) * cell_size, height=len(grid) * cell_size)
    canvas.pack()

    def draw_cell(x, y, color):
        canvas.create_rectangle(x * cell_size, y * cell_size, (x + 1) * cell_size, (y + 1) * cell_size, fill=color)

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '5':
                draw_cell(x, y, 'black')
            else:
                draw_cell(x, y, 'white')


    if path:
        for node in path:
            draw_cell(node.position.x_value, node.position.y_value, 'blue')


    starter = start
    goal = cel

    draw_cell(starter.x_value, starter.y_value, 'green')
    draw_cell(goal.x_value, goal.y_value, 'red')

    root.mainloop()


if __name__ == '__main__':
    grid_path = "C:/Users/kubam/szkoła/ElementyRobotyki/grid.txt"
    grid = grid(grid_path)
    start_x = int(input("podaj współrzędną x dla kratki startowej (int): "))
    start_y = int(input("podaj współrzędną y dla kratki startowej (int): "))
    cel_x = int(input("podaj współrzędną x dla kratki końcowej (int): "))
    cel_y = int(input("podaj współrzędną y dla kratki końcowej (int): "))
    cel = Position(cel_x,cel_y)
    start = Position(start_x,start_y)
    koncowka(grid, start, cel)


