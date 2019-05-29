from gameClasses import *
import gameVariables


def paralaxBack(screen, pos):
    im = "opt1.jpg"
    gameVariables.stage = loadImage(im)
    sz = gameVariables.stage.get_size()
    s = sz.index(min(sz))
    mul = gameVariables.screenSize[s] / sz[s] * 1.1

    gameVariables.stage = loadImage(im, mul)
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
    text_image = font.render(text, True, color)
    screen.blit(text_image, (x, y))
#########


def loadImage(img, scl=1, rot=0):
    imge = pygame.image.load("images/{}".format(img)).convert_alpha()
    imge = pygame.transform.rotozoom(imge, rot, scl)
    return imge
