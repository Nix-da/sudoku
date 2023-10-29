import numpy as np

class SudokuSolver:

    def __init__(self, sudoku):
        self.sudoku = sudoku
        self.total_sudoku = sudoku.original_sudoku + sudoku.solutions_sudoku

    def find_all_numbers(self, number):
        findings = np.where(self.total_sudoku == number)
        coords = []
        for i in range(len(findings[0])):
            coords.append((findings[0][i], findings[1][i]))
        return coords

    def solve(self, action):
        if action == "nothing":
            return True
        if action == "scan field":
            if self.sudoku.selected is None:
                self.sudoku.selected = (0, 0)
            else:
                x = self.sudoku.selected[0]
                y = self.sudoku.selected[1]
                coord_sum = x + y
                new_coord_sum = (coord_sum + 1) % self.sudoku.grid_count ** 2
                x = new_coord_sum // self.sudoku.segment_count
                y = new_coord_sum % self.sudoku.segment_count
                self.sudoku.selected = (x, y)
            if not self.total_sudoku[self.sudoku.selected] == 0:
                self.sudoku.observations = self.find_all_numbers(self.total_sudoku[self.sudoku.selected])
            return True

        return False
