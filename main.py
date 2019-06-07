from gameClasses import *
import gameVariables
import stage
import settings
import gameFunctions
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


black = Color.BLACK.value
red = Color.RED.value
blue = Color.BLUE.value

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
        screen.fill(black)

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
        screen.fill(black)

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

        screen.fill(red)

        # this is the text that appear on the intro screen askign the user for the name
        gameFunctions.print_text(win, 10, 25, "The first thing you need to do is to enter your names...", Color.YELLOW,
                                 screen)
        gameFunctions.print_text(win, 10, 175, "Player 1 shall be known as ",Color.YELLOW, screen)
        gameFunctions.print_text(lost, 10, 225, "Enter Your Name", Color.WHITE, screen)
        gameFunctions.print_text(bigfont, 10, 250, gameVariables.player_list.player1, Color.GREEN, screen)

        pygame.display.flip()

    #################################################################

    #######################################################################

    while True:
        screen.fill(blue)
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
        gameFunctions.print_text(win, 10, 25, "Player 2 shall be known as ", Color.YELLOW, screen)
        gameFunctions.print_text(lost, 10, 125, "Enter Your Name", Color.WHITE, screen)
        gameFunctions.print_text(bigfont, 10, 150, gameVariables.player_list.player2, Color.GREEN, screen)

        pygame.display.flip()

##############################################################################

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
        screen.fill(black)

        # this is the text that appear on the intro screen askign the user for the name
        gameFunctions.print_text(bigfont, 50, 25, "Instructions", Color.GREEN, screen)
        gameFunctions.print_text(win, 10, 100, gameVariables.player_list[0] + "'s controlls are:", Color.RED,
                                 screen)
        gameFunctions.print_text(myfont, 10, 150, "The A, S, W and D Keys to move and 5 for bullets and 6 for Rocket",
                                 Color.WHITE,
                                 screen)
        gameFunctions.print_text(win, 10, 250, gameVariables.player_list[1] + "'s controlls are:", Color.BLUE,
                                 screen)
        gameFunctions.print_text(myfont, 10, 300, "Arrow keys, and bullet is keypad 2, rocket is keypad 3", Color.WHITE,
                                 screen)
        gameFunctions.print_text(myfont, 10, 350,
                                 "Both players have a mid air jump that cools down when they hit the ground", Color.RED,
                                 screen)
        gameFunctions.print_text(myfont, 10, 400, "Good luck...",
                                 Color.WHITE, screen)
        pygame.display.flip()

    ###################################++++++++++++++++++++++++++++++++######################

    stage.createStage(gameVariables.stage_choice)

    player1 = Player("player1", "right", gameVariables.player1_controls, gameVariables.player_list.player1, (200, 200),
                     gameVariables.screenSize[1]/3200)
    player2 = Player("player2", "left", gameVariables.player2_controls, gameVariables.player_list.player2, (600, 200),
                     gameVariables.screenSize[1]/3200)

    gameVariables.players.add(player1)
    gameVariables.players.add(player2)

    gameVariables.score = gameVariables.player_list.list

    ######################################

    ################################
    # gameVariables.scr = screen

    rain_tick = gameVariables.rain_delay



    while True:
        pygame.mouse.set_visible = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    if settingsMen():
                        return
                if event.key == pygame.K_RETURN:
                    makeItRain()

        rain_tick = max(0,rain_tick-1)




        if rain_tick == 0:
            makeItRain()
            random_offset = randint(0, 200)
            off_dir = random(0, 1) * 2 - 1
            rain_tick = gameVariables.rain_delay + random_offset * off_dir



        avrg = gameFunctions.avreagePos(gameVariables.players.sprites())
        title = "{0}: {2} V.S. {1}: {3}".format(*gameVariables.player_list.list.keys(),
                                                *gameVariables.player_list.list.values())
        xPos, _ = bigfont.size(title)
        xPos = gameVariables.screenSize[0] / 2 - xPos / 2
        screen.fill(black)
        stage.draw(screen, avrg)

        gameVariables.raining.update()
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


