import stage
import gameFunctions
import settings
from gameClasses import *
import gameVariables
import pygame
import sys

####from fiirstclass import bla ###    Put classes here

pygame.init()

# These are some fonts that I made up with differ sizes for different events such as when you win, lose, etc.
titlefont = pygame.font.Font("kunstler.ttf", 200)
bigfont = pygame.font.SysFont("monospace", 40)
myfont = pygame.font.SysFont("monospace", 25)
lost = pygame.font.SysFont("monospace", 20)
win = pygame.font.SysFont("monospace", 30)

settings.load()
settings.apply()

BLACK = Color.BLACK.value

# use clock to slow things down
clock = pygame.time.Clock()
# creates a screen
screen = pygame.display.set_mode(gameVariables.screenSize)
# Title of the game
pygame.display.set_caption("Bullet Rain")

#################################################


def main():  #################################################################
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
        gameFunctions.print_text(titlefont, 200, 300, "Bullet-Rain", Color.RED, screen)

        pygame.display.flip()

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
        gameFunctions.print_text(win, 10, 25, "The first thing you need to do is to enter your names", Color.BLUE,
                                 screen)
        gameFunctions.print_text(win, 10, 175, "Player 1 shall be known as ", Color.RED, screen)
        gameFunctions.print_text(lost, 10, 225, "Enter Your Name", Color.WHITE, screen)
        gameFunctions.print_text(bigfont, 10, 250, gameVariables.player_list.player1, Color.GREEN, screen)

        pygame.display.flip()

#################################################################



#######################################################################

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
            leave = False
            break
        gameFunctions.print_text(win, 10, 25, "Player 2 shall be known as ", Color.RED, screen)
        gameFunctions.print_text(lost, 10, 125, "Enter Your Name", Color.WHITE, screen)
        gameFunctions.print_text(bigfont, 10, 150, gameVariables.player_list.player2, Color.GREEN, screen)

        pygame.display.flip()



    if gameVariables.player_list.player1 == "":
        gameVariables.player_list.player1 = "ROB"
    if gameVariables.player_list.player2 == "":
        gameVariables.player_list.player2 = "BOB"


###############################++++++++++++++++++++++#########################3

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
        gameFunctions.print_text(bigfont, 50, 25, "Instructions", Color.RED, screen)
        gameFunctions.print_text(win, 10, 100, gameVariables.player_list[0] +"'s controlls are:", Color.BLUE,
                                 screen)
        gameFunctions.print_text(myfont, 10, 150, "The A, S, W and D Keys to move and 5 for bullets and 6 for Rocket", Color.WHITE,
                                 screen)
        gameFunctions.print_text(myfont, 10, 250,  gameVariables.player_list[1] +"'s controlls are:", Color.WHITE,
                                 screen)
        gameFunctions.print_text(myfont, 10, 300, "Arrow keys, and bullet is keypad 2, rocket is keypad 3", Color.WHITE, screen)
        gameFunctions.print_text(myfont, 10, 350, "Both players have a mid air jump that cools down when they hit the ground", Color.RED, screen)
        gameFunctions.print_text(myfont, 10, 400, "Good luck...",
                                 Color.WHITE, screen)
        pygame.display.flip()




###################################++++++++++++++++++++++++++++++++######################




    stage.createStage(1)

    player1 = Player("player1", "right", gameVariables.player1_controls, gameVariables.player_list.player1, (200, 200))
    player2 = Player("player2", "left", gameVariables.player2_controls, gameVariables.player_list.player2, (600, 200))

    gameVariables.players.add(player1)
    gameVariables.players.add(player2)

    gameVariables.score = gameVariables.player_list.list

######################################


################################
    #gameVariables.scr = screen
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
        xPos = gameVariables.screenSize[0] / 2 - xPos / 2
        screen.fill(BLACK)
        stage.draw(screen, avrg)

        gameVariables.players.update(pygame.key.get_pressed(), clock.get_time())
        gameVariables.projectiles.update()

        gameVariables.players.draw(screen)
        gameVariables.projectiles.draw(screen)
        gameVariables.statuss.draw(screen)

        v = 5
        gameFunctions.print_text(bigfont, xPos + v, 15 + v, title, Color.LIGHT_GRAY, screen)
        gameFunctions.print_text(bigfont, xPos, 15, title, Color.WHITE, screen)

        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)


def settings():
    menu = True
    cols = [[0, 0, 255, 255], [255, 0, 0, 255]]

    scrX = 19
    screenSmall = Button("Small", gameFunctions.placeAt((scrX, 20)), gameFunctions.placeAt((15, 5)), cols, win)
    screenMedium = Button("Medium", gameFunctions.placeAt((scrX+17, 20)), gameFunctions.placeAt((15, 5)), cols, win)
    screenLarge = Button("Large", gameFunctions.placeAt((scrX+34, 20)), gameFunctions.placeAt((15, 5)), cols, win, 1)

    diffX = 17
    easyDiff = Button("Easy", gameFunctions.placeAt((diffX, 30)), gameFunctions.placeAt((15, 5)), cols, win)
    mediumDiff = Button("Medium", gameFunctions.placeAt((diffX + 17, 30)), gameFunctions.placeAt((15, 5)), cols, win, 1)
    hardDiff = Button("Hard", gameFunctions.placeAt((diffX + 34, 30)), gameFunctions.placeAt((15, 5)), cols, win)

    powX = 16
    powTrue = Button("Yes", gameFunctions.placeAt((powX + 17, 40)), gameFunctions.placeAt((15, 5)), cols, win)
    powFalse = Button("No", gameFunctions.placeAt((powX, 40)), gameFunctions.placeAt((15, 5)), cols, win, 1)

    screenSize = MultipleOptions([screenSmall, screenMedium, screenLarge])
    diffs = MultipleOptions([easyDiff, mediumDiff, hardDiff])
    pows = MultipleOptions([powTrue, powFalse])

    save = ClickButton("Save Settings", gameFunctions.placeAt((30, 90)), gameFunctions.placeAt((21, 5)), cols, win)
    apply = ClickButton("Apply settings", gameFunctions.placeAt((55, 90)), gameFunctions.placeAt((21, 5)), cols, win,
                   func=lambda: print(gameVariables.settings))

    dele = 0

    while menu:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    menu = False

        gameFunctions.print_text(bigfont, 50, 25, "Hello and Welcome to Bullet-Rain!", Color.RED, screen)

        gameFunctions.print_text(win, *gameFunctions.placeAt((1, 20)), "Screen Size:", Color.WHITE, screen)
        gameFunctions.print_text(win, *gameFunctions.placeAt((1, 30)), "Difficulty:", Color.WHITE, screen)
        gameFunctions.print_text(win, *gameFunctions.placeAt((1, 40)), "Power ups:", Color.WHITE, screen)

        acc = False
        if pygame.mouse.get_pressed()[0] and not dele > 0:
            acc = True
            dele = 5

        diffs.update(pygame.mouse, acc)
        screenSize.update(pygame.mouse, acc)
        pows.update(pygame.mouse, acc)

        save.update(pygame.mouse, acc)
        apply.update(pygame.mouse, acc)

        save.draw(screen)
        apply.draw(screen)

        diffs.draw(screen)
        screenSize.draw(screen)
        pows.draw(screen)

        pygame.display.flip()

        if dele > 0:
            dele -= 1
        clock.tick(30)


if __name__ == "__main__":  # ####################################################################
    main()

pygame.quit()
sys.exit()
