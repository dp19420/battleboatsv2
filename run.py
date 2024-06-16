from random import randint

target_grid = [[' '] * 10 for x in range(10)]

aim_grid = [[' '] * 10 for x in range(10)]


# Creates the 10 by 10 grid
def print_grid(grid):
    print('  1 2 3 4 5 6 7 8 9 10')
    print('  --------------------')
    row_num = 1
    for row in grid:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num += 1


# CPU opponent random place 7 ships on grid
def place_ships(grid):
    for ship in range(7):
        ship_row, ship_column = randint(0, 9), randint(0, 9)
        while grid[ship_row][ship_column] == 'X':
            ship_row, ship_location = randint(0, 9), randint(0, 9)
        grid[ship_row][ship_column] = 'X'


# register location fired upon
def place_shot():
    row = input("Enter a Number 1-10 for the vertical coordinate:\n")
    while not (row.isdigit() and (1 <= int(row) <= 10)):
        print("Invalid input. Please enter a number between 1 and 10.")
        row = input("Enter a Number 1-10 for the vertical coordinate:\n")
    column = input("Enter a Number 1-10 for the horizontal coordinate:\n")
    while not (column.isdigit() and (1 <= int(column) <= 10)):
        print("Invalid input. Please enter a number between 1 and 10.")
        column = input("Enter a Number 1-10 for the horizontal coordinate:\n")
    return int(row) - 1, int(column) - 1


# counter for hit ships
def sunk_ships(grid):
    sunk = 0
    for row in grid:
        for column in row:
            if column == 'X':
                sunk += 1
    return sunk


# Runs the Game
place_ships(target_grid)
turns = 15
while turns > 0:
    print_grid(aim_grid)
    row, column = place_shot()
    if aim_grid[row][column] == '-':
        print('This location has already been targeted, try again!')
    elif target_grid[row][column] == 'X':
        print('Perfect hit!')
        aim_grid[row][column] = 'X'
        turns -= 1
    else:
        print('Damn! Missed!')
        aim_grid[row][column] = '-'
        turns -= 1

    if sunk_ships(aim_grid) == 7:
        print('All their ships are belong to the sea, we are belong!')
        break

    print(f"There are only {turns} rounds left to sink the bastards!")
    if turns == 0:
        print("All is lost, flee, flee for your lives!")
        break
