from gameClasses import *
import stage
import sys

####from fiirstclass import bla ###    Put classes here

pygame.init()

# These are some fonts that I made up with differ sizes for different events such as when you win, lose, etc.
titlefont = pygame.font.Font("./kunstler.ttf", 200)
#winfont = pygame.font.Font('monospace.fon', 36)
bigfont = pygame.font.SysFont("monospace", 40)
myfont = pygame.font.SysFont("monospace", 25)
lost = pygame.font.SysFont("monospace", 20)
win = pygame.font.SysFont("monospace", 30)
warning = pygame.font.Font("vgafix.fon", 36)

# load and apply settings
settings.load()
settings.apply()


# call colors into variables
black = Color.BLACK.value
red = Color.RED.value
blue = Color.BLUE.value

# use clock to slow things down
clock = pygame.time.Clock()
# creates a screen
screen = pygame.display.set_mode(gameVariables.screenSize)
# Title of the game
pygame.display.set_caption("Bullet Rain")

rain_tick = gameVariables.rain_delay

#################################################

#Creats game loop for the first screen
def main():  #################################################################
    # variable for leaving
    leave = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    leave = True
        # go to next screen
        if leave:
            leave = False
            break

        # first screen
        screen.fill(black)

        # this is the text that appear on the intro screen askign the user for the name
        gameFunctions.print_text(titlefont, 200, 300, "Bullet-Rain", Color.RED, screen)

        # update screen
        pygame.display.flip()
    # Creats game loop for the second screen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    leave = True
        # go to next screen
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
        gameFunctions.print_text(myfont, 10, 250, "In this game there are ledges to jump to bullets to dodge, and a rain to fear.", Color.WHITE,
                                 screen)
        gameFunctions.print_text(myfont, 10, 300, "Good luck", Color.WHITE, screen)
        gameFunctions.print_text(myfont, 10, 350, "The Player with the most points wins!!!", Color.RED, screen)
        gameFunctions.print_text(myfont, 10, 400, "But before playing we need to take you to some other screens.",
                                 Color.WHITE, screen)
        gameFunctions.print_text(myfont, 10, 450, "Please press enter to continue.", Color.WHITE, screen)

        # update screen
        pygame.display.flip()

    #############################################################################

    # makes a variable where I will record the keys pressed by the user when typing the name
    gameVariables.player_list = PlayerList("", "", 0)

    # Creates game loop for the first player screen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    leave = True

                # type name
                gameVariables.player_list.player1 = gameFunctions.typeing(event.key, gameVariables.player_list.player1)
        # next screen
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

        # update screen
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

                # type name
                gameVariables.player_list.player2 = gameFunctions.typeing(event.key, gameVariables.player_list.player2)
        # next screen
        if leave:
            leave = False
            break
        # screen messages
        gameFunctions.print_text(win, 10, 25, "Player 2 shall be known as ", Color.YELLOW, screen)
        gameFunctions.print_text(lost, 10, 125, "Enter Your Name", Color.WHITE, screen)
        gameFunctions.print_text(bigfont, 10, 150, gameVariables.player_list.player2, Color.GREEN, screen)

        # update screen
        pygame.display.flip()

    ##############################################################################

    # if name was not set defaults
    if gameVariables.player_list.player1 == "":
        gameVariables.player_list.player1 = "ROB"
    if gameVariables.player_list.player2 == "":
        gameVariables.player_list.player2 = "BOB"

    ##############################################################################

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    leave = True

        # next screen
        if leave:
            leave = False
            break

        # first screen
        screen.fill(black)

        # this is the text that appear on the intro screen askign the user for the name
        gameFunctions.print_text(bigfont, 50, 25, "Instructions", Color.GREEN, screen)
        gameFunctions.print_text(win, 10, 100, gameVariables.player_list[0] + "'s controls are:", Color.RED,
                                 screen)
        gameFunctions.print_text(myfont, 10, 150, "The A, S, W and D Keys to move, use 5 for bullets and 6 for rocket",
                                 Color.WHITE,
                                 screen)
        gameFunctions.print_text(win, 10, 250, gameVariables.player_list[1] + "'s controls are:", Color.BLUE,
                                 screen)
        gameFunctions.print_text(myfont, 10, 300, "Arrow keys, use keypad 2 for bullets, keypad 3 for rocket",
                                 Color.WHITE, screen)
        gameFunctions.print_text(myfont, 10, 350,
                                 "Both players have a mid air jump that cools down when they hit the ground", Color.RED,
                                 screen)
        gameFunctions.print_text(myfont, 10, 400, "Good luck...",
                                 Color.WHITE, screen)

        # update screen
        pygame.display.flip()

    ###############################################################################

    # create stage
    stage.createStage(gameVariables.stage_choice)

    # create players
    player1 = Player("player1", "right", gameVariables.player1_controls, gameVariables.player_list.player1, (200, 200),
                     gameVariables.screenSize[1]/3200)
    player2 = Player("player2", "left", gameVariables.player2_controls, gameVariables.player_list.player2, (600, 200),
                     gameVariables.screenSize[1]/3200)

    # load players into player sprite group
    gameVariables.players.add(player1)
    gameVariables.players.add(player2)

    ######################################

    ################################
    # gameVariables.scr = screen

    global rain_tick
    # set rain timer
    rain_tick = gameVariables.rain_delay

    # setup warning message
    warningMsg = warning.render("Rain incoming!!", False, Color.RED.value)
    warningMsg = pygame.transform.scale(warningMsg, list(map(lambda x: x*round(gameVariables.screenSize[0]/125),
                                                             warningMsg.get_size())))


    # main loop
    while True:
        # show won message if a player has won
        if won():
            break

        pygame.mouse.set_visible = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    if settingsMen():
                        return
                '''if event.key == pygame.K_RETURN:
                    makeItRain()'''

        # decrees rain tick
        rain_tick = max(0, rain_tick-1)

        # check if rain timer is 0 and start the rain
        if rain_tick == 0:
            makeItRain()
            random_offset = randint(0, 200)
            off_dir = randint(0, 1) * 2 - 1
            rain_tick = gameVariables.rain_delay + random_offset * off_dir

        # get average position of players
        avrg = gameFunctions.avreagePos(gameVariables.players.sprites())

        # make banner title message
        title = "{0}: {2} V.S. {1}: {3}".format(*gameVariables.player_list.list.keys(),
                                                *gameVariables.player_list.list.values())
        xPos, _ = bigfont.size(title)
        xPos = gameVariables.screenSize[0] / 2 - xPos / 2

        # fill screen with black and draw stage
        screen.fill(black)
        stage.draw(screen, avrg)

        # update players, rain and projectiles
        gameVariables.raining.update()
        gameVariables.players.update(pygame.key.get_pressed(), clock.get_time())
        gameVariables.projectiles.update()

        # draw players projectiles and status
        gameVariables.players.draw(screen)
        gameVariables.projectiles.draw(screen)
        gameVariables.statuss.draw(screen)

        # draw banner title
        v = 5
        gameFunctions.print_text(bigfont, xPos + v, 15 + v, title, Color.LIGHT_GRAY, screen)
        gameFunctions.print_text(bigfont, xPos, 15, title, Color.WHITE, screen)

        # display warning message when it is about to rain
        if 50 < rain_tick < 200:
            screen.blit(warningMsg, gameFunctions.placeAt((3, 35)))

        # refresh and update screen
        pygame.display.update()
        pygame.display.flip()
        # set tick rate
        clock.tick(60)


