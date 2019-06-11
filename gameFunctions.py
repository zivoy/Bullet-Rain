from gameClasses import pygame
import gameVariables
import settings


# scale and load image for background
def loadBack(aa=True):
    # get image size
    sz = loadImage(gameVariables.img).get_size()
    szc = list(sz)
    szd = szc.copy()
    mul = 1

    # scale image
    if list(map(lambda x: sz[x] < gameVariables.screenSize[x], range(2))):
        for i in range(2):
            if szd[i] > gameVariables.screenSize[i]:
                mul = (gameVariables.screenSize[i] / sz[i]) * 1.1
                szd = list(map(lambda x: x * mul, sz))
        szc = szd

    for i in range(2):
        if szc[i] < gameVariables.screenSize[i]:
            mul = (gameVariables.screenSize[i] / sz[i]) * 1.1
            szc = list(map(lambda x: x * mul, sz))

    # load image
    gameVariables.stage = loadImage(gameVariables.img, mul, aaScale=aa)


# draw the image in paralax
def paralaxBack(screen, pos):
    if gameVariables.stage == pygame.image:
        loadBack(True)
    imgSz = gameVariables.stage.get_size()
    xDiff = gameVariables.screenSize[0] - imgSz[0]
    yDiff = gameVariables.screenSize[1] - imgSz[1]
    xMov = pos[0] * xDiff / gameVariables.screenSize[0]
    yMov = pos[1] * yDiff / gameVariables.screenSize[1]
    screen.blit(gameVariables.stage, (xMov, yMov))


# The idea for the function print_text was taken from //stackoverflow.com/questions/39594390
# but later I realized that it is not that useful because it has a set font. This is why below I created
# my own fonts
def print_text(font, x, y, text, color, screen):
    """Draws a text image to display surface"""
    text_image = font.render(text, True, color.value)
    screen.blit(text_image, (x, y))


#########


# load image with options to scale
def loadImage(img, scl=1, rot=0, aaScale=True):
    imge = pygame.image.load("images/{}".format(img)).convert_alpha()
    if aaScale:
        imge = pygame.transform.rotozoom(imge, rot, scl)
    else:
        imge = pygame.transform.rotozoom(imge, rot, 1)
        scl = list(map(lambda x: int(x * scl), imge.get_size()))
        imge = pygame.transform.scale(imge, scl)
    return imge


# function for typing text
def typeing(key, varb):
    if chr(key).lower() in gameVariables.keys and len(varb) < 16:
        varb += chr(key)
    elif key == pygame.K_BACKSPACE:
        varb = varb[:-1]

    return varb.upper()


# returns a rect given start pos and end pos
def drawRectangle(startPos, endPos, inv=True):
    if inv:
        startPos = invCord(startPos)
        endPos = invCord(endPos)

    xStart, yStart = startPos
    xEnd, yEnd = endPos
    xEnd = xEnd - xStart
    yEnd = yEnd - yStart

    xStart, xEnd = positiveBox(xStart, xEnd)
    yStart, yEnd = positiveBox(yStart, yEnd)

    return pygame.Rect(xStart, yStart, xEnd, yEnd)


# invert y coord
def invCord(cords):
    ret = list(cords)
    ret[1] = -(cords[1] - gameVariables.screenSize[1])
    return tuple(ret)


# fill an area of a rect with a repeting image
def fillArea(screen, img, rect):
    # pygame.draw.rect(screen, [63, 64, 65], rect)
    platform = pygame.Surface([abs(rect.w), abs(rect.h)], pygame.SRCALPHA)
    imgr = img.get_rect()
    fitX = abs(rect.w / imgr.w)
    fitY = abs(rect.h / imgr.h)
    for i in range(round(fitX + .5)):
        for j in range(round(fitY + .5)):
            platform.blit(img, (imgr.w * i, imgr.h * j))
    screen.blit(platform, (rect.x, rect.y))


# given the percentage of the screen return coords
def placeAt(percent):
    return int(gameVariables.screenSize[0] * percent[0] / 100), int(gameVariables.screenSize[1] * percent[1] / 100)


# function to handle deceleration
def decel(val, rate=.5):
    neg = -1 if val < 0 else 1

    if val != 0:
        return val - (rate * neg)
    else:
        return 0


# returns the average pos of coords
def avreagePos(sprites):
    x = list()
    y = list()
    for i in sprites:
        x.append(i.rect.x + i.rect.w / 2)
        y.append(i.rect.y + i.rect.h / 2)
    return avrage(x), avrage(y)


# does average
def avrage(items):
    return sum(items) / len(items)


# function that calculate velocity due to gravity
def gravity(initalVel, airtime):
    return initalVel + gameVariables.gravity * airtime


# function that makes sure that a rect will always be positive
def positiveBox(start, gofor):
    if gofor < 0:
        start += gofor
        return start, abs(gofor)
    else:
        return start, gofor


# toggle function
def flag(item1, item2, curr):
    if curr == item1:
        return item2
    else:
        return item1


# set the screen size
def setScreen(size):
    gameVariables.settings['screen'] = size
    return True


# set the difficulty
def setDiff(diff):
    gameVariables.settings['difficulty'] = diff
    return True


# set the use of power ups
def setPow(pows):
    gameVariables.settings['power-ups'] = pows
    return True


# apply and save settings
def saveAndApply():
    settings.apply()
    settings.compose()
    return True


# won message screen
def wonMsg(player, screen, font, color):
    message = "{0} won the game".format(player)
    tX, tY = font.size(message)
    posX, posY = placeAt((50, 50))
    posX -= tX / 2
    posY -= tY / 2
    print_text(font, posX, posY, message, color, screen)
