from gameClasses import *
import gameFunctions
import gameVariables
from gameFunctions import placeAt


def draw(screen, pos):
    gameFunctions.paralaxBack(screen, pos)

    pygame.draw.rect(screen, [63, 64, 65], gameFunctions.drawRectangle((0, 100), (gameVariables.screenSize[0], 0)))
    pygame.draw.rect(screen, [0, 0, 0], gameFunctions.drawRectangle(placeAt((20, 30)), placeAt((40, 35))))
