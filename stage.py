from gameClasses import *
import gameFunctions
import gameVariables
from gameFunctions import placeAt

groundBounds = list()


def createStage():
    global platforms
    platforms = pygame.Surface(gameVariables.screenSize, pygame.SRCALPHA)
    groundBounds.append(gameFunctions.drawRectangle((0, 100), (gameVariables.screenSize[0], 0)))
    groundBounds.append(gameFunctions.drawRectangle(placeAt((20, 30)), placeAt((40, 35))))
    for i in groundBounds:
        gameFunctions.fillArea(platforms, gameFunctions.loadImage("briks.jpg", 1.2), i)

def draw(screen, pos):
    gameFunctions.paralaxBack(screen, pos)
    screen.blit(platforms, (0, 0))
