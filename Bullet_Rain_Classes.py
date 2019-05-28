import pygame

GREEN = (20, 255, 140)
GREY = (210, 210, 210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)

class Bullet_sprite(pygame.sprite.Sprite):

    def __init__(self, color, width, height, radius, ):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        pygame.draw.circle(self.image, color, [0, 0, radius, width])

#  def __init__(self, bullspeed, hit, damage, vecor, color):
#      self.bulletspeed
#     self.hit
#    self.damage
#   self.vector
#  self.color







