import pygame
from random import random, randint
import gameVariables
import gameFunctions
from enum import Enum

pygame.font.init()
nams = pygame.font.SysFont("monospace", 20)

# colors
class Color(Enum):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (200, 0, 0)
    YELLOW = (255, 255, 0)
    PURPLE = (255, 0, 255)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 230)
    LIGHT_GRAY = (30, 30, 30)


class Bullets(pygame.sprite.Sprite):
    def __init__(self, img, pos, direc, damage, speed, sz=1.0):
        super().__init__()
        self.pos = list(pos)
        self.vel = [0, 0]
        self.damage = damage
        self.direc = direc  # 0 left, 1 right, 2 down, 3 up

        turnDeg = {0: 180, 1: 0, 2: 270, 3: 90}
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
        self.pos = list(pos)
        self.startpos = pos
        self.hp = gameVariables.player_health
        self.direc = 0 if direc == "left" else 1
        self.name = name
        self.namelength, _ = nams.size(name)
        self.speed = 5
        self.jump = 10  # 6
        self.airtime = self.time = self.u = 0
        self.airjumps = 1
        self.jumptick = 0
        self.offs = [0, 23]

        self.clip = gameVariables.clip_size
        self.reloadTick = 0  # gameVariables.reload_speed
        self.rockNums = 1

        self.fall = True

        self.spacial1tick = self.respawn_tick = 0
        self.doRespawn = False
        self.spacial2tick = gameVariables.rocket_reload

        self.dead = False

        self.directions = [gameFunctions.loadImage("{0}/left.png".format(playerSpr), sz),
                           gameFunctions.loadImage("{0}/right.png".format(playerSpr), sz)]
        self.deadImg = gameFunctions.loadImage("{0}/dead.png".format(playerSpr), sz)

        self.controls = controls

        self.image = pygame.image
        self.rect = pygame.rect
        self.colider = pygame.rect
        self.reImage()

        self.position()

        statsPos = gameFunctions.placeAt((2, 10)) if self.direc == 1 else gameFunctions.placeAt((97, 10))
        self.stats = StatusBars(statsPos, gameFunctions.placeAt((2, 70)),
                                [201, 49, 38, 60], gameVariables.player_health)
        bulletsPos = gameFunctions.placeAt((4.2, 60)) if self.direc == 1 else gameFunctions.placeAt((94.8, 60))
        rocketsPos = gameFunctions.placeAt((6.4, 60)) if self.direc == 1 else gameFunctions.placeAt((92.6, 60))
        self.bulles = StatusBars(bulletsPos, gameFunctions.placeAt((2, 20)),
                                [221, 221, 122, 60], gameVariables.clip_size, True)
        self.rokes = StatusBars(rocketsPos, gameFunctions.placeAt((2, 20)),
                                [53, 186, 135, 60], self.rockNums, True)
        gameVariables.statuss.add(self.stats)
        gameVariables.statuss.add(self.bulles)
        gameVariables.statuss.add(self.rokes)

    def handleKeys(self, key):
        if key[self.controls["jump"]] and self.airjumps > 0 and self.jumptick == 0:  # self.airtime == 0:
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

        if key[self.controls["special1"]] and self.spacial1tick == 0 and self.clip > 0:
            self.spacial1()
            self.spacial1tick = 12
            self.clip = max(0, self.clip - 1)
            self.reloadTick = 0

        if key[self.controls["special2"]] and self.spacial2tick == 250 and self.rockNums > 0:
            self.spacial2()
            self.rockNums = max(0, self.rockNums - 1)
            self.spacial2tick = 0

    def spacial1(self):
        spawnS = self.rect.midright if self.direc == 1 else self.rect.midleft
        bullet = Bullets("bullet.png", (spawnS[0] + self.vel[0], spawnS[1]),
                         self.direc, gameVariables.bullet_damage, gameVariables.bullet_speed, 1.3)
        gameVariables.projectiles.add(bullet)
        # print("bam")

    def spacial2(self):
        spawnS = self.rect.midright if self.direc == 1 else self.rect.midleft
        rocket = Bullets("rocket.png", (spawnS[0] + self.vel[0], spawnS[1]),
                         self.direc, gameVariables.rocket_damage, gameVariables.rocket_speed, 5)
        gameVariables.projectiles.add(rocket)

    def position(self):
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.colider.x = self.pos[0] + self.offs[0]
        self.colider.y = self.pos[1] + self.offs[1]

    def reImage(self, image=None):
        if image is None:
            image = self.directions[self.direc]
        if image.get_size()[0] < self.namelength:
            self.offs[0] = (self.namelength - image.get_size()[0]) / 2
        bonds = [max(self.namelength, image.get_size()[0]),
                 image.get_size()[1] + self.offs[1]]
        self.image = pygame.Surface(bonds, pygame.SRCALPHA)
        self.image.blit(image, self.offs)
        gameFunctions.print_text(nams, bonds[0] / 2 - self.namelength / 2, 0, self.name, Color.WHITE, self.image)

        self.rect = self.image.get_rect()
        self.colider = image.get_rect()
        self.position()

    def colideIn(self):
        saf = 13
        self.position()
        coordsX = self.colider.topright if self.vel[0] > 0 else self.colider.topleft
        coordsY = self.colider.bottomleft if self.vel[1] > 0 else self.colider.topleft

        xSide = False if self.vel[0] > 0 else True
        ySide = False if self.vel[1] > 0 else True

        colliders = [pygame.Rect(coordsX[0], coordsX[1] + saf, self.vel[0], self.colider.h - saf * 2),
                     pygame.Rect(int(coordsY[0] + saf / 2), coordsY[1], self.colider.w - saf, self.vel[1])]

        flors = gameFunctions.drawRectangle((self.colider.bottomleft[0] + 5, self.colider.bottomleft[1]),
                                            (self.colider.bottomright[0] - 5, self.colider.bottomright[1] + 1), False)

        """
        #for testing purposes
        for scan in colliders:
            if scan.w == 0 or scan.h == 0:
                continue
            else:
                pygame.draw.rect(gameVariables.scr, [63, 64, 65], scan)
            pygame.draw.rect(gameVariables.scr, [255, 255, 255], flors)
        """

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
                self.airtime = 0.001
                self.u = 0

            if flors.colliderect(obstecles):
                self.airjumps = 1
                self.fall = False
        self.position()

    def gotHit(self):
        for projectile in gameVariables.projectiles:
            if self.colider.colliderect(projectile.rect):
                self.hp -= projectile.damage
                projectile.kill()

    def life(self):
        if self.hp <= 0:
            openet = gameVariables.player_list.opponent(self.name)
            curr = gameVariables.player_list.playerScore(openet)
            gameVariables.player_list.playerScore(openet, curr + 1)
            self.clip = gameVariables.clip_size
            self.spacial1tick = 0

            self.clip = gameVariables.clip_size
            self.reloadTick = 0
            self.spacial2tick = gameVariables.rocket_reload
            self.rockNums = 1

            self.reImage(self.deadImg)
            self.dead = True

        '''if gameVariables.score[self.name] <= 0:
            self.kill()'''

    def update(self, keys, time):
        self.stats.update(self.hp)
        if self.clip > 0:
            self.bulles.update(self.clip)
        else:
            self.bulles.update(self.reloadTick / gameVariables.reload_speed * gameVariables.clip_size)

        if self.rockNums > 0:
            self.rokes.update(self.rockNums)
        else:
            self.rokes.update(self.spacial2tick / gameVariables.rocket_reload)

        if not self.dead:
            self.time = time / 1000
            self.fall = True
            self.handleKeys(keys)

            self.colideIn()

            self.pos = list(map(lambda x, y: int(x + y), self.pos, self.vel))
            self.vel[0] = gameFunctions.decel(self.vel[0])

            self.colideIn()

            self.position()

            self.jumptick = max(0, self.jumptick - 1)
            self.spacial1tick = max(0, self.spacial1tick - 1)

            self.gotHit()
            self.life()

            if self.fall:
                self.airtime += self.time
                self.vel[1] = gameFunctions.gravity(self.u, self.airtime)

            if self.clip == 0:
                self.reloadTick = min(gameVariables.reload_speed, self.reloadTick + 1)

            if self.rockNums == 0:
                self.spacial2tick = min(250, self.spacial2tick + 1)

            if self.spacial2tick == gameVariables.rocket_reload:
                self.rockNums = 1

            if self.reloadTick == gameVariables.reload_speed:
                self.clip = gameVariables.clip_size

        elif not self.doRespawn:  #  elif keys[gameVariables.revive_key] and not self.doRespawn:
            self.respawn_tick = 0
            self.doRespawn = True

        regenWait = 75
        if self.doRespawn and self.respawn_tick == regenWait:
            self.respawn()
            self.doRespawn = False

        if self.doRespawn:
            self.hp = self.respawn_tick / regenWait * gameVariables.player_health

        self.respawn_tick = min(regenWait, self.respawn_tick + 1)

    def respawn(self):
        self.dead = False
        self.reImage()
        self.hp = gameVariables.player_health
        self.pos = list(self.startpos)


