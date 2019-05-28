from gameClasses import *
import gameVariables

screenSize = [0, 0]
stage = pygame.image

def paralaxBack(pos, img):
    pass


# The idea for the function print_text was taken from //stackoverflow.com/questions/39594390
# but later I realized that it is not that useful because it has a set font. This is why below I created
# my own fonts
def print_text(font, x, y, text, color, screen):
    """Draws a text image to display surface"""
    text_image = font.render(text, True, color)
    screen.blit(text_image, (x,y))
#########


def drawImage(screen, pos, img, scl=1, rot=0):
    imge = pygame.image.load("images/{}".format(img)).convert_alpha()
    imge = pygame.transform.rotozoom(imge, rot, scl)
    screen.blit(imge, pos)
