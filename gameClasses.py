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
    def __init__(self, img, pos, direc, damage, speed, sz=1.0):
        super().__init__()
        self.pos = list(pos)
        self.vel = [0, 0]
        self.damage = damage
        self.direc = direc  # 0 left, 1 right, 2 down, 3 up

        turnDeg = {0: 180, 1: 0, 2: 90, 3: 270}
        self.image = gameFunctions.loadImage("projectiles/{0}".format(img), sz, turnDeg[direc])
        self.rect = self.image.get_rect()


        if direc == 0:
            self.vel = [-speed, 0]
            self.pos[0] -= self.rect.w
        elif direc == 1:
            self.vel = [speed, 0]
        elif direc == 2:
            self.vel = [0, speed]
        elif direc == 3:
            self.vel = [0, -speed]
            self.pos[1] -= self.rect.h

        self.position()

    def collide(self):
        for obstecles in gameVariables.obstecls:
            if self.rect.colliderect(obstecles):
                self.kill()

    def position(self):
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]

    def update(self):
        self.pos = list(map(lambda x, y: int(x + y), self.pos, self.vel))
        self.collide()
        self.position()



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

        self.fall = True

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
            if self.direc != 1:
                self.direc = 1
                self.reImage()

        if key[self.controls["left"]]:
            self.vel[0] = -self.speed
            if self.direc != 0:
                self.direc = 0
                self.reImage()

        if key[self.controls["sneak"]]:
            self.speed = 2
            self.jump = 5
        else:
            self.speed = 5
            self.jump = 10

        if key[self.controls["special1"]] and self.spacial1tick == 0:
            self.spacial1()
            self.spacial1tick = 20

        if key[self.controls["special2"]] and self.spacial2tick == 0:
            self.spacial2()
            self.spacial2tick = 10000

    def spacial1(self):
        spawnS = self.rect.midright if self.direc == 1 else self.rect.midleft
        bullet = Bullets("bullet.png", spawnS, self.direc, 5, 20, 1.4)
        gameVariables.projectiles.add(bullet)
        #print("bam")

    def spacial2(self):
        pass

    def position(self):
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.colider.x = self.pos[0] + self.offs[0]
        self.colider.y = self.pos[1] + self.offs[1]

    def reImage(self):
        image = self.directions[self.direc]
        if image.get_size()[0] < self.namelength:
            self.offs[0] = (self.namelength-image.get_size()[0])/2
        bonds = [max(self.namelength, image.get_size()[0]),
                 image.get_size()[1]+self.offs[1]]
        self.image = pygame.Surface(bonds, pygame.SRCALPHA)
        self.image.blit(image, self.offs)
        gameFunctions.print_text(nams, bonds[0]/2-self.namelength/2, 0, self.name, Color.WHITE, self.image)

        self.rect = self.image.get_rect()
        self.colider = image.get_rect()

    def colideIn(self):
        saf = 10

        coordsX = self.colider.topright if self.vel[0] > 0 else self.colider.topleft
        coordsY = self.colider.bottomleft if self.vel[1] > 0 else self.colider.topleft

        xSide = False if self.vel[0] > 0 else True
        ySide = False if self.vel[1] > 0 else True

        xF = -1 if xSide else 1
        yF = -1 if ySide else 1

        colliders = [pygame.Rect(coordsX[0], coordsX[1] + saf, self.vel[0], self.colider.h - saf*2),
                     pygame.Rect(coordsY[0] + saf, coordsY[1], self.colider.w - saf*2, self.vel[1])]

        flors = gameFunctions.drawRectangle((self.colider.bottomleft[0]+saf, self.colider.bottomleft[1]),
                                            (self.colider.bottomright[0]-saf, self.colider.bottomright[1] + 1), False)

        '''
        #for testing purposes
        for scan in colliders:
            if scan.w == 0 or scan.h == 0:
                continue
            else:
                pygame.draw.rect(gameVariables.scr, [63, 64, 65], scan)
        '''
        for obstecles in gameVariables.obstecls:
            if colliders[0].colliderect(obstecles) and colliders[0].w != 0:
                offSide = 0 if xSide else self.colider.w
                wallAt = obstecles.midright[0] if xSide else obstecles.midleft[0]
                self.vel[0] = 0
                self.pos[0] = wallAt - offSide - self.offs[0]

            if colliders[1].colliderect(obstecles) and colliders[1].h != 0:
                offSide = 0 if ySide else self.colider.h
                wallAt = obstecles.midbottom[1] if ySide else obstecles.midtop[1]
                self.vel[1] = 0
                self.pos[1] = wallAt - offSide - self.offs[1]
                self.airtime = 0
                self.u = 0

            if flors.colliderect(obstecles):
                self.airjumps = 2
                self.fall = False
        self.position()

    def gotHit(self):
        for projectile in gameVariables.projectiles:
            if self.colider.colliderect(projectile.rect):
                self.hp -= projectile.damage
                projectile.kill()

    def life(self):
        if self.hp <= 0:
            self.hp = 20
            openet = gameVariables.player_list.opponent(self.name)
            curr = gameVariables.player_list.playerScore(openet)
            gameVariables.player_list.playerScore(openet, curr+1)

        '''if gameVariables.score[self.name] <= 0:
            self.kill()'''

    def update(self, keys, time):
        self.time = time/1000
        self.fall = True
        self.colideIn()
        self.handleKeys(keys)

        self.pos = list(map(lambda x, y: int(x+y), self.pos, self.vel))
        self.vel[0] = gameFunctions.decel(self.vel[0])

        self.position()

        self.jumptick = max(0, self.jumptick - 1)
        self.spacial1tick = max(0, self.spacial1tick - 1)
        self.spacial2tick = max(0, self.spacial2tick - 1)

        self.gotHit()
        self.life()

        if self.fall:
            self.airtime += self.time
            self.vel[1] = gameFunctions.gravity(self.u, self.airtime)


class StatusBars:
    def __init__(self):
        pass


class PlayerList:
    def __init__(self, player1, player2, scoreStart=0):
        self.player1 = player1
        self.player2 = player2
        self.score = [scoreStart, scoreStart]

    def __getitem__(self, val):
        if val == 0:
            return self.player1
        else:
            return self.player2

    def __getattr__(self, item):
        if item == "list":
            return {self.player1: self.score[0], self.player2: self.score[1]}
        else:
            if isinstance(self, item):
                return self.item

    def opponent(self, player):
        return {self.player2: self.player1,
                self.player1: self.player2}[player]

    def index(self, player):
        return {self.player1: 0,
                self.player2: 1}[player]

    def playerScore(self, player, setTo=None):
        if setTo is not None:
            self.score[self.index(player)] = setTo
        else:
            return self.score[self.index(player)]
