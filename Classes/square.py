from Resources import constants
import pygame


class square:
    x, y = -1, -1
    rectangle = None
    border = None
    symbol_value = None

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rectangle = pygame.Rect(x, y, constants.RECTANGLE_X, constants.RECTANGLE_Y)
        self.border = []
        self.border.append(((self.x, self.y), (self.x, self.y + constants.BLOCK_SIZE)))
        self.border.append(((self.x + constants.BLOCK_SIZE, self.y),
                           (self.x + constants.BLOCK_SIZE, self.y + constants.BLOCK_SIZE)))
        self.border.append(((self.x, self.y), (self.x + constants.BLOCK_SIZE, self.y)))
        self.border.append(((self.x, self.y + constants.BLOCK_SIZE),
                           (self.x + constants.BLOCK_SIZE, self.y + constants.BLOCK_SIZE)))
        self.symbol_value = None

    def return_empty_rectangle(self):
        return self.rectangle

