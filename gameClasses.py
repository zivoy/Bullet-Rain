# imports
import pygame
from random import random, randint
import gameVariables
import settings
import gameFunctions
from enum import Enum

# init and declare a font for names
pygame.font.init()
nams = pygame.font.SysFont("monospace", 20)


# Class that stores colors to make sure all colors are the same
class Color(Enum):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (200, 0, 0)
    YELLOW = (255, 255, 0)
    PURPLE = (255, 0, 255)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 230)
    LIGHT_GRAY = (30, 30, 30)
    GOLD = (185, 191, 21)


# Class that handles projectiles
class Bullets(pygame.sprite.Sprite):
    def __init__(self, img, pos, direc, damage, speed, sz=1.0):
        super().__init__()
        self.pos = list(pos)  # initial position
        self.vel = [0, 0]  # projectiles velocity
        self.damage = damage  # damage that projectile deals
        self.direc = direc  # 0 left, 1 right, 2 down, 3 up

        # load image
        turnDeg = {0: 180, 1: 0, 2: 270, 3: 90}
        self.image = gameFunctions.loadImage("projectiles/{0}".format(img), sz, turnDeg[direc])
        self.rect = self.image.get_rect()

        # set velocity
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

        # set position of projectile
        self.position()

    # checks for collision with obstacles
    def collide(self):
        for obstecles in gameVariables.obstecls:
            if self.rect.colliderect(obstecles):
                self.kill()

    # set the position of rect to the pos
    def position(self):
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]

    # update function
    def update(self):
        # apply velocity to position
        self.pos = list(map(lambda x, y: int(x + y), self.pos, self.vel))
        # check for collisions
        self.collide()
        # update position
        self.position()


#######################################################################################


