import pygame

class Ability(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__(self)
    self.image = pygame.image.load()
    self.rect = self.image.get_rect()
    self.speed = 8


  def update(self):
    self.rect.y -= self.speed