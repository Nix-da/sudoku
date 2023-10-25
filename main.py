import pygame
import numpy as np


pygame.font.init()
screen = pygame.display.set_mode((500, 600))

pygame.display.set_caption("sudoku solver")
#img = pygame.image.load('icon.png')
#pygame.display.set_icon(img)
font = pygame.font.SysFont("calibri", 20)

# empty sudoku
grid = np.zeros((9, 9))


def draw():
    dif = 500 / 9
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                pygame.draw.rect(screen, (0, 153, 153), (i * dif, j * dif, dif + 1, dif + 1))

    for i in range(10):
        if i % 3 == 0:
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, (5, 5, 5), (5, i * dif), (500, i * dif), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)


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