class StatusBars(pygame.sprite.Sprite):
    def __init__(self, pos, size, color, maxVl, beck=False, revs=True):
        super().__init__()
        self.color = color
        self.val = 0
        self.revs = revs
        self.max = maxVl
        self.image = pygame.Surface(size, pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.beck = beck
        self.draw()

    def draw(self):
        self.image.fill([0, 0, 0, 0])
        backroundC = list(map(lambda x: max(0, x - 70), self.color))
        hight = self.val * self.rect.h / self.max
        req = pygame.Rect(0, hight, *self.rect.size)
        self.color[3] = 150
        backroundC[3] = 150
        if self.beck:
            self.image.fill(backroundC)
        pygame.draw.rect(self.image, self.color, req)

    def update(self, val):
        if self.revs:
            self.val = val * -1 + self.max
        else:
            self.val = val
        self.draw()


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


class RebindButton:
    def __init__(self, key, player):
        pass


class Button(pygame.sprite.Sprite):
    def __init__(self, message, pos, size, colors, font, deful=0, func=lambda: True):
        super().__init__()
        self.font = font
        self.message = message
        self.colors = colors
        self.curr_color = deful
        self.size = size
        self.function = func
        self.image = pygame.Surface(size, pygame.SRCALPHA)
        self.mouse = pygame.mouse
        gameVariables.butonRel.add(self)
        self.rlsd = False

        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def relase(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.rlsd = True

    def messageSprite(self, col=Color.WHITE.value):
        self.image.fill(self.colors[self.curr_color])
        xTx, yTx = self.font.size(self.message)
        xTx = self.size[0] / 2 - xTx / 2
        yTx = self.size[1] / 2 - yTx / 2

        text_image = self.font.render(self.message, True, col)
        self.image.blit(text_image, (xTx, yTx))

    def flagColor(self):
        self.curr_color = gameFunctions.flag(0, 1, self.curr_color)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, mouse, accept):
        self.mouse = mouse
        if accept:
            if self.rect.collidepoint(mouse.get_pos()):
                self.flagColor()
                self.messageSprite()
                return self.function()
        self.messageSprite()


class MultipleOptions(pygame.sprite.Group):
    def __init__(self, objects):
        super().__init__()
        self.items = objects
        self.selections = dict()
        for i in objects:
            self.add(i)
        self.updateList()
        for i in self.sprites():
            i.update([0, 0], False)

    def updateList(self):
        for i in self.items:
            self.selections[i.message] = bool(i.curr_color)

    def selectOne(self, pressed):
        for i in self.items:
            if i.message != pressed:
                i.curr_color = 0
        self.updateList()

    def update(self, mouse, accept):
        #if accept:
        for j in self.items:
            if not self.selections[j.message]:
                if j.update(mouse, accept):
                    self.selectOne(j.message)

        return self.selections


class ClickButton(Button):
    def __init__(self, message, pos, size, colors, font, func=lambda: True):
        super().__init__(message, pos, size, colors, font, func=func)

    def update(self, mouse, accept):
        self.mouse = mouse
     #   if accept:
        if self.rect.collidepoint(mouse.get_pos()):
            if self.mouse.get_pressed()[0]:
                self.curr_color = 1
                self.messageSprite()
            if self.rlsd:
                self.rlsd = False
                return self.function()
        if not self.mouse.get_pressed()[0] or not self.rect.collidepoint(mouse.get_pos()):
            self.curr_color = 0
        self.messageSprite()


class ClickRelese:
    def __init__(self):
        self.monitor = list()

    def gotClicked(self):
        for i in self.monitor:
            i.relase()

    def add(self, act):
        self.monitor.append(act)


gameVariables.butonRel = ClickRelese()


class RainDrop:
    def __init__(self, tick, drop):
        self.tick = tick
        self.drop = drop

    def update(self):
        self.tick = max(0, self.tick-1)
        if self.tick == 0:
            gameVariables.projectiles.add(self.drop)
            return True
        return False


class Rain:
    def __init__(self):
        self.rainDrops = list()
        self.doRain = False

    def update(self):
        if self.doRain:
            for j, i in reversed(list(enumerate(self.rainDrops))):
                if i.update():
                    self.rainDrops.pop(j)

        if self.rainDrops == list():
            self.doRain = False


gameVariables.raining = Rain()


def makeItRain():
    rain_amount = gameVariables.rain_amount
    number = randint(rain_amount-5, rain_amount+5)
    print(number)
    for i in range(number):
        waitAm = randint(0, 25)
        proj = Bullets("bullet.png", (round(random()*gameVariables.screenSize[0]), 1), 2,
                       gameVariables.bullet_damage, gameVariables.bullet_speed, 1.3)
        drop = RainDrop(waitAm, proj)
        gameVariables.raining.rainDrops.append(drop)
    gameVariables.raining.doRain = True
