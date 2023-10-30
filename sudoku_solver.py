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
                new_coord_sum = (x * self.sudoku.grid_count + y + 1) % (self.sudoku.grid_count ** 2)
                self.sudoku.selected = (new_coord_sum // self.sudoku.grid_count, new_coord_sum % self.sudoku.grid_count)
            if not self.total_sudoku[self.sudoku.selected] == 0:
                self.sudoku.observations = self.find_all_numbers(self.total_sudoku[self.sudoku.selected])
                self.sudoku.selected_number = self.total_sudoku[self.sudoku.selected[0]][self.sudoku.selected[1]]
            else:
                self.sudoku.observations = []
                self.sudoku.selected_number = 0
            return True

        return False
