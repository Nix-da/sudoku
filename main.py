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


run = True

while run:
    screen.fill((229, 229, 229))
    pygame.display.update()

pygame.quit()