import pygame
pygame.init()

SCREEN_X = 600
SCREEN_Y = 600

RECTANGLE_X = 200
RECTANGLE_Y = 200

GRID_SIZE_X = 3
GRID_SIZE_Y = 3

GRID_COLOR = (255, 255, 255)
LINE_COLOR = (255, 0, 0)

BLOCK_SIZE = 200

X_ICON = pygame.transform.scale(pygame.image.load('Resources/x.png'), (BLOCK_SIZE - 2, BLOCK_SIZE - 2))
O_ICON = pygame.transform.scale(pygame.image.load('Resources/o.png'), (BLOCK_SIZE - 2, BLOCK_SIZE - 2))

GRID_REVERSAL = {(0, 2): (0, 0), (1, 2): (0, 1), (2, 2): (0, 2), (0, 1): (1, 0), (1, 1): (1, 1), (2, 1): (1, 2),
                 (0, 0): (2, 0), (1, 0): (2, 1), (2, 0): (2, 2)}

INDICES = {(0, 0): 0, (0, 1): 3, (0, 2): 6, (1, 0): 1, (1, 1): 4, (1, 2): 7, (2, 0): 2, (2, 1): 5, (2, 2): 8}

DEBUG_ENABLED = True

MODEL_FILENAME = 'model.sav'
MODEL_RAW_DATA = 'Resources/tic-tac-toe.data'

FONT_COLOR = (0, 255, 0)
FONT = pygame.font.SysFont('Comic Sans MS', 30)


def text_surface_creator(text):
    return FONT.render(text, False, FONT_COLOR)
