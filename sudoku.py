import math

import numpy as np
from typing import Union, Tuple


class Sudoku:

    # creates a new, empty sudoku. Default size is 9x9
    def __init__(self, grid_count=9):
        # if the grid size is not a square number, it is rounded back to the last lower sqaure number
        self.__segment_count = math.floor(math.sqrt(grid_count))
        self.__grid_count = self.__segment_count ** 2

        # initialize 2D arrays to represent the sudoku grid
        self.__original_sudoku = np.zeros(shape=(self.__grid_count, self.__grid_count))
        self.__solutions_sudoku = np.zeros(shape=(self.__grid_count, self.__grid_count))
        self.__possibilities_sudoku = np.zeros(shape=(self.__grid_count, self.__grid_count, self.__grid_count))
        self.__total_sudoku = self.__original_sudoku

        # initialize the selection and observation space
        self.__selected = None
        self.__selected_number = 0
        self.observations = []

        # initialize the numbers
        self.numbers = [x for x in range(1, self.__grid_count + 1)]

    # reads a sudoku from a text file
    def read_sudoku_from_file(self, file):
        self.__original_sudoku = np.array(
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
        self.__total_sudoku = self.__original_sudoku

    # calculates the (x, y) coordinate of the collapsed array index
    def coord_from_index(self, index: int) -> Tuple[int, int]:
        return index // self.__grid_count, index % self.__grid_count

    # calculates the collapsed array index of a coord
    def index_from_coord(self, coord: Tuple[int, int]):
        return coord[0] * self.__grid_count + coord[1]

    # getter for segment count
    def get_segment_count(self):
        return self.__segment_count

    # getter for grid count
    def get_grid_count(self):
        return self.__grid_count

    # getter for original sudoku
    def get_original_sudoku(self):
        return self.__original_sudoku

    # getter for solutions sudoku
    def get_solutions_sudoku(self):
        return self.__solutions_sudoku

    # getter for total sudoku
    def get_total_sudoku(self):
        return self.__total_sudoku

    # getter for possibilities sudoku
    def get_possibilities_sudoku(self):
        return self.__possibilities_sudoku

    # converts Union[index of collapsed array, (x, y) coordinate] into the coordinate
    # only for in-class calculations
    def __get_coord_from_position(self, position):
        if isinstance(position, int):
            return self.coord_from_index(position)
        if isinstance(position, Tuple):
            return position
        return None

    # get number of the currently selected field
    def get_selected_number(self) -> int:
        return self.__selected_number

    # get number of a field at the given position
    def get_number(self, position: Union[int, Tuple[int, int]]) -> int:
        coord = self.__get_coord_from_position(position)

        return self.__total_sudoku[coord[0]][coord[1]]

    # get number of the currently selected field
    def get_selected_possibilities(self) -> int:
        return self.__possibilities_sudoku[self.__selected[0]][[self.__selected[1]]]

    # get number of a field at the given position
    def get_possibilities(self, position: Union[int, Tuple[int, int]]) -> int:
        coord = self.__get_coord_from_position(position)

        return self.__possibilities_sudoku[coord[0]][coord[1]]

    # get the currently selected coordinate
    def get_selected_coord(self):
        return self.__selected

    # get current row, values at index 0, coordinates at index 1
    def get_row(self, position):
        coord = self.__get_coord_from_position(position)
        row = []
        row_index = []
        for i in range(self.__grid_count):
            row.append(self.__total_sudoku[i][coord[0]])
            row_index.append((coord[0], i))
        return row, row_index

    # get current column, values at index 0, coordinates at index 1
    def get_col(self, position):
        coord = self.__get_coord_from_position(position)
        col = []
        col_index = []
        for i in range(self.__grid_count):
            col.append(self.__total_sudoku[coord[1]][i])
            col_index.append((i, coord[1]))
        return col, col_index

    # get current segment, values at index 0, coordinates at index 1
    def get_segment(self, position):
        coord = self.__get_coord_from_position(position)
        segment = []
        segment_index = []
        x_from = self.__segment_count * (coord[0] // self.__segment_count)
        x_to = x_from + self.__segment_count
        y_from = self.__segment_count * (coord[1] // self.__segment_count)
        y_to = y_from + self.__segment_count
        for i in range(x_from, x_to):
            for j in range(y_from, y_to):
                segment.append(self.__total_sudoku[i][j])
                segment_index.append((i, j))
        return segment, segment_index

    # get current row, col and segment, values at index 0, coordinates at index 1
    def get_relevant_elements(self, position):
        rows = self.get_row(position)
        cols = self.get_col(position)
        segments = self.get_segment(position)
        return rows[0] + cols[0] + segments[0], rows[1] + cols[1] + segments[1]

    # select a field at the given position
    def select(self, position) -> int:
        coord = self.__get_coord_from_position(position)
        self.__selected = coord
        self.__selected_number = self.get_number(coord)
        return self.__selected_number

    def set_possibilities(self, position, possibilities):
        coord = self.__get_coord_from_position(position)
        self.__possibilities_sudoku[coord[0]][coord[1]] = possibilities
        self.numbers = [x for x in range(1, self.__grid_count + 1)]

    # set the value of a field at the given position
    def set_value(self, position: Union[int, Tuple[int, int]], value: int):
        coord = self.__get_coord_from_position(position)

        self.__solutions_sudoku[coord[0]][coord[1]] = value
        self.__total_sudoku[coord[0]][coord[1]] = value

        # remove all possibilities in this row, col and segment
        for possibility_coord in self.get_relevant_elements(coord)[1]:
            self.get_possibilities_sudoku()[possibility_coord[0]][possibility_coord[1]][int(value) - 1] = 0

        return coord
