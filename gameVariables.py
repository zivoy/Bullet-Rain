#from gameClasses import *
import gameClasses
from gameClasses import pygame

screenSize = [800, 800]
stage = pygame.image
img = "opt4.jpg"

keys = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
        "w", "x", "y", "z", "-", "_"]

actions = "jump sneak right left special1 special2".split()
player1_keys = [pygame.K_w, pygame.K_s, pygame.K_d, pygame.K_a, pygame.K_q, pygame.K_e]
player2_keys = [pygame.K_KP8, pygame.K_KP5, pygame.K_KP6, pygame.K_KP4, pygame.K_KP7, pygame.K_KP9]
player1_controls = dict(zip(actions, player1_keys))
player2_controls = dict(zip(actions, player2_keys))

gravity = 15

obstecls = list()

#scr = pygame.display.set_mode(screenSize)

players = pygame.sprite.Group()
projectiles = pygame.sprite.Group()

player_list = dict()
