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

    def up(self):
        self.__navigate(-1)

    def down(self):
        self.__navigate(1)

    def left(self):
        self.__navigate(-self.sudoku.get_grid_count())

    def right(self):
        self.__navigate(self.sudoku.get_grid_count())

    def __navigate(self, step):
        if self.sudoku.get_selected_coord() is None:
            self.sudoku.select((0, 0))
        else:
            current_coord = self.sudoku.get_selected_coord()
            next_position = (self.sudoku.index_from_coord(current_coord) + step) % self.sudoku.get_grid_count() ** 2
            self.sudoku.select(next_position)
        if not self.sudoku.get_selected_number() == 0:
            self.sudoku.observations = self.find_all_numbers(self.sudoku.get_selected_number())
            self.sudoku.observations += self.sudoku.get_relevant_elements(self.sudoku.get_selected_coord())[1]
        else:
            self.sudoku.observations = []

    def fill_possibilities(self):
        if self.sudoku.get_number(self.sudoku.get_selected_coord()) == 0:

            self.sudoku.observations = self.sudoku.get_relevant_elements(self.sudoku.get_selected_coord())[1]

            observed_numbers = self.sudoku.get_relevant_elements(self.sudoku.get_selected_coord())[0]

            possibilities = self.sudoku.numbers

            for i in range(len(possibilities)):
                if possibilities[i] in observed_numbers:
                    possibilities[i] = 0

            self.sudoku.set_possibilities(self.sudoku.get_selected_coord(), possibilities)

    def fill_all_possibilities(self):
        for i in range(self.sudoku.get_grid_count() ** 2):
            self.fill_possibilities()
            self.down()

    def apply_possibility(self):
        # if there is only one option left in the cell
        possibilities = set(self.sudoku.get_possibilities(self.sudoku.get_selected_coord()))
        if len(possibilities) == 2:
            possibilities.remove(0)
            self.sudoku.set_value(self.sudoku.get_selected_coord(), possibilities.pop())

        # if there is only one option left in the segment
        possibilities = []
        segment_coords = self.sudoku.get_segment(self.sudoku.get_selected_coord())[1]
        for segment_coord in segment_coords:
            possibilities += list(self.sudoku.get_possibilities(segment_coord))

        for number in self.sudoku.numbers:
            if possibilities.count(number) == 1:
                self.sudoku.set_value(segment_coords[int(possibilities.index(number) // self.sudoku.get_grid_count())], number)

        # if there is only one option left in the row
        possibilities = []
        row_coords = self.sudoku.get_row(self.sudoku.get_selected_coord())[1]
        for row_coord in row_coords:
            possibilities += list(self.sudoku.get_possibilities(row_coord))

        for number in self.sudoku.numbers:
            if possibilities.count(number) == 1:
                self.sudoku.set_value(row_coords[int(possibilities.index(number) // self.sudoku.get_grid_count())],
                                      number)

        # if there is only one option left in the col
        possibilities = []
        col_coords = self.sudoku.get_col(self.sudoku.get_selected_coord())[1]
        for col_coord in col_coords:
            possibilities += list(self.sudoku.get_possibilities(col_coord))

        for number in self.sudoku.numbers:
            if possibilities.count(number) == 1:
                self.sudoku.set_value(col_coords[int(possibilities.index(number) // self.sudoku.get_grid_count())],
                                      number)

    def apply_all_possibilities(self):
        for i in range(self.sudoku.get_grid_count() ** 2):
            self.apply_possibility()
            self.down()

    def solve(self, action):
        # default
        if action == "nothing":
            return True

        # navigation
        if action == "up":
            self.up()
            return True
        if action == "down":
            self.down()
            return True
        if action == "left":
            self.left()
            return True
        if action == "right":
            self.right()
            return True

        # interaction

        # validation

        # automation
        if action == "fill possibilities":
            self.fill_possibilities()
            return True
        if action == "fill all possibilities":
            self.fill_all_possibilities()
            return True
        if action == "apply possibility":
            self.apply_possibility()
            return True
        if action == "apply all possibilities":
            self.apply_all_possibility()
            return True

        return False
