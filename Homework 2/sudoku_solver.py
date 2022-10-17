# input
'''
0 4 0 0 0 0 0 0 0
0 0 1 0 3 4 6 2 0
6 0 3 0 0 0 0 7 0
0 0 0 4 8 3 5 0 7
0 0 0 0 5 0 0 6 0
0 0 0 0 0 9 0 4 0
0 0 5 0 0 0 0 0 1
8 0 0 5 4 7 3 9 6
0 0 0 0 2 1 0 0 0
'''

grid = []


def get_input():
    for i in range(9):
        input_grid = input()
        arr = list(map(int, input_grid.split(" ")))
        grid.append(arr)


def possible(x, y, n):
    # check for every element in row x is it possible to assign n
    for j in range(9):
        if grid[x][j] == n:
            return False

    # check for every element in the column y is it possible to assign n
    for i in range(9):
        if grid[i][y] == n:
            return False

    # check for every element in the region is it possible to assign n
    xc = x//3
    yc = y//3
    for i in range(xc*3, xc*3+3):
        for j in range(yc*3, yc*3+3):
            if grid[i][j] == n:
                return False
    return True


def sudoku_solver():
    for x in range(9):
        for y in range(9):
            if grid[x][y] == 0:
                for n in range(1, 10):
                    if possible(x, y, n):
                        grid[x][y] = n
                        sudoku_solver()
                        grid[x][y] = 0
                return # back tracking
    print_answer()


def print_answer():
    for x in range(9):
        solution = ""
        for y in range(9):
            solution += str(grid[x][y]) + ' '
        print(solution)


if __name__ == '__main__':
    get_input()
    sudoku_solver()



