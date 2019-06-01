import stage
import gameFunctions
from gameClasses import *
import gameVariables
import pygame
import sys


####from fiirstclass import bla ###    Put classes here

pygame.init()

# These are some fonts that I made up with differ sizes for different events such as when you win, lose, etc.
bigfont = pygame.font.SysFont("monospace", 40)
myfont = pygame.font.SysFont("monospace", 25)
lost = pygame.font.SysFont("monospace", 20)
win = pygame.font.SysFont("monospace", 30)


gameVariables.screenSize = (1250, 800)

BLACK = Color.BLACK.value


# use clock to slow things down
clock = pygame.time.Clock()
# creates a screen
screen = pygame.display.set_mode(gameVariables.screenSize)


#################################################
score = [0, 0]


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






def main(): #################################################################
    leave = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    leave = True
        if leave:
            leave = False
            break

        # first screen
        screen.fill(BLACK)

        # this is the text that appear on the intro screen askign the user for the name
        gameFunctions.print_text(bigfont, 50, 25, "Hello and Welcome to Bullet-Rain!", Color.RED, screen)
        gameFunctions.print_text(win, 10, 100, "This is a two-player game and here are the instructions:", Color.BLUE,
                                 screen)
        gameFunctions.print_text(myfont, 10, 150, "Each player is a character in the world of Rain.", Color.WHITE,
                                 screen)
        gameFunctions.print_text(myfont, 10, 200, "the game is a PVP game last man standing", Color.WHITE, screen)
        gameFunctions.print_text(myfont, 10, 250, "In this game there are power-ups and ledges to jump to", Color.WHITE,
                                 screen)
        gameFunctions.print_text(myfont, 10, 300, "Good luck", Color.WHITE, screen)
        gameFunctions.print_text(myfont, 10, 350, "The player who reaches five points first wins!", Color.RED, screen)
        gameFunctions.print_text(myfont, 10, 400, "But before playing we need to take you to some other screens.",
                                 Color.WHITE, screen)
        gameFunctions.print_text(myfont, 10, 450, "Please press enter to continue.", Color.WHITE, screen)

        pygame.display.flip()

    #############################################################################

    # makes a variable where I will record the keys pressed by the user when typing the name
    player1_name = ""
    player2_name = ""

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    leave = True

                player1_name = gameFunctions.typeing(event.key, player1_name)
        if leave:
            leave = False
            break

        screen.fill(BLACK)

        # this is the text that appear on the intro screen askign the user for the name
        gameFunctions.print_text(win, 10, 25, "The first thing you need to do is to enter your names", Color.BLUE, screen)
        gameFunctions.print_text(win, 10, 175, "Player 1 shall be known as ", Color.RED, screen)
        gameFunctions.print_text(lost, 10, 225, "Enter Your Name", Color.WHITE, screen)
        gameFunctions.print_text(bigfont, 10, 250, player1_name, Color.GREEN, screen)

        pygame.display.flip()

    while True:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    leave = True

                player2_name = gameFunctions.typeing(event.key, player2_name)
        if leave:
            leave = False
            break
        gameFunctions.print_text(win, 10, 25, "Player 2 shall be known as ", Color.RED, screen)
        gameFunctions.print_text(lost, 10, 125, "Enter Your Name", Color.WHITE, screen)
        gameFunctions.print_text(bigfont, 10, 150, player2_name, Color.GREEN, screen)

        pygame.display.flip()

    if player1_name == "":
        player1_name = "Player 1"
    if player2_name == "":
        player2_name = "Player 2"

    stage.createStage()

    player1 = Player("player1", "right", gameVariables.player1_controls, player1_name, (200, 200))
    player2 = Player("player2", "left", gameVariables.player2_controls, player2_name, (600, 200))

    gameVariables.players.add(player1)
    gameVariables.players.add(player2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    if settings():
                        return
        avrg = gameFunctions.avreagePos(gameVariables.players.sprites())
        title = "{0}: {2} V.S. {1}: {3}".format(player1_name, player2_name, score[0], score[1])
        xPos, _ = bigfont.size(title)
        xPos = gameVariables.screenSize[0]/2 - xPos/2
        screen.fill(BLACK)
        stage.draw(screen, avrg)

        gameVariables.players.draw(screen)
        gameVariables.players.update(pygame.key.get_pressed(), clock.get_time(),)

        v = 5
        gameFunctions.print_text(bigfont, xPos + v, 15 + v, title, Color.LIGHT_GRAY, screen)
        gameFunctions.print_text(bigfont, xPos, 15, title, Color.WHITE, screen)

        pygame.display.flip()
        clock.tick(60)


def settings():
    menu = True
    while menu:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    menu = False

        gameFunctions.print_text(bigfont, 50, 25, "Hello and Welcome to Bullet-Rain!", Color.RED, screen)
        pygame.display.flip()


if __name__ == "__main__":  # ####################################################################
    main()

pygame.quit()
sys.exit()