# winning message
def won():
    global rain_tick
    wonGm = False
    for i in range(2):
        if gameVariables.player_list.score[i] > gameVariables.player_lives:
            wonGm = True
            winner = gameVariables.player_list[i]
            break

    while wonGm:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    wonGm = False
                    for i in gameVariables.players.sprites():
                        i.respawn()
                    for i in gameVariables.projectiles:
                        i.kill()
                    rain_tick = gameVariables.rain_delay
                    gameVariables.raining.rainDrops = list()
                    gameVariables.player_list.score = [0, 0]

        # display message
        gameFunctions.wonMsg(winner, screen, bigfont, Color.RED)

        # update screen
        pygame.display.flip()
        clock.tick(30)


# settings menu
def settingsMen():
    menu = True
    cols = [Color.BLUE.value, Color.RED.value]

    # screensize buttons
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

    # difficulty buttons
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

    screenSize = MultipleOptions([screenSmall, screenMedium, screenLarge])
    diffs = MultipleOptions([easyDiff, mediumDiff, hardDiff])

    save = ClickButton("Save and Close", gameFunctions.placeAt((40, 90)), gameFunctions.placeAt((21, 5)), cols, win,
                       func=gameFunctions.saveAndApply)
    dele = 0

    while menu:
        # stop repeated presses
        acc = False
        if pygame.mouse.get_pressed()[0] and not dele > 0:
            acc = True
            dele = 5

        # update buttons
        diffs.update(pygame.mouse, acc)
        screenSize.update(pygame.mouse, acc)
        if save.update(pygame.mouse, acc):
            return True

        pygame.mouse.set_visible = True
        screen.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    menu = False

            # get release of mouse
            if event.type == pygame.MOUSEBUTTONUP:
                gameVariables.butonRel.gotClicked()

        # welcome message
        gameFunctions.print_text(bigfont, 50, 25, "Hello and Welcome to Bullet-Rain!", Color.RED, screen)

        # instinctual messages
        gameFunctions.print_text(win, *gameFunctions.placeAt((1, 20)), "Screen Size:", Color.WHITE, screen)
        gameFunctions.print_text(win, *gameFunctions.placeAt((1, 30)), "Difficulty:", Color.WHITE, screen)

        # draw buttons
        save.draw(screen)
        diffs.draw(screen)
        screenSize.draw(screen)

        # update screen
        pygame.display.flip()

        # decrease delay
        if dele > 0:
            dele -= 1
        clock.tick(30)


# Start
if __name__ == "__main__":  # ####################################################################
    main()

# quit
pygame.quit()
sys.exit()
