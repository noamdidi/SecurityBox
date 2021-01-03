import random

def generate_grid():
    grid = []
    row = []
    while grid.__len__() != 9:
        pixel = random.randint(1, 9)
        if pixel not in row:
            row.append(pixel)
        if row.__len__() == 9:
            grid.append(row)
            row = []
    return grid

def hide_pixels(grid, level):
    count = 0
    for row in grid:
        while count < level:
            place = random.randint(0, 8)
            if row[place] != 'X':
                row[place] = 'X'
                count += 1
        count = 0
    return grid

def print_grid(grid):
    for row in grid:
        print(*row, sep = ' | ')
        print("----------------------------------")

def main():
    print("choose difficulty:"
          "1. piece of cake"
          "2. mmmmedium"
          "3. ok it's hard"
          "4. HELL")
    level = int(input("I want: "))
    print_grid(hide_pixels(generate_grid(), level))

main()

