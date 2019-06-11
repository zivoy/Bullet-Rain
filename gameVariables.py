import settings
from gameClasses import pygame

# sets screen size
screenSize = [800, 800]
# sets the stage
stage = pygame.image

# sets the img
img = "opt1.jpg"

# keys allowed in names
keys = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
        "w", "x", "y", "z", "-", "_"]

# sets possible actions
actions = "jump sneak right left special1 special2".split()

# lists key binds for player 1
player1_keys = [pygame.K_w, pygame.K_s, pygame.K_d, pygame.K_a, pygame.K_5, pygame.K_6]

# lists keybinds for player 2
player2_keys = [pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT, pygame.K_KP2, pygame.K_KP3]

# sets keybinds to a dictionary
player1_controls = dict(zip(actions, player1_keys))
player2_controls = dict(zip(actions, player2_keys))

# sets the gravity varible for use later
gravity = 15 * screenSize[1] / 800

# creates a variable for the obstacle to be collided with
obstecls = list()

# sets up player sprites
players = pygame.sprite.Group()
# sets up projectiles sprites(Bullets and Rockets)
projectiles = pygame.sprite.Group()
# sets up stats sprites
statuss = pygame.sprite.Group()

# sets the names of the players
player_list = dict()

# sets the number of player lives
player_lives = 5

# sets the player health
player_health = 20

# sets the bullet speed
bullet_speed = 20

# sets the rocket speed
rocket_speed = 30

# sets the rocket health
rocket_damage = 10

# sets the player health
bullet_damage = 5

# sets the player health
rocket_reload = 250

# loads the setings
settings = settings.load()

# sets the defualt settings
clip_size = 20

# sets defualt reload speed
reload_speed = 150

# sets number of bullets in bullet rain
rain_amount = 10

# Sets the atage
stage_choice = 1

# Sets the bullet rain
raining = list()

# sets up buttons
butonRel = list()

# sets the delay on the bullet rain
rain_delay = 1500

# sets bullet size
bull_size = screenSize[1] * 0.001625

# sets rocket size
roke_size = screenSize[1] * 0.00625
