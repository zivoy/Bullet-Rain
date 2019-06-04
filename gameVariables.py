#from gameClasses import *
import gameClasses
from gameClasses import pygame

screenSize = [800, 800]
stage = pygame.image
img = "opt4.jpg"

keys = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
        "w", "x", "y", "z", "-", "_"]

actions = "jump sneak right left special1 special2".split()
player1_keys = [pygame.K_w, pygame.K_s, pygame.K_d, pygame.K_a, pygame.K_n, pygame.K_m]
player2_keys = [pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT, pygame.K_SLASH, pygame.K_RSHIFT]
player1_controls = dict(zip(actions, player1_keys))
player2_controls = dict(zip(actions, player2_keys))

gravity = 15

obstecls = list()

#scr = pygame.display.set_mode(screenSize)

players = pygame.sprite.Group()
projectiles = pygame.sprite.Group()

player_list = dict()

player_lives = 5
player_health = 20

bullet_speed = 20
rocket_speed = 30
