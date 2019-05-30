import pygame
import random
import gameVariables

# Initializing pygame
pygame.init()

# Create a screen called window
window = pygame.display.set_mode((800, 600))

# Title of the game
pygame.display.set_caption("Bullet Rain")

# colors
black = (0, 0, 0)
white = (255, 255, 255)
red =(255,0,0)
yellow=(255,255,0)
purple=(255,0,255)






class Bullets(pygame.sprite.Sprite):

    def __init__(self, x, y, img=gameVariables.defBull, xVel=5):
        self.super()
        self.x = x
        self.y = y
        self.xVel = xVel
        self.img = img

        self.radius = 10

    def render(self):

        pygame.draw.circle(window, yellow, ((self.x)%800, self.y), self.radius)
