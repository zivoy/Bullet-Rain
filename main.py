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
# Title of the game
pygame.display.set_caption("Bullet Rain")

#################################################

'''
beatlist=[]
for i in range(1000):
    beatlist.append(random.randrange(1,7))'''
#############################################


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
    gameVariables.player_list = PlayerList("", "", 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    leave = True

                gameVariables.player_list.player1 = gameFunctions.typeing(event.key, gameVariables.player_list.player1)
        if leave:
            leave = False
            break

        screen.fill(BLACK)

        # this is the text that appear on the intro screen askign the user for the name
        gameFunctions.print_text(win, 10, 25, "The first thing you need to do is to enter your names", Color.BLUE, screen)
        gameFunctions.print_text(win, 10, 175, "Player 1 shall be known as ", Color.RED, screen)
        gameFunctions.print_text(lost, 10, 225, "Enter Your Name", Color.WHITE, screen)
        gameFunctions.print_text(bigfont, 10, 250, gameVariables.player_list.player1, Color.GREEN, screen)

        pygame.display.flip()

    while True:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    leave = True

                gameVariables.player_list.player2 = gameFunctions.typeing(event.key, gameVariables.player_list.player2)
        if leave:
            break
        gameFunctions.print_text(win, 10, 25, "Player 2 shall be known as ", Color.RED, screen)
        gameFunctions.print_text(lost, 10, 125, "Enter Your Name", Color.WHITE, screen)
        gameFunctions.print_text(bigfont, 10, 150, gameVariables.player_list.player2, Color.GREEN, screen)

        pygame.display.flip()

    if gameVariables.player_list.player1 == "":
        gameVariables.player_list.player1 = "Player 1"
    if gameVariables.player_list.player2 == "":
        gameVariables.player_list.player2 = "Player 2"

    stage.createStage()

    player1 = Player("player1", "right", gameVariables.player1_controls, gameVariables.player_list.player1, (200, 200))
    player2 = Player("player2", "left", gameVariables.player2_controls, gameVariables.player_list.player2, (600, 200))

    gameVariables.players.add(player1)
    gameVariables.players.add(player2)

    gameVariables.score = gameVariables.player_list.list

   # gameVariables.scr = screen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    if settings():
                        return
        avrg = gameFunctions.avreagePos(gameVariables.players.sprites())
        title = "{0}: {2} V.S. {1}: {3}".format(*gameVariables.player_list.list.keys(),
                                                *gameVariables.player_list.list.values())
        xPos, _ = bigfont.size(title)
        xPos = gameVariables.screenSize[0]/2 - xPos/2
        screen.fill(BLACK)
        stage.draw(screen, avrg)

        gameVariables.players.update(pygame.key.get_pressed(), clock.get_time())
        gameVariables.projectiles.update()

        gameVariables.players.draw(screen)
        gameVariables.projectiles.draw(screen)

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