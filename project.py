import random
import pyfiglet
import cowsay
from dinosay import dinoprint, DINO_TYPE
from tabulate import tabulate

#COMPLEMENTARY FUNCTIONS
def swap_row(grid, a, b):
    temp = grid[a]
    grid[a] = grid[b]
    grid[b] = temp
    return(grid)

def swap_column(grid, a, b):
    for i in range(len(grid)):
        temp = grid[i][a]
        grid[i][a] = grid[i][b]
        grid[i][b] = temp
    return(grid)

def check_none(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == None or grid[i][j] == set():
                return(False)
    return(True)

#FUNCTIONS FOR PLAY MODE
def greeting(text):
    return(pyfiglet.figlet_format(text, "slant"))

def mode_input():
    mode = input("What is your chosen mode? [create_new or play_new])  ")
    while not (mode in ["create_new", "play_new"]):
        cowsay.cow("Invalid. Try again. \N{grinning face}")
        print()
        mode = input("What is your chosen mode? [create_new or play_new])  ")
    if mode == "create_new":
        cowsay.pig("Well done!!! Here you go >:)")
    else:
        cowsay.daemon("Well done!!! Fill in the missing number. You have 1 chance to fill in a block. No correction!")
    return(mode)

def user_input(grid):
    flag = True
    while flag:
        try:
            flag = False
            row = int(input("Please enter row number (1 - 5): ")) - 1
            col = int(input("Please enter column number (1 - 5): ")) - 1
            if grid[row][col] != None:
                flag = True
                print("Invalid position.")
            else:
                number = int(input("Please enter the number (1 - 5): "))
        except:
            flag = True
    return((number, row, col))

def check_correct(grid):
    correct = True
    rows = [set() for i in range(len(grid))]
    cols = [set() for i in range(len(grid[0]))]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            rows[i].add(grid[i][j])
            cols[j].add(grid[i][j])
    check = set(range(1, 6))
    for i in range(len(grid)):
        if rows[i] != check or cols[i] != check:
            correct = False
            break
    return(correct)

def play(grid):
    while not check_none(grid):
        number, i, j = user_input(grid)
        grid[i][j] = number
        print(tabulate(grid, tablefmt = "grid"))
    return(check_correct(grid))

def congrat():
    print(f"Choose a type of dinosaurs from this list. Enter the name lowercase and correctly.")
    types = list(DINO_TYPE.keys())
    print(types)
    type = input("Type: ")
    if not type in types:
        print("Miss your chance")
        cowsay.dragon("CONGARTULATIONS, though! Bye bye.")
        return(False)
    else:
        dinoprint(message = "CONGRATULATIONS", body = DINO_TYPE[type])
        return(True)



#FUNCTIONS FOR CREATING AND SOLVING THE PUZZLES
def initialize(grid):
    for i in range(5):
        new = [(i+j+1)%5 + 1 for j in range(5)]
        grid.append(new)
    r_swaps = random.randint(3, 10)
    c_swaps = random.randint(3, 10)
    for i in range(r_swaps):
        grid = swap_row(grid, random.randint(0, 4), random.randint(0, 4))
    for i in range(c_swaps):
        grid = swap_column(grid, random.randint(0, 4), random.randint(0, 4))
    return(grid)


def checker(grid):
    values = set([1, 2, 3, 4, 5])
    poss_grid = [[set() for i in range(5)] for j in range(5)]
    exist_row = [set() for i in range(5)]
    exist_col = [set() for i in range(5)]
    for i in range(5):
        for j in range(5):
            if grid[i][j] != None:
                exist_row[i].add(grid[i][j])
                exist_col[j].add(grid[i][j])
    for i in range(5):
        for j in range(5):
            if grid[i][j] == None:
                new = values.difference(exist_row[i])
                new = new.difference(exist_col[j])
                poss_grid[i][j] = new
    return(poss_grid)


def unique(grid):
    poss_grid = checker(grid)
    unique_grid = [[set() for i in range(5)] for j in range(5)]
    for i in range(5):
        for j in range(5):
            if poss_grid[i][j] != set():
                other_row = set()
                for x in range(5):
                    if x != j:
                        other_row = other_row.union(poss_grid[i][x])
                other_col = set()
                for x in range(5):
                    if i != x:
                        other_col = other_col.union(poss_grid[x][j])
                new = poss_grid[i][j].difference(other_row)
                new = new.difference(other_col)
                unique_grid[i][j] = new
    return(unique_grid)


def solver(grid):
    unique_grid = unique(grid)
    flag = True
    while flag == True:
        flag = False
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if len(unique_grid[i][j]) == 1:
                    flag = True
                    grid[i][j] = list(unique_grid[i][j])[0]
        unique_grid = unique(grid)
    if check_none(grid):
        return(grid, True)
    else:
        return(None, False)


def creator(grid):
    seed = set()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            seed.add((i, j))
    for pair in seed:
        i, j = pair
        temp = grid[i][j]
        grid[i][j] = None
        new = [row[:] for row in grid]
        solved, flag = solver(new)
        if flag == False:
            grid[i][j] = temp
    return(grid)


def main():
    print(greeting("WELCOME TO"))
    print(greeting("SUDOKU  5 X 5"))
    mode = mode_input()
    grid = []
    grid = initialize(grid)
    new = creator(grid)
    print(tabulate(new, tablefmt = "grid"))
    if mode == "play_new":
        result = play(new)
        if result == False:
            cowsay.fox("Sorry, you didn't solve the puzzle. The grapes are sour")
        else:
            flag = congrat()
    print(greeting("Game over"))


if __name__ == "__main__":
    main()