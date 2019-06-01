import pygame
import random
import gameVariables
import gameFunctions
from enum import Enum

pygame.font.init()
nams = pygame.font.SysFont("monospace", 20)


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
    def __init__(self, x, y,direc, img ,xVel=5, ):
        super().__init__()
        self.x = x
        self.y = y
        self.xVel = xVel
        self.img = img
        self.direc = 0 if direc == "left" else 1
        self.radius = 10

    def render(self):
        pygame.draw.circle(window, Color.YELLOW, ((self.x) % 800, self.y), self.radius)

####################################****#################################************************








#######################################################################################

class Player(pygame.sprite.Sprite):
    def __init__(self, playerSpr, direc, controls, name, pos, sz=.25):
        super().__init__()
        self.vel = [0, 0]
        self.pos = pos
        self.hp = 20
        self.direc = 0 if direc == "left" else 1
        self.name = name
        self.namelength, _ = nams.size(name)
        self.speed = 5
        self.jump = 10 #6
        self.airtime = 0
        self.time = 0
        self.u = 0
        self.airjumps = 2
        self.jumptick = 0
        self.offs = [0, 23]

        self.spacial1tick = 0
        self.spacial2tick = 0

        self.directions = [gameFunctions.loadImage("{0}/left.png".format(playerSpr), sz),
                           gameFunctions.loadImage("{0}/right.png".format(playerSpr), sz)]

        self.controls = controls

        self.image = pygame.image
        self.rect = pygame.rect
        self.colider = pygame.rect
        self.reImage()

        self.position()

    def handleKeys(self, key):
        if key[self.controls["jump"]] and self.airjumps > 0 and self.jumptick == 0: #self.airtime == 0:
            self.vel[1] = -self.jump
            self.u = -self.jump
        #    print(self.airjumps)
            self.airtime = self.time
            self.jumptick = 18
            if self.airtime > 0:
                self.airjumps -= 1

        if key[self.controls["right"]]:
            self.vel[0] = self.speed
            self.direc = 1
            self.reImage()

        if key[self.controls["left"]]:
            self.vel[0] = -self.speed
            self.direc = 0
            self.reImage()

        if key[self.controls["sneak"]]:
            pass

        if key[self.controls["special1"]] and self.spacial1tick == 0:
            self.spacial1()
            self.spacial1tick = 10

        if key[self.controls["special2"]] and self.spacial2tick == 0:
            self.spacial2()
            self.spacial2tick = 100

    def spacial1(self):
        pass

    def spacial2(self):
        pass

    def position(self):
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.colider.x = self.pos[0] + self.offs[0]
        self.colider.y = self.pos[1] + self.offs[1]

    def bounds(self):
        if self.pos[0] < 0 and self.vel[0] < 0:
            self.collisions("left", 0)

        elif self.pos[1] < 0 - self.offs[1] and self.vel[1] < 0:
            self.collisions("up", 0)

        elif self.pos[0] > gameVariables.screenSize[0] - self.colider.size[0] - self.offs[0] and self.vel[0] > 0:
            self.collisions("right", gameVariables.screenSize[0])

        elif self.pos[1] > gameVariables.screenSize[1] - self.rect.size[1] and self.vel[1] > 0:
            self.collisions("down", gameVariables.screenSize[1])

    def collisions(self, direct, loc):
        if direct == "up":
            self.vel[1] = 0
            self.pos[1] = loc - self.offs[1]
            self.airtime = 0
            self.u = 0

        elif direct == "down":
            self.vel[1] = 0
            self.pos[1] = loc - self.rect.h+1
            self.airtime = 0
            self.u = 0
            self.airjumps = 2

        elif direct == "right":
            self.vel[0] = 0
            self.pos[0] = loc - self.colider.w - self.offs[0]

        elif direct == "left":
            self.vel[0] = 0
            self.pos[0] = loc - self.offs[0]

    def reImage(self):
        image = self.directions[self.direc]
        if image.get_size()[0] < self.namelength:
            self.offs[0] = (self.namelength-image.get_size()[0])/2
        bonds = [max(self.namelength, image.get_size()[0]),
                 image.get_size()[1]+self.offs[1]]
        self.image = pygame.Surface(bonds, pygame.SRCALPHA)
        self.image.blit(image, self.offs)
        gameFunctions.print_text(nams, 0, 0, self.name, Color.WHITE, self.image)

        self.rect = self.image.get_rect()
        self.colider = image.get_rect()

    def update(self, keys, time):
        self.time = time/1000
        fall = True
        for i in gameVariables.obstecls:
            colisions = gameFunctions.colideDir(self.colider, i)
            if colisions is not None:
                self.collisions(colisions[0], colisions[1])
                if colisions[0] == "down":
                    fall = False
        self.bounds()
        self.handleKeys(keys)
        self.pos = list(map(lambda x, y: int(x+y), self.pos, self.vel))
        self.vel[0] = gameFunctions.decel(self.vel[0])
        self.position()

        self.jumptick = max(0, self.jumptick - 1)
        self.spacial1tick = max(0, self.spacial1tick - 1)
        self.spacial2tick = max(0, self.spacial2tick - 1)

        if fall:
            self.airtime += self.time
            self.vel[1] = gameFunctions.gravity(self.u, self.airtime)
