import math

import pygame
import numpy as np


sudoku_segment_count = 3
sudoku_grid_count = sudoku_segment_count ** 2
sudoku_cell_size = 50
sudoku_cell_line = 1
sudoku_cell_border = 2
sudoku_cell_highlight = 3
sudoku_offset = 40

sudoku_width = sudoku_grid_count * sudoku_cell_size + 6 * sudoku_cell_line + 7 * sudoku_cell_border
sudoku_height = sudoku_grid_count * sudoku_cell_size + 6 * sudoku_cell_line + 7 * sudoku_cell_border

window_width = sudoku_width + 2 * sudoku_offset
window_height = 1.1 * sudoku_height + 2 * sudoku_offset

# empty sudoku
grid = np.zeros((sudoku_grid_count, sudoku_grid_count))

pygame.font.init()
screen = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption("sudoku solver")
#img = pygame.image.load('icon.png')
#pygame.display.set_icon(img)
font = pygame.font.SysFont("calibri", 20)


def draw():
    # draw border
    start_coord = (
        sudoku_offset,
        sudoku_offset
    )
    dimensions = (
        sudoku_cell_size * sudoku_grid_count,
        sudoku_cell_size * sudoku_grid_count
    )
    pygame.draw.rect(
        screen,
        (0, 0, 0),
        (start_coord, dimensions),
        sudoku_cell_border * 2
    )

    # draw segments
    for i in range(sudoku_segment_count):
        for j in range(sudoku_segment_count):
            start_coord = (
                sudoku_offset + i * sudoku_cell_size * sudoku_segment_count,
                sudoku_offset + j * sudoku_cell_size * sudoku_segment_count
            )
            dimensions = (
                sudoku_cell_size * 3,
                sudoku_cell_size * 3
            )
            pygame.draw.rect(
                screen,
                (0, 0, 0),
                (start_coord, dimensions),
                sudoku_cell_border
            )

    # draw small cells
    for i in range(sudoku_grid_count):
        for j in range(sudoku_grid_count):
            start_coord = (
                sudoku_offset + i * sudoku_cell_size,
                sudoku_offset + j * sudoku_cell_size
            )
            dimensions = (
                sudoku_cell_size,
                sudoku_cell_size
            )
            pygame.draw.rect(
                screen,
                (0, 0, 0),
                (start_coord, dimensions),
                1
            )
            text = font.render(str(grid[i][j]), 1, (0, 0, 0))
            screen.blit(text, (i * sudoku_cell_size + sudoku_offset + 10, j * sudoku_cell_size + sudoku_offset + 10))


run = True

while run:
    screen.fill((229, 229, 229))

    # detect key press
    for event in pygame.event.get():
        # quit
        if event.type == pygame.QUIT:
            run = False

    draw()
    pygame.display.update()

pygame.quit()
