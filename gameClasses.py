import pygame
import random
import gameVariables
from enum import Enum

# Initializing pygame
pygame.init()

# Create a screen called window
window = pygame.display.set_mode((800, 600))

# Title of the game
pygame.display.set_caption("Bullet Rain")


# colors
class Color(Enum):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    PURPLE = (255, 0, 255)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    LIGHT_GRAY = (30, 30, 30)


class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y, img=gameVariables.defBull, xVel=5):
        super().__init__()
        self.x = x
        self.y = y
        self.xVel = xVel
        self.img = img

        self.radius = 10

    def render(self):
        pygame.draw.circle(window, yellow, ((self.x) % 800, self.y), self.radius)
