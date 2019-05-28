import pygame

pygame.init()

GREEN = (20, 255, 140)
GREY = (210, 210, 210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)

SCREENWIDTH = 800
SCREENHEIGHT = 1000

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)

carryOn = True
clock = pygame.time.Clock()








while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False

    # Game Logic
    .update()

    # Drawing on Screen
    screen.fill(GREY)
    # Draw The Road
    pygame.draw.rect(screen, RED, [40, 0, 200, 300])

    # Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
    .draw(screen)

    # Refresh Screen
    pygame.display.flip()

    # Number of frames per secong e.g. 60
    clock.tick(60)

pygame.quit()