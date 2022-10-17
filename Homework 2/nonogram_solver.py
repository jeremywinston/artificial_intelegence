# input
'''
input
10 10
1 1
2 2
5
1 1 1
7
5 2
3 1
3 1
4 2
7
1
6
2 6
8
2 6
6 2
1 1
1
1 2
4
'''

import numpy as np
from itertools import combinations

grid = []


def get_input():
    n_row, n_col = list(map(int, input().split(" ")))

    row_raw = []
    column_raw = []

    for i in range(n_row):
        input_row = input()
        arr = list(map(int, input_row.split(' ')))
        row_raw.append(arr)

    for i in range(n_col):
        input_column = input()
        arr = list(map(int, input_column.split(' ')))
        column_raw.append(arr)

    return n_row, n_col, row_raw, column_raw


def all_possibility(arr, max_size):
    decoded_solutions = []
    n_group = len(arr)
    n_empty = max_size - (sum(arr) + n_group - 1)  # empty excluding empty between 2 group
    solutions = combinations(range(n_group + n_empty), n_group)

    encoded_solutions = [i for i in solutions]

    for loc in encoded_solutions:
        result = [-1] * max_size
        past_arr = []
        for n, i in enumerate(loc):
            for j in range(arr[n]):
                result[loc[n] + sum(past_arr) + j] = 1
            past_arr.append(arr[n])
        decoded_solutions.append(result)

    return decoded_solutions


def check_row_overlap(grid_stat, poss_stat):
    for n, data in enumerate(row_poss):
        for i in range(n_col):
            for j in range(len(data)):              # in case: grid_stat = '*' poss_stat = -1
                if row_poss[n][j][i] == poss_stat:  # if we found a -1 on row_poss, then stop the process.
                    break                           # this will save time because we don't have to check all possibility inside the row_poss
                if j == len(data) - 1:              # at the end if we never found -1
                    grid[n][i] = grid_stat          # plot '*' on the grid (same process for grid_stat = '.' poss_stat = 1)


def check_column_overlap(grid_stat, poss_stat):
    for n, data in enumerate(column_poss):
        for i in range(n_row):
            for j in range(len(data)):                  # in case: grid_stat = '*' poss_stat = -1
                if column_poss[n][j][i] == poss_stat:   # if we found a -1 on column_poss, then stop the process.
                    break                               # this will save time because we don't have to check all possibility inside column_poss
                if j == len(data) - 1:                  # if at the end we never found -1
                    grid[i][n] = grid_stat              # plot '*' on the grid (same process for grid_stat = '.' poss_stat = 1)


def decrease_row_possibility(grid_stat, poss_stat):
    for m, g in enumerate(grid):
        for n, i in enumerate(g):
            if i == grid_stat:
                delete = []
                for j in range(len(row_poss[m])):
                    if row_poss[m][j][n] == poss_stat:
                        delete.append(j)
                row_poss[m] = np.delete(row_poss[m], delete, axis=0).tolist()


def decrease_column_possibility(grid_stat, poss_stat):
    for m, g in enumerate(np.transpose(grid).tolist()):
        for n, i in enumerate(g):
            if i == grid_stat:
                delete = []
                for j in range(len(column_poss[m])):
                    if column_poss[m][j][n] == poss_stat:
                        delete.append(j)
                column_poss[m] = np.delete(column_poss[m], delete, axis=0).tolist()


def done():
    row_done = False
    column_done = False

    for data in row_poss:
        if len(data) > 1:
            row_done = False
            break
        row_done = True

    if row_done:
        for data in column_poss:
            if len(data) > 1:
                column_done = False
                break
            column_done = True

        if column_done:
            return True

        return False

    else:
        return False


def print_solution():
    for i in range(n_row):
        print_grid = ''
        for j in range(n_col):
            if grid[i][j] == '*':
                print_grid += '*'
            else:
                print_grid += ' '
        print(print_grid)


if __name__ == '__main__':

    # get all the input
    n_row, n_col, row_raw, column_raw = get_input()

    # create grid world
    grid = [['-' for col in range(n_col)] for row in range(n_row)]

    # convert each row configuration and column configuration into all possible solutions
    row_poss = []
    column_poss = []
    for arr in row_raw:
        row_poss.append(all_possibility(arr, n_row))
    for arr in column_raw:
        column_poss.append(all_possibility(arr, n_col))

    # repeat until done
    while not done():
        # check overlap
        check_row_overlap('*', -1)
        check_row_overlap('.', 1)
        check_column_overlap('*', -1)
        check_column_overlap('.', 1)

        # delete solution that violates the grid
        decrease_row_possibility('*', -1)
        decrease_row_possibility('.', 1)
        decrease_column_possibility('*', -1)
        decrease_column_possibility('.', 1)

    print_solution()
