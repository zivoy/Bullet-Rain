from gameClasses import *
import gameFunctions
import gameVariables
from gameFunctions import placeAt

stage1 = [gameFunctions.drawRectangle(placeAt((20, 30)), placeAt((40, 35))),
          gameFunctions.drawRectangle(placeAt((60, 30)), placeAt((80, 35))),
          gameFunctions.drawRectangle(placeAt((45, 59)), placeAt((65, 56))),
          gameFunctions.drawRectangle(placeAt((30, 60)), placeAt((32, 100))),
          gameFunctions.drawRectangle(placeAt((20, 75)), placeAt((35, 70)))]

stage2 = [gameFunctions.drawRectangle(placeAt((10, 30)), placeAt((34, 37.5))),
          gameFunctions.drawRectangle(placeAt((50, 30)), placeAt((70, 35))),
          gameFunctions.drawRectangle(placeAt((41, 59)), placeAt((65, 56))),
          gameFunctions.drawRectangle(placeAt((30, 60)), placeAt((32, 100))),
          gameFunctions.drawRectangle(placeAt((30, 75)), placeAt((30, 75))),
          gameFunctions.drawRectangle(placeAt((47.5, 30)), placeAt((52.5, 70)))]

stage3 = [gameFunctions.drawRectangle(placeAt((25, 30)), placeAt((40, 40))),
          gameFunctions.drawRectangle(placeAt((55, 30)), placeAt((75, 35))),
          gameFunctions.drawRectangle(placeAt((43, 59)), placeAt((65, 56))),
          gameFunctions.drawRectangle(placeAt((30, 60)), placeAt((32, 100))),
          gameFunctions.drawRectangle(placeAt((25, 75)), placeAt((32.5, 72.5)))]

def createStage(stage3):
    global platforms
    platforms = pygame.Surface(gameVariables.screenSize, pygame.SRCALPHA)

    floors = [gameFunctions.drawRectangle(placeAt((0, 10)), placeAt((100, 0))),
              gameFunctions.drawRectangle(placeAt((-5, 0)), placeAt((0, 100))),
              gameFunctions.drawRectangle(placeAt((105, 0)), placeAt((100, 100))),
              gameFunctions.drawRectangle(placeAt((0, 105)), placeAt((100, 100)))]

    for i in floors:
        gameVariables.obstecls.append(i)
        gameFunctions.fillArea(platforms, gameFunctions.loadImage("ground.jpg", .4), i)

    for i in stage3:
        gameVariables.obstecls.append(i)
        gameFunctions.fillArea(platforms, gameFunctions.loadImage("briks.jpg", 1.2), i)


def draw(screen, pos):
    gameFunctions.paralaxBack(screen, pos)
    screen.blit(platforms, (0, 0))
