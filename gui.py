import pygame

class Sudoku_user_interface():
    sudoku_cell_size = 50
    sudoku_cell_line = 1
    sudoku_cell_border = 2
    sudoku_offset = 40

    def __init__(self, sudoku):
        self.sudoku = sudoku
        self.sudoku_width = self.sudoku.grid_count * self.sudoku_cell_size + \
                            6 * self.sudoku_cell_line + \
                            4 * self.sudoku_cell_border
        self.sudoku_height = self.sudoku.grid_count * self.sudoku_cell_size + \
                             6 * self.sudoku_cell_line + \
                             4 * self.sudoku_cell_border

        self.window_width = self.sudoku_width + 2 * self.sudoku_offset
        self.window_height = 1.1 * self.sudoku_height + 2 * self.sudoku_offset

    def open(self):
        pygame.font.init()
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))

        pygame.display.set_caption("sudoku solver")
        # img = pygame.image.load('icon.png')
        # pygame.display.set_icon(img)
        self.font = pygame.font.SysFont("calibri", 35)

    def quit(self):
        pygame.quit()

    def draw(self):
        # draw border
        start_coord = (
            self.sudoku_offset,
            self.sudoku_offset
        )
        dimensions = (
            self.sudoku_cell_size * self.sudoku.grid_count,
            self.sudoku_cell_size * self.sudoku.grid_count
        )
        pygame.draw.rect(
            self.screen,
            (0, 0, 0),
            (start_coord, dimensions),
            self.sudoku_cell_border * 2
        )

        # draw segments
        for i in range(self.sudoku.segment_count):
            for j in range(self.sudoku.segment_count):
                start_coord = (
                    self.sudoku_offset + i * self.sudoku_cell_size * self.sudoku.segment_count,
                    self.sudoku_offset + j * self.sudoku_cell_size * self.sudoku.segment_count
                )
                dimensions = (
                    self.sudoku_cell_size * 3,
                    self.sudoku_cell_size * 3
                )
                pygame.draw.rect(
                    self.screen,
                    (0, 0, 0),
                    (start_coord, dimensions),
                    self.sudoku_cell_border
                )

        # draw small cells
        for i in range(self.sudoku.grid_count):
            for j in range(self.sudoku.grid_count):
                start_coord = (
                    self.sudoku_offset + i * self.sudoku_cell_size,
                    self.sudoku_offset + j * self.sudoku_cell_size
                )
                dimensions = (
                    self.sudoku_cell_size,
                    self.sudoku_cell_size
                )
                pygame.draw.rect(
                    self.screen,
                    (0, 0, 0),
                    (start_coord, dimensions),
                    1
                )

        # write numbers
        for i in range(self.sudoku.grid_count):
            for j in range(self.sudoku.grid_count):
                if not self.sudoku.original_sudoku[i][j] == 0:
                    text = self.font.render(str(self.sudoku.original_sudoku[i][j]), 1, (0, 0, 0))
                    self.screen.blit(
                        text,
                        (i * self.sudoku_cell_size + self.sudoku_offset + 16,
                         j * self.sudoku_cell_size + self.sudoku_offset + 9)
                    )

    def update(self):
        self.screen.fill((229, 229, 229))

        # detect key press
        for event in pygame.event.get():
            # quit
            if event.type == pygame.QUIT:
                return False

        self.draw()
        pygame.display.update()

        return True
