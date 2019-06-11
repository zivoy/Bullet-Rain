from gameClasses import *
import gameFunctions
import gameVariables
from gameFunctions import placeAt


# create a stage from given default is option 1
def createStage(stage=1):
    global platforms
    # stages/brick platforms
    stages = [[gameFunctions.drawRectangle(placeAt((20, 30)), placeAt((40, 35))),
               gameFunctions.drawRectangle(placeAt((60, 30)), placeAt((80, 35))),
               gameFunctions.drawRectangle(placeAt((45, 59)), placeAt((65, 55))),
               gameFunctions.drawRectangle(placeAt((30, 60)), placeAt((32, 100))),
               gameFunctions.drawRectangle(placeAt((20, 75)), placeAt((35, 70)))],

              [gameFunctions.drawRectangle(placeAt((10, 30)), placeAt((34, 37.5))),
               gameFunctions.drawRectangle(placeAt((50, 30)), placeAt((70, 35))),
               gameFunctions.drawRectangle(placeAt((41, 59)), placeAt((65, 56))),
               gameFunctions.drawRectangle(placeAt((30, 60)), placeAt((32, 100))),
               gameFunctions.drawRectangle(placeAt((30, 75)), placeAt((30, 75))),
               gameFunctions.drawRectangle(placeAt((47.5, 30)), placeAt((52.5, 70)))],

              [gameFunctions.drawRectangle(placeAt((25, 30)), placeAt((40, 40))),
               gameFunctions.drawRectangle(placeAt((55, 30)), placeAt((75, 35))),
               gameFunctions.drawRectangle(placeAt((43, 59)), placeAt((65, 56))),
               gameFunctions.drawRectangle(placeAt((30, 60)), placeAt((32, 100))),
               gameFunctions.drawRectangle(placeAt((25, 75)), placeAt((32.5, 72.5)))]]

    # surface
    platforms = pygame.Surface(gameVariables.screenSize, pygame.SRCALPHA)

    # bounds
    floors = [gameFunctions.drawRectangle(placeAt((0, 10)), placeAt((100, 0))),
              gameFunctions.drawRectangle(placeAt((-5, 0)), placeAt((0, 100))),
              gameFunctions.drawRectangle(placeAt((105, 0)), placeAt((100, 100))),
              gameFunctions.drawRectangle(placeAt((0, 105)), placeAt((100, 100)))]

    # load bounds
    for i in floors:
        gameVariables.obstecls.append(i)
        gameFunctions.fillArea(platforms, gameFunctions.loadImage("ground3.jpg", .5), i)

    # platforms
    for i in stages[stage - 1]:
        gameVariables.obstecls.append(i)
        gameFunctions.fillArea(platforms, gameFunctions.loadImage("briks.jpg", .9), i)


# draw background and stage on it
def draw(screen, pos):
    gameFunctions.paralaxBack(screen, pos)
    screen.blit(platforms, (0, 0))
