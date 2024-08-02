import pygame

# SCREEN RESOLUTION
WIDTH = 600
HEIGHT = 600

# ROWS AND COLUMNS
ROWS = 3
COLS = 3
SQUARE_SIZE = WIDTH // COLS

LINE_WIDTH = 15
CIRC_WIDTH = 15
CROSS_WIDTH = 20

RADIUS = SQUARE_SIZE // 4

OFFSET = 50

# COLORS
BG_COLOUR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRC_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic-Tac-Toe Game')
screen.fill(BG_COLOUR)
