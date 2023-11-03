import pygame

class Sudoku_user_interface():
    sudoku_cell_size = 50
    sudoku_cell_line = 1
    sudoku_cell_border = 2
    sudoku_offset = 40

    border_color = (52, 72, 97)
    line_color = (191, 198, 212)
    original_color = (52, 72, 97)
    solutions_color = (50, 90, 175)
    possibilities_color = (110, 124, 140)
    selected_bckgr_color = (187, 222, 251)
    observation_bckgr_color = (216, 225, 233)


    def __init__(self, sudoku):
        self.sudoku = sudoku
        self.sudoku_width = self.sudoku.get_grid_count() * self.sudoku_cell_size + \
                            6 * self.sudoku_cell_line + \
                            4 * self.sudoku_cell_border
        self.sudoku_height = self.sudoku.get_grid_count() * self.sudoku_cell_size + \
                             6 * self.sudoku_cell_line + \
                             4 * self.sudoku_cell_border

        self.window_width = self.sudoku_width + 2 * self.sudoku_offset
        self.window_height = 1.1 * self.sudoku_height + 2 * self.sudoku_offset

        pygame.font.init()
        self.font_possible_selected = pygame.font.SysFont("calibri", 15, bold=True)
        self.font_possible = pygame.font.SysFont("calibri", 15)
        self.font_original_selected = pygame.font.SysFont("calibri", 35, bold=True)
        self.font_original = pygame.font.SysFont("calibri", 35)
        self.font_solution = pygame.font.SysFont("calibri", 35)
        self.font_solution_selected = pygame.font.SysFont("calibri", 35, bold=True)

    def open(self):
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))

        pygame.display.set_caption("sudoku solver")
        # img = pygame.image.load('icon.png')
        # pygame.display.set_icon(img)

    def quit(self):
        pygame.quit()

    def draw(self):
        # draw small cells
        for i in range(self.sudoku.get_grid_count()):
            for j in range(self.sudoku.get_grid_count()):
                start_coord = (
                    self.sudoku_offset + i * self.sudoku_cell_size,
                    self.sudoku_offset + j * self.sudoku_cell_size
                )
                dimensions = (
                    self.sudoku_cell_size,
                    self.sudoku_cell_size
                )

                if (i, j) in self.sudoku.observations:
                    pygame.draw.rect(
                        self.screen,
                        self.observation_bckgr_color,
                        (start_coord, dimensions)
                    )
                if (i, j) == self.sudoku.get_selected_coord():
                    pygame.draw.rect(
                        self.screen,
                        self.selected_bckgr_color,
                        (start_coord, dimensions)
                    )
                pygame.draw.rect(
                    self.screen,
                    self.line_color,
                    (start_coord, dimensions),
                    1
                )

        # draw segments
        for i in range(self.sudoku.get_segment_count()):
            for j in range(self.sudoku.get_segment_count()):
                start_coord = (
                    self.sudoku_offset + i * self.sudoku_cell_size * self.sudoku.get_segment_count(),
                    self.sudoku_offset + j * self.sudoku_cell_size * self.sudoku.get_segment_count()
                )
                dimensions = (
                    self.sudoku_cell_size * self.sudoku.get_segment_count(),
                    self.sudoku_cell_size * self.sudoku.get_segment_count()
                )
                pygame.draw.rect(
                    self.screen,
                    self.border_color,
                    (start_coord, dimensions),
                    self.sudoku_cell_border
                )

        # draw border
        start_coord = (
            self.sudoku_offset,
            self.sudoku_offset
        )
        dimensions = (
            self.sudoku_cell_size * self.sudoku.get_grid_count(),
            self.sudoku_cell_size * self.sudoku.get_grid_count()
        )
        pygame.draw.rect(
            self.screen,
            self.border_color,
            (start_coord, dimensions),
            self.sudoku_cell_border * 2
        )

        # write numbers
        for i in range(self.sudoku.get_grid_count()):
            for j in range(self.sudoku.get_grid_count()):
                # write original
                if not self.sudoku.get_original_sudoku()[i][j] == 0:
                    if self.sudoku.get_selected_number() == self.sudoku.get_original_sudoku()[i][j]:
                        text = self.font_original_selected.render(
                            str(int(self.sudoku.get_original_sudoku()[i][j])),
                            True,
                            self.original_color
                        )
                    else:
                        text = self.font_original.render(
                            str(int(self.sudoku.get_original_sudoku()[i][j])),
                            True,
                            self.original_color
                        )

                    self.screen.blit(
                        text,
                        (i * self.sudoku_cell_size + self.sudoku_offset + 16,
                         j * self.sudoku_cell_size + self.sudoku_offset + 9)
                    )

                # write solutions
                if not self.sudoku.get_solutions_sudoku()[i][j] == 0:
                    if self.sudoku.get_selected_number() == self.sudoku.get_solutions_sudoku()[i][j]:
                        text = self.font_solution_selected.render(
                            str(int(self.sudoku.get_solutions_sudoku()[i][j])),
                            True,
                            self.original_color
                        )
                    else:
                        text = self.font_original.render(
                            str(int(self.sudoku.get_solutions_sudoku()[i][j])),
                            True,
                            self.original_color
                        )
                    self.screen.blit(
                        text,
                        (i * self.sudoku_cell_size + self.sudoku_offset + 16,
                         j * self.sudoku_cell_size + self.sudoku_offset + 9)
                    )

                # write possibilities
                for n in range(self.sudoku.get_segment_count()):
                    for m in range(self.sudoku.get_segment_count()):
                        if not self.sudoku.get_possibilities_sudoku()[i][j][n * self.sudoku.get_segment_count() + m] == 0:
                            if self.sudoku.get_selected_number() == self.sudoku.get_possibilities_sudoku()[i][j][n * self.sudoku.get_segment_count() + m]:
                                text = self.font_possible_selected.render(
                                    str(int(self.sudoku.get_possibilities_sudoku()[i][j][n * self.sudoku.get_segment_count() + m])),
                                    True,
                                    self.possibilities_color
                                )
                            else:
                                text = self.font_possible.render(
                                    str(int(self.sudoku.get_possibilities_sudoku()[i][j][n * self.sudoku.get_segment_count() + m])),
                                    True,
                                    self.possibilities_color
                                )

                            self.screen.blit(
                                text,
                                (i * self.sudoku_cell_size + self.sudoku_offset + 7 + n * 14,
                                 j * self.sudoku_cell_size + self.sudoku_offset + 7 + m * 14)
                            )


    def update(self):
        self.screen.fill((229, 229, 229))

        key_press_event = "nothing"
        # detect key press
        for event in pygame.event.get():
            # quit
            if event.type == pygame.QUIT:
                key_press_event = "Quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key_press_event = "scan field"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                    key_press_event = "fill possibilities"

        self.draw()
        pygame.display.update()

        return key_press_event
