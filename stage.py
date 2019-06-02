from gameClasses import *
import gameFunctions
import gameVariables
from gameFunctions import placeAt


def createStage():
    global platforms
    platforms = pygame.Surface(gameVariables.screenSize, pygame.SRCALPHA)

    floors = [gameFunctions.drawRectangle(placeAt((0, 10)), placeAt((100, 0))),
              gameFunctions.drawRectangle(placeAt((-1, 0)), placeAt((0, 100))),
              gameFunctions.drawRectangle(placeAt((101, 0)), placeAt((100, 100)))]

    landings = [gameFunctions.drawRectangle(placeAt((20, 30)), placeAt((40, 35))),
                gameFunctions.drawRectangle(placeAt((50, 30)), placeAt((60, 35))),
                gameFunctions.drawRectangle(placeAt((45, 45)), placeAt((60, 50)))]

    for i in floors:
        gameVariables.obstecls.append(i)
        gameFunctions.fillArea(platforms, gameFunctions.loadImage("ground.jpg", .4), i)

    for i in landings:
        gameVariables.obstecls.append(i)
        gameFunctions.fillArea(platforms, gameFunctions.loadImage("briks.jpg", 1.2), i)


def draw(screen, pos):
    gameFunctions.paralaxBack(screen, pos)
    screen.blit(platforms, (0, 0))