# player class
class Player(pygame.sprite.Sprite):
    def __init__(self, playerSpr, direc, controls, name, pos, sz=.25):
        super().__init__()
        # player variables
        # velocity and position
        self.vel = [0, 0]
        self.pos = list(pos)
        self.startpos = pos

        # hp and name
        self.hp = gameVariables.player_health
        self.direc = 0 if direc == "left" else 1
        self.name = name
        self.namelength, _ = nams.size(name)

        # speed and jump power
        self.speed = 5 * gameVariables.screenSize[0] / 1250
        self.jump = 10 * gameVariables.screenSize[1] / 800
        self.airtime = self.time = self.u = 0
        self.airjumps = 1
        self.jumptick = 0
        self.offs = [0, 23]

        # ammo
        self.clip = gameVariables.clip_size
        self.reloadTick = 0  # gameVariables.reload_speed
        self.rockNums = 1

        # gravity
        self.fall = True

        # timers
        self.spacial1tick = self.respawn_tick = 0
        self.doRespawn = False
        self.spacial2tick = gameVariables.rocket_reload

        # is dead
        self.dead = False

        # player images
        self.directions = [gameFunctions.loadImage("{0}/left.png".format(playerSpr), sz),
                           gameFunctions.loadImage("{0}/right.png".format(playerSpr), sz)]
        self.deadImg = gameFunctions.loadImage("{0}/dead.png".format(playerSpr), sz)

        # controls
        self.controls = controls

        # image
        self.image = pygame.image
        self.rect = pygame.rect
        self.colider = pygame.rect
        self.reImage()

        # position
        self.position()

        # hp and ammo bars
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

    # key handler
    def handleKeys(self, key):
        # handler for jump key
        if key[self.controls["jump"]] and self.airjumps > 0 and self.jumptick == 0:  # self.airtime == 0:
            self.vel[1] = -self.jump
            self.u = -self.jump
            #    print(self.airjumps)
            self.airtime = self.time
            self.jumptick = 18
            if self.airtime > 0:
                self.airjumps -= 1

        # handler fot moving right
        if key[self.controls["right"]]:
            self.vel[0] = self.speed
            if self.direc != 1:
                self.direc = 1
                self.reImage()

        # handler for moving left
        if key[self.controls["left"]]:
            self.vel[0] = -self.speed
            if self.direc != 0:
                self.direc = 0
                self.reImage()

        # handler for sneaking
        if key[self.controls["sneak"]]:
            self.speed = 2 * gameVariables.screenSize[0] / 1250
            self.jump = 5 * gameVariables.screenSize[1] / 800
        else:
            self.speed = 5 * gameVariables.screenSize[0] / 1250
            self.jump = 10 * gameVariables.screenSize[1] / 800

        # handler for bullets
        if key[self.controls["special1"]] and self.spacial1tick == 0 and self.clip > 0:
            self.spacial1()
            self.spacial1tick = 12
            self.clip = max(0, self.clip - 1)
            self.reloadTick = 0

        # handler for rockets
        if key[self.controls["special2"]] and self.spacial2tick == 250 and self.rockNums > 0:
            self.spacial2()
            self.rockNums = max(0, self.rockNums - 1)
            self.spacial2tick = 0

    # attack 1 bullet
    def spacial1(self):
        # spawn direction
        spawnS = self.rect.midright if self.direc == 1 else self.rect.midleft
        # make bullet and add to projectile sprite class
        bullet = Bullets("bullet.png", (spawnS[0] + self.vel[0], spawnS[1]),
                         self.direc, gameVariables.bullet_damage, gameVariables.bullet_speed, gameVariables.bull_size)
        gameVariables.projectiles.add(bullet)
        # print("bam")

    # attack 2 rocket
    def spacial2(self):
        # spawn direction
        spawnS = self.rect.midright if self.direc == 1 else self.rect.midleft
        # spawn rocket and add to projectile class
        rocket = Bullets("rocket.png", (spawnS[0] + self.vel[0], spawnS[1]),
                         self.direc, gameVariables.rocket_damage, gameVariables.rocket_speed, gameVariables.roke_size)
        gameVariables.projectiles.add(rocket)

    # set position of the player from cord
    def position(self):
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.colider.x = self.pos[0] + self.offs[0]
        self.colider.y = self.pos[1] + self.offs[1]

    # change the player image
    def reImage(self, image=None):
        # if no image was specified set the image as the side
        if image is None:
            image = self.directions[self.direc]
        # if the name is bigger then the sprite image create an offset
        if image.get_size()[0] < self.namelength:
            self.offs[0] = (self.namelength - image.get_size()[0]) / 2
        # set the size as ths the bigger one in case the name is smaller then the image
        bonds = [max(self.namelength, image.get_size()[0]),
                 image.get_size()[1] + self.offs[1]]
        # set the image as an empty surface and blit image and name
        self.image = pygame.Surface(bonds, pygame.SRCALPHA)
        self.image.blit(image, self.offs)
        gameFunctions.print_text(nams, bonds[0] / 2 - self.namelength / 2, 0, self.name, Color.WHITE, self.image)

        # get rect and collider rect
        self.rect = self.image.get_rect()
        self.colider = image.get_rect()
        # set position
        self.position()

    # handles collisions of player
    def colideIn(self):
        # safe zone for no conflicts in collider
        saf = 13 * round(gameVariables.screenSize[1] / 800)
        # update position and get the starting coords for colliders
        self.position()
        coordsX = self.colider.topright if self.vel[0] > 0 else self.colider.topleft
        coordsY = self.colider.bottomleft if self.vel[1] > 0 else self.colider.topleft

        # determine side of collider
        xSide = False if self.vel[0] > 0 else True
        ySide = False if self.vel[1] > 0 else True

        # create x and y colliders
        colliders = [pygame.Rect(coordsX[0], coordsX[1] + saf, self.vel[0], self.colider.h - saf * 2),
                     pygame.Rect(int(coordsY[0] + saf / 2), coordsY[1], self.colider.w - saf, self.vel[1])]

        # create a colider for gravity
        flors = gameFunctions.drawRectangle((self.colider.bottomleft[0] + 5, self.colider.bottomleft[1]),
                                            (self.colider.bottomright[0] - 5, self.colider.bottomright[1] + 1), False)

        # this part displays the colliders for testing purposes
        """
        #for testing purposes
        for scan in colliders:
            if scan.w == 0 or scan.h == 0:
                continue
            else:
                pygame.draw.rect(gameVariables.scr, [63, 64, 65], scan)
            pygame.draw.rect(gameVariables.scr, [255, 255, 255], flors)
        """

        # for every obstacle test for collision
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

            # check if touching ground
            if flors.colliderect(obstecles):
                self.airjumps = 1
                self.fall = False
        # update position
        self.position()

    # checks if player got hit by any projectile
    def gotHit(self):
        for projectile in gameVariables.projectiles:
            if self.colider.colliderect(projectile.rect):
                self.hp -= projectile.damage
                projectile.kill()

    # check if player died and increase score for opponent
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

    # update function
    def update(self, keys, time):
        # update hp bar
        self.stats.update(self.hp)
        # if not out of ammo update ammo bar else reload bar
        if self.clip > 0:
            self.bulles.update(self.clip)
        else:
            self.bulles.update(self.reloadTick / gameVariables.reload_speed * gameVariables.clip_size)

        # if rocket not fired update bar else reload
        if self.rockNums > 0:
            self.rokes.update(self.rockNums)
        else:
            self.rokes.update(self.spacial2tick / gameVariables.rocket_reload)

        # if player not dead
        if not self.dead:
            # update player time
            self.time = time / 1000
            # assume player is falling
            self.fall = True
            # handle keys
            self.handleKeys(keys)

            # handle collisions
            self.colideIn()

            # update position and velocity
            self.pos = list(map(lambda x, y: int(x + y), self.pos, self.vel))
            self.vel[0] = gameFunctions.decel(self.vel[0])

            # handle collisons again
            self.colideIn()

            # decrease jump tick and attack 1 tick
            self.jumptick = max(0, self.jumptick - 1)
            self.spacial1tick = max(0, self.spacial1tick - 1)

            # check if player got hit or is dead
            self.gotHit()
            self.life()

            # if the player is falling accelerate it
            if self.fall:
                self.airtime += self.time
                self.vel[1] = gameFunctions.gravity(self.u, self.airtime)

            # if out of ammo start reload timer
            if self.clip == 0:
                self.reloadTick = min(gameVariables.reload_speed, self.reloadTick + 1)

            # if out of rockets start reload timer
            if self.rockNums == 0:
                self.spacial2tick = min(250, self.spacial2tick + 1)

            # if rocket reload timer is done reload rockets
            if self.spacial2tick == gameVariables.rocket_reload:
                self.rockNums = 1

            # if ammo reload timer is done reload bullets
            if self.reloadTick == gameVariables.reload_speed:
                self.clip = gameVariables.clip_size

        # start respawn timer if dead
        elif not self.doRespawn:
            self.respawn_tick = 0
            self.doRespawn = True

        # respawn delay
        regenWait = 75

        # if respawn timer is done respawn
        if self.doRespawn and self.respawn_tick == regenWait:
            self.respawn()
            self.doRespawn = False

        # regen hp if dead
        if self.doRespawn:
            self.hp = self.respawn_tick / regenWait * gameVariables.player_health

        # increase respawn tick
        self.respawn_tick = min(regenWait, self.respawn_tick + 1)

    # respawn function
    def respawn(self):
        self.dead = False
        self.reImage()
        self.hp = gameVariables.player_health
        self.pos = list(self.startpos)


