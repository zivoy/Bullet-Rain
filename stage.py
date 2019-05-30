from gameClasses import *
import gameFunctions
import gameVariables


def draw(screen, pos):
    gameFunctions.paralaxBack(screen, pos)
    screenSz = gameVariables.screenSize

    pygame.draw.rect(screen, [63, 64, 65], gameFunctions.drawRectangle((0, 100), (gameVariables.screenSize[0], 0)))
    pygame.draw.rect(screen, [0, 0, 0], gameFunctions.drawRectangle((int(screenSz[0]*.2), int(screenSz[1]*.3)), (600, 300)))
