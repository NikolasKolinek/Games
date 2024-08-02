import numpy as np
from setup import *

class Board:
    def __init__(self):
        self.squares = np.zeros((ROWS, COLS))
        self.empty_squares = self.squares
        self.marked_squares = 0

    def final_state(self, show=False):
        # return 0 if there is  no win yet
        # return 1 if player 1 win
        # return 2 if player 2 win

        # VERTICAL WINS
        for col in range(COLS):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:
                if show:
                    color = CIRC_COLOR if self.squares[0][col] == 2 else CROSS_COLOR
                    i_pos = (col * SQUARE_SIZE + SQUARE_SIZE // 2, 20)
                    f_pos = (col * SQUARE_SIZE + SQUARE_SIZE // 2, HEIGHT - 20)
                    pygame.draw.line(screen, color, i_pos, f_pos, LINE_WIDTH)
                return self.squares[0][col]

        # HORIZONTAL WINS
        for row in range(ROWS):
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                if show:
                    color = CIRC_COLOR if self.squares[row][0] == 2 else CROSS_COLOR
                    i_pos = (20, row + SQUARE_SIZE + SQUARE_SIZE // 2)
                    f_pos = (WIDTH - 20, row * SQUARE_SIZE + SQUARE_SIZE // 2)
                    pygame.draw.line(screen, color, i_pos, f_pos, LINE_WIDTH)
                return self.squares[row][0]

        # DESCENDING DIAGONAL
            if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
                if show:
                    color = CIRC_COLOR if self.squares[1][1] == 2 else CROSS_COLOR
                    i_pos = (20, 20)
                    f_pos = (WIDTH - 20, HEIGHT - 20)
                    pygame.draw.line(screen, color, i_pos, f_pos, CROSS_WIDTH)
                return self.squares[1][1]

        # ASCENDING DIAGONAL
            if self.squares[2][0] == self.squares[1][1] == self.squares[0][2] != 0:
                if show:
                    color = CIRC_COLOR if self.squares[1][1] == 2 else CROSS_COLOR
                    i_pos = (20, HEIGHT - 20)
                    f_pos = (WIDTH - 20, 20)
                    pygame.draw.line(screen, color, i_pos, f_pos, CROSS_WIDTH)
                return self.squares[1][1]

        # NO WINN FOUND
        return 0

    def mark_sqr(self, row, col, player):
        self.squares[row][col] = player
        self.marked_squares += 1

    def empty_sqr(self, row, col):
        return self.squares[row][col] == 0

    def get_empty_squares(self):
        marked_squares = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.empty_sqr(row, col):
                    marked_squares.append((row,col))

        return marked_squares

    def is_full(self):
        return self.marked_squares == 9

    def is_empty(self):
        return self.marked_squares == 0