# class for creating status bars
class StatusBars(pygame.sprite.Sprite):
    def __init__(self, pos, size, color, maxVl, beck=False, revs=True):
        super().__init__()
        self.color = color  # color of bar
        self.val = 0  # value
        self.revs = revs  # reverse direction
        self.max = maxVl  # max possible value
        self.image = pygame.Surface(size, pygame.SRCALPHA)  # create surface
        self.rect = self.image.get_rect()  # get rect of surface
        self.rect.topleft = pos  # set position of rect
        self.beck = beck  # render back
        self.draw()  # draw bar on surface

    # function for drawing bar
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

    # update bar and draw it
    def update(self, val):
        if self.revs:
            self.val = val * -1 + self.max
        else:
            self.val = val
        self.draw()


# function that keeps player name and score
class PlayerList:
    def __init__(self, player1, player2, scoreStart=0):
        self.player1 = player1  # player 1 name
        self.player2 = player2  # player 2 name
        self.score = [scoreStart, scoreStart]  # player scores

    # return name from id
    def __getitem__(self, val):
        if val == 0:
            return self.player1
        else:
            return self.player2

    # if .list is added to the end it returns dict with names and scores
    def __getattr__(self, item):
        if item == "list":
            return {self.player1: self.score[0], self.player2: self.score[1]}
        else:
            if isinstance(self, item):
                return self.item

    # returns opponent given name
    def opponent(self, player):
        return {self.player2: self.player1,
                self.player1: self.player2}[player]

    # returns id given name
    def index(self, player):
        return {self.player1: 0,
                self.player2: 1}[player]

    # set/get score given name
    def playerScore(self, player, setTo=None):
        if setTo is not None:
            self.score[self.index(player)] = setTo
        else:
            return self.score[self.index(player)]


# unfinished callas for buttons for rebinding keys
class RebindButton:
    def __init__(self, key, player):
        pass


