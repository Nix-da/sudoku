from sudoku import Sudoku
from gui import Sudoku_user_interface

sudoku = Sudoku()
gui = Sudoku_user_interface(sudoku)
gui.open()

run = True

while run:
    run = gui.update()

gui.quit()
