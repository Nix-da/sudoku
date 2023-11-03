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

    def solve(self, action):
        if action == "nothing":
            return True
        if action == "scan field":
            if self.sudoku.get_selected_coord() is None:
                self.sudoku.select((0, 0))
            else:
                current_coord = self.sudoku.get_selected_coord()
                next_position = 1 + self.sudoku.index_from_coord(current_coord)
                self.sudoku.select(next_position)
            if not self.sudoku.get_selected_number() == 0:
                self.sudoku.observations = self.find_all_numbers(self.sudoku.get_selected_number())
            else:
                self.sudoku.observations = []
                # self.sudoku.selected_number = 0
            return True

        return False
