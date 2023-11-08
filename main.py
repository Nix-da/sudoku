from sudoku import Sudoku
from sudoku_solver import SudokuSolver
from gui import Sudoku_user_interface

sudoku = Sudoku()
sudoku.read_sudoku_from_file("./data/saved_sudokus/9_hard_001.txt")
sudoku_solver = SudokuSolver(sudoku)
gui = Sudoku_user_interface(sudoku)
gui.open()

run = True

while run:
    event = gui.update()
    if event == "Quit":
        run = False

    run = sudoku_solver.solve(event)

gui.quit()
