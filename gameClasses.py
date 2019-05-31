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

'''
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

'''
class Player(pygame.sprite.Sprite):
    def __init__(self, playerSpr, direc, controls, name, pos, sz=.5):
        super().__init__()
        self.vel = [0, 0]
        self.pos = pos
        self.hp = 20
        self.direc = 0 if direc == "left" else 1
        self.name = name
        self.speed = 5
        self.jump = 10 #6
        self.airtime = 0.001
        self.time = 0
        self.u = 0

        self.directions = [gameFunctions.loadImage("{0}/left.png".format(playerSpr), sz),
                           gameFunctions.loadImage("{0}/right.png".format(playerSpr), sz)]

        self.controls = controls

        self.image = pygame.image
        self.reImage()

        self.rect = self.image.get_rect()
        self.position()

    def handleKeys(self, key):
        if key[self.controls["jump"]] and self.airtime == 0:
            self.vel[1] = -self.jump
            self.u = -self.jump
            self.airtime = self.time

        if key[self.controls["right"]]:
            self.vel[0] = self.speed
            self.direc = 1
            self.reImage()

        if key[self.controls["left"]]:
            self.vel[0] = -self.speed
            self.direc = 0
            self.reImage()

        if key[self.controls["special1"]]:
            self.spacial1()

        if key[self.controls["special2"]]:
            self.spacial2()

    def spacial1(self):
        pass

    def spacial2(self):
        pass

    def position(self):
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]

    def bounds(self):
        if self.pos[1] <= 0 and self.vel[1] < 0:
            self.airtime = 0.002
            self.u = 0
        elif self.pos[1] >= gameVariables.screenSize[1] - self.rect.size[1] and self.vel[1] > 0:
            self.airtime = 0
            self.u = 0
        for i in range(2):
            if self.pos[i] <= 0 and self.vel[i] < 0:
                self.vel[i] = 0
                self.pos[i] = 0
            elif self.pos[i] >= gameVariables.screenSize[i] - self.rect.size[i] and self.vel[i] > 0:
                self.vel[i] = 0
                self.pos[i] = gameVariables.screenSize[i] - self.rect.size[i]

    def reImage(self):
        image = self.directions[self.direc]
        self.image = pygame.Surface(image.get_size(), pygame.SRCALPHA)
        self.image.blit(image, (0, 0))

        self.rect = self.image.get_rect()

    def update(self, keys, time):
        self.time = time/1000
        self.bounds()
        self.handleKeys(keys)
        self.pos = list(map(lambda x, y: int(x+y), self.pos, self.vel))
        self.vel[0] = gameFunctions.decel(self.vel[0])
        self.position()
        if self.airtime != 0:
            self.airtime += self.time
            self.vel[1] = gameFunctions.gravity(self.u, self.airtime)
