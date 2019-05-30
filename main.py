import stage
import gameFunctions
from gameClasses import *
import gameVariables
import pygame
from pygame.locals import *
import sys


####from fiirstclass import bla ###    Put classes here

pygame.init()

# These are some fonts that I made up with differ sizes for different events such as when you win, lose, etc.
bigfont = pygame.font.SysFont("monospace", 40)
myfont = pygame.font.SysFont("monospace", 25)
lost = pygame.font.SysFont("monospace", 20)
win = pygame.font.SysFont("monospace", 30)


gameVariables.screenSize = (1250, 800)

#color list
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0,0,0)


# use clock to slow things down
clock = pygame.time.Clock()
# creates a screen
screen = pygame.display.set_mode(gameVariables.screenSize)


#################################################
score=[0,0]


beatlist=[]
for i in range(1000):
    beatlist.append(random.randrange(1,7))
#############################################


def winner(x,y):
    if x>y:
        score[1]+=1
    elif x==y:
        score[1]+=0
    else:
        score[0]+=1




#What is this????
def die_sum(lister):
    lister.sort(reverse=True)
    adder=""
    for i in lister:
        adder+=str(i)
    return int(adder)

def main(): #################################################################
#    white = (0, 0, 255 )

    instructions = True  # intro is the boolean that keeps me in the introduction window

    # makes a variable where I will record the keys pressed by the user when typing the name
    player1_name = ""
    player2_name = ""

    # first screen
    screen.fill(black)

    # this is the text that appear on the intro screen askign the user for the name
    gameFunctions.print_text(bigfont, 50, 25, "Hello and Welcome to Bullet-Rain!", red, screen)
    gameFunctions.print_text(win, 10, 100, "This is a two-player game and here are the instructions:", blue, screen)
    gameFunctions.print_text(myfont, 10, 150, "Each player is a character in the world of Rain.", white, screen)
    gameFunctions.print_text(myfont, 10, 200, "the game is a PVP game last man standing", white, screen)
    gameFunctions.print_text(myfont, 10, 250, "In this game there are power-ups and ledges to jump to", white, screen)
    gameFunctions.print_text(myfont, 10, 300, "Good luck", white, screen)
    gameFunctions.print_text(myfont, 10, 350, "The player who reaches five points first wins!", red, screen)
    gameFunctions.print_text(myfont, 10, 400, "But before playing we need to take you to some other screens.", white,
                             screen)
    gameFunctions.print_text(myfont, 10, 450, "Please press enter to continue.", white, screen)

    pygame.display.flip()

    while instructions:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYUP:
                if event.key == K_RETURN:
                    instructions = False

    #############################################################################

    intro_player1 = True  # intro is the boolean that keeps me in the introduction window

    # makes a variable where I will record the keys pressed by the user when typing the name
    player1_name = ""
    player2_name = ""

    while intro_player1:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYUP:
                if event.key == K_RETURN or event.key == K_KP_ENTER:
                    intro_player1 = False

                player1_name = gameFunctions.typeing(event.key, player1_name)

        screen.fill(black)

        # this is the text that appear on the intro screen askign the user for the name
        gameFunctions.print_text(win, 10, 25, "The first thing you need to do is to enter your names", blue, screen)
        gameFunctions.print_text(win, 10, 125, "", red, screen)
        gameFunctions.print_text(win, 10, 175, "Player 1 shall be known as ", red, screen)
        gameFunctions.print_text(lost, 10, 225, "Enter Your Name", white, screen)
        gameFunctions.print_text(bigfont, 10, 250, player1_name, green, screen)

        pygame.display.flip()

    intro_player2 = True

    while intro_player2:
        screen.fill(black)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYUP:
                if event.key == K_RETURN or event.key == K_KP_ENTER:
                    intro_player2 = False

                player2_name = gameFunctions.typeing(event.key, player2_name)

        gameFunctions.print_text(win, 10, 25, "Player 2 shall be known as ", red, screen)
        gameFunctions.print_text(lost, 10, 125, "Enter Your Name", white, screen)
        gameFunctions.print_text(bigfont, 10, 150, player2_name, green, screen)

        pygame.display.flip()
    curr = (0, 0)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    settings()
            curr = pygame.mouse.get_pos()
        screen.fill((0, 0, 0))
        stage.draw(screen, curr)
        pygame.display.flip()
        clock.tick(60)


def settings():
    menu = True
    while menu:
        screen.fill(black)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    menu = False

        gameFunctions.print_text(bigfont, 50, 25, "Hello and Welcome to Bullet-Rain!", red, screen)



if __name__ == "__main__":  # ####################################################################
    main()

