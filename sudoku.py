import numpy as np


class Sudoku:
    segment_count = 3
    grid_count = segment_count ** 2

    original_sudoku = np.zeros(shape=(grid_count, grid_count))
    solutions_sudoku = np.zeros(shape=(grid_count, grid_count))
    possibilities_sudoku = np.zeros(shape=(grid_count, grid_count, grid_count))

    selected = (0, 0)
    observations = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9)]

    def __init__(self):
        self.read_sudoku_from_file("")

    def read_sudoku_from_file(self, file):
        self.original_sudoku = np.array(
            [
                [0, 0, 5, 2, 0, 0, 0, 6, 0],
                [0, 0, 0, 8, 0, 0, 0, 0, 3],
                [0, 7, 0, 0, 3, 5, 0, 9, 0],
                [0, 8, 0, 0, 0, 0, 6, 0, 0],
                [0, 0, 6, 0, 5, 9, 0, 0, 1],
                [0, 0, 0, 0, 0, 2, 0, 0, 0],
                [0, 0, 8, 0, 1, 6, 0, 0, 9],
                [4, 0, 0, 0, 0, 0, 0, 7, 0],
                [0, 0, 0, 3, 0, 0, 0, 0, 0],
            ]
        )
        self.solutions_sudoku[0][0] = 1
        self.possibilities_sudoku[1][0][0] = 1
        self.possibilities_sudoku[1][0][0] = 2
        self.possibilities_sudoku[1][0][0] = 3
        self.possibilities_sudoku[1][0][0] = 4
        self.possibilities_sudoku[1][0][0] = 5
        self.possibilities_sudoku[1][0][0] = 6
        self.possibilities_sudoku[1][0][0] = 7
        self.possibilities_sudoku[1][0][0] = 8
        self.possibilities_sudoku[1][0][0] = 9