def settingsMen():
    menu = True
    cols = [Color.BLUE.value, Color.RED.value]

    sS = sM = sL = 0
    if gameVariables.settings['screen'] == "small":
        sS = 1
    elif gameVariables.settings['screen'] == "medium":
        sM = 1
    else:
        sL = 1

    scrX = 19
    screenSmall = Button("Small", gameFunctions.placeAt((scrX, 20)), gameFunctions.placeAt((15, 5)), cols, win, sS,
                         func=lambda: gameFunctions.setScreen("small"))
    screenMedium = Button("Medium", gameFunctions.placeAt((scrX + 17, 20)), gameFunctions.placeAt((15, 5)), cols, win,
                          sM, func=lambda: gameFunctions.setScreen("medium"))
    screenLarge = Button("Large", gameFunctions.placeAt((scrX + 34, 20)), gameFunctions.placeAt((15, 5)), cols, win, sL,
                          func=lambda: gameFunctions.setScreen("large"))

    dE = dM = dH = 0
    if gameVariables.settings['difficulty'] == "easy":
        dE = 1
    elif gameVariables.settings['difficulty'] == "medium":
        dM = 1
    else:
        dH = 1

    diffX = 17
    easyDiff = Button("Easy", gameFunctions.placeAt((diffX, 30)), gameFunctions.placeAt((15, 5)), cols, win, dE,
                      func=lambda: gameFunctions.setDiff("easy"))
    mediumDiff = Button("Medium", gameFunctions.placeAt((diffX + 17, 30)), gameFunctions.placeAt((15, 5)), cols, win,
                        dM, func=lambda: gameFunctions.setDiff("medium"))
    hardDiff = Button("Hard", gameFunctions.placeAt((diffX + 34, 30)), gameFunctions.placeAt((15, 5)), cols, win, dH,
                      func=lambda: gameFunctions.setDiff("hard"))

    pY = pN = 0
    if gameVariables.settings['power-ups']:
        pY = 1
    else:
        pN = 1

    powX = 16
    powTrue = Button("Yes", gameFunctions.placeAt((powX + 17, 40)), gameFunctions.placeAt((15, 5)), cols, win, pY,
                     func=lambda: gameFunctions.setPow(True))
    powFalse = Button("No", gameFunctions.placeAt((powX, 40)), gameFunctions.placeAt((15, 5)), cols, win, pN,
                      func=lambda: gameFunctions.setPow(False))

    screenSize = MultipleOptions([screenSmall, screenMedium, screenLarge])
    diffs = MultipleOptions([easyDiff, mediumDiff, hardDiff])
    pows = MultipleOptions([powTrue, powFalse])

    save = ClickButton("Save Settings", gameFunctions.placeAt((30, 90)), gameFunctions.placeAt((21, 5)), cols, win,
                       func=lambda: settings.compose())  # print(gameVariables.settings))
    apply = ClickButton("Apply settings", gameFunctions.placeAt((55, 90)), gameFunctions.placeAt((21, 5)), cols, win,
                        func=lambda: settings.apply())

    dele = 0

    while menu:
        acc = False
        if pygame.mouse.get_pressed()[0] and not dele > 0:
            acc = True
            dele = 5
        diffs.update(pygame.mouse, acc)
        screenSize.update(pygame.mouse, acc)
        pows.update(pygame.mouse, acc)

        save.update(pygame.mouse, acc)
        apply.update(pygame.mouse, acc)

        pygame.mouse.set_visible = True
        screen.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    menu = False

            if event.type == pygame.MOUSEBUTTONUP:
                gameVariables.butonRel.gotClicked()

        gameFunctions.print_text(bigfont, 50, 25, "Hello and Welcome to Bullet-Rain!", Color.RED, screen)

        gameFunctions.print_text(win, *gameFunctions.placeAt((1, 20)), "Screen Size:", Color.WHITE, screen)
        gameFunctions.print_text(win, *gameFunctions.placeAt((1, 30)), "Difficulty:", Color.WHITE, screen)
        gameFunctions.print_text(win, *gameFunctions.placeAt((1, 40)), "Power ups:", Color.WHITE, screen)

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