# toggle button class
class Button(pygame.sprite.Sprite):
    def __init__(self, message, pos, size, colors, font, deful=0, func=lambda: True):
        super().__init__()
        # button variables
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

    # checks for when click was released
    def relase(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.rlsd = True

    # draw button surface
    def messageSprite(self, col=Color.WHITE.value):
        self.image.fill(self.colors[self.curr_color])
        xTx, yTx = self.font.size(self.message)
        xTx = self.size[0] / 2 - xTx / 2
        yTx = self.size[1] / 2 - yTx / 2

        text_image = self.font.render(self.message, True, col)
        self.image.blit(text_image, (xTx, yTx))

    # toggle the color of button
    def flagColor(self):
        self.curr_color = gameFunctions.flag(0, 1, self.curr_color)

    # draw button on screen
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    # update button
    def update(self, mouse, accept):
        self.mouse = mouse
        # check for click
        if accept:
            if self.rect.collidepoint(mouse.get_pos()):
                self.flagColor()
                self.messageSprite()
                return self.function()
        self.messageSprite()


# class for handling multiple choice buttons
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

    # make a updates list of the state of each button
    def updateList(self):
        for i in self.items:
            self.selections[i.message] = bool(i.curr_color)

    # make sure only one button is selected
    def selectOne(self, pressed):
        for i in self.items:
            if i.message != pressed:
                i.curr_color = 0
        self.updateList()

    # update all buttons
    def update(self, mouse, accept):
        # if accept:
        for j in self.items:
            if not self.selections[j.message]:
                if j.update(mouse, accept):
                    self.selectOne(j.message)

        return self.selections


# class for click buttons
class ClickButton(Button):
    def __init__(self, message, pos, size, colors, font, func=lambda: True):
        super().__init__(message, pos, size, colors, font, func=func)

    # handles clicks on button
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


# class for handling the release of mouse
class ClickRelese:
    def __init__(self):
        self.monitor = list()

    # activates button on release
    def gotClicked(self):
        for i in self.monitor:
            i.relase()

    # add button to buttons to monitor
    def add(self, act):
        self.monitor.append(act)


# set butonRel in gameVariables to release handler
gameVariables.butonRel = ClickRelese()


# handler for raindrops
class RainDrop:
    def __init__(self, tick, drop):
        self.tick = tick
        self.drop = drop

    # decrease bullet tick and when zero summon bullet
    def update(self):
        self.tick = max(0, self.tick - 1)
        if self.tick == 0:
            gameVariables.projectiles.add(self.drop)
            return True
        return False


# handler for rain
class Rain:
    def __init__(self):
        self.rainDrops = list()
        self.doRain = False

    # remove raindrops from list that needs to be summoned when summoned
    def update(self):
        if self.doRain:
            for j, i in reversed(list(enumerate(self.rainDrops))):
                if i.update():
                    self.rainDrops.pop(j)

        if self.rainDrops == list():
            self.doRain = False


# set raining in gameVariables to rain handler
gameVariables.raining = Rain()


# function that starts the rain
def makeItRain():
    rain_amount = gameVariables.rain_amount
    number = randint(rain_amount - 5, rain_amount + 5)
#    print(number)
    for i in range(number):
        waitAm = randint(0, 25)
        proj = Bullets("bullet.png", (round(random() * gameVariables.screenSize[0]), 1), 2,
                       gameVariables.bullet_damage, gameVariables.bullet_speed, gameVariables.bull_size)
        drop = RainDrop(waitAm, proj)
        gameVariables.raining.rainDrops.append(drop)
    gameVariables.raining.doRain = True


# some weird stuff
class shield:
    def __init__(self):
        self.sheild = gameFunctions()
        self.sheild = False

    def __init__(self, direc, controls, pos, sz=12.5):
        super().__init__()
        self.vel = [0, 0]
        self.pos = list(pos)
        self.startpos = pos
        self.hp = gameVariables.player_health
        self.direc = 0 if direc == "left" else 1
        self.speed = 5
        self.jump = 10  # 6
        self.airtime = self.time = self.u = 0
        self.airjumps = 1
        self.jumptick = 0
        self.offs = [0, 23]

        self.fall = True

        self.dead = False

        self.directions = [gameFunctions.loadImage("{0}/leftshield.png".format(shieldSpr), sz),
                           gameFunctions.loadImage("{0}/rightshield.png".format(shieldSpr), sz)]
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
