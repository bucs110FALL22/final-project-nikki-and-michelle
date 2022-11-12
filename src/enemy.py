import pygame
import random

class Enemy(pygame.sprite.Sprite): 
  def __init__(self):
    super().__init__(self)
    self.health = 1
    self.speed = 3
    self.image = pygame.image.load()
    self.rect = self.image.get_rect()

    
  def move_down(self):
    self.rect.y += random.range(-self.speed, self.speed+1)