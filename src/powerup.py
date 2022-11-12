import pygame
import random

class Powerup(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__(self)
    self.image = pygame.image.load()
    self.rect = self.image.get_rect()
    self.speed = 3
    self.location = random.randrange()