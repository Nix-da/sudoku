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

    # get the currently selected coordinate
    def get_selected_coord(self):
        return self.__selected

    # select a field at the given position
    def select(self, position) -> int:
        coord = self.__get_coord_from_position(position)
        self.__selected = coord
        self.__selected_number = self.get_number(coord)
        return self.__selected_number

    # set the value of a field at the given position
    def set_value(self, position: Union[int, Tuple[int, int]], value: int):
        coord = self.__get_coord_from_position(position)

        self.__solutions_sudoku[coord[0]][coord[1]] = value
        self.__total_sudoku[coord[0]][coord[1]] = value
        self.__solutions_sudoku[coord[0]][coord[1]] = 0  # np.zeros(self.__grid_count)
        return coord
