import pygame
import random
import gameVariables
import gameFunctions
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
        pygame.draw.circle(window, Color.YELLOW, ((self.x) % 800, self.y), self.radius)


class Player(pygame.sprite.Sprite):
    def __init__(self, img, controls, name, pos, sz=.5):
        super().__init__()
        self.vel = [0, 0]
        self.pos = pos
        self.hp = 20
        self.name = name
        self.speed = 5

        self.controls = controls

        img = gameFunctions.loadImage("sprites/{}".format(img), sz)
        self.image = pygame.Surface(img.get_size(), pygame.SRCALPHA)
        self.image.blit(img, (0, 0))

        self.rect = self.image.get_rect()
        self.position()

    def handleKeys(self, key):
        for j, i in enumerate(self.controls):
            if key[i]:
                if j == 0:
                    self.vel[1] = -self.speed
                elif j == 1:
                    self.vel[1] = self.speed
                elif j == 2:
                    self.vel[0] = self.speed
                elif j == 3:
                    self.vel[0] = -self.speed
                elif j == 4:
                    self.spacial1()
                elif j == 5:
                    self.spacial2()

    def spacial1(self):
        pass

    def spacial2(self):
        pass

    def position(self):
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]

    def bounds(self):
        for i in range(2):
            if self.pos[i] <= 0 and self.vel[i] < 0:
                self.vel[i] = 0
            elif self.pos[i] >= gameVariables.screenSize[i] - self.rect.size[i] and self.vel[i] > 0:
                self.vel[i] = 0

    def update(self, keys):
        self.bounds()
        self.pos = list(map(lambda x, y: int(x+y), self.pos, self.vel))
        self.vel = list(map(gameFunctions.decel, self.vel))
        self.handleKeys(keys)
        self.position()
