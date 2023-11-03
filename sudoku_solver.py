import numpy as np


class SudokuSolver:

    def __init__(self, sudoku):
        self.sudoku = sudoku

    def find_all_numbers(self, number):
        findings = np.where(self.sudoku.get_total_sudoku() == number)
        coords = []
        for i in range(len(findings[0])):
            coords.append((findings[0][i], findings[1][i]))
        return coords

    def scan_field(self):
        if self.sudoku.get_selected_coord() is None:
            self.sudoku.select((0, 0))
        else:
            current_coord = self.sudoku.get_selected_coord()
            next_position = (1 + self.sudoku.index_from_coord(current_coord)) % self.sudoku.get_grid_count() ** 2
            self.sudoku.select(next_position)
        if not self.sudoku.get_selected_number() == 0:
            self.sudoku.observations = self.find_all_numbers(self.sudoku.get_selected_number())
            self.sudoku.observations += (self.sudoku.get_row(self.sudoku.get_selected_coord())[1])
            self.sudoku.observations += (self.sudoku.get_col(self.sudoku.get_selected_coord())[1])
            self.sudoku.observations += (self.sudoku.get_segment(self.sudoku.get_selected_coord())[1])
        else:
            self.sudoku.observations = []

    def fill_possibilities(self):
        if self.sudoku.get_number(self.sudoku.get_selected_coord()) == 0:
            self.sudoku.set_possibilities(self.sudoku.get_selected_coord(), [1,2,3,4,5,6,7,8,9])

    def solve(self, action):
        if action == "nothing":
            return True
        if action == "scan field":
            self.scan_field()
            return True
        if action == "fill possibilities":
            self.fill_possibilities()
            return True

        return False
