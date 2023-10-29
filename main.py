from sudoku import Sudoku
from sudoku_solver import SudokuSolver
from gui import Sudoku_user_interface

sudoku = Sudoku()
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
