from gameClasses import *
import gameFunctions
import gameVariables


def draw(screen, pos):
    gameFunctions.paralaxBack(screen, pos)

    pygame.draw.rect(screen, [63, 64, 65], gameFunctions.drawRectangle((0, 100), (gameVariables.screenSize[0], 0)))
    pygame.draw.rect(screen, [0, 0, 0], gameFunctions.drawRectangle((400, 300), (600, 300)))
