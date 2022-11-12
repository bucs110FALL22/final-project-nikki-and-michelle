import pygame


class Background(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__(self)
    self.speed = 5
    self.image = pygame.image.load()
    self.rect = self.image.get_rect()

  
  def move_up(self):
    self.rect.y -= self.speed