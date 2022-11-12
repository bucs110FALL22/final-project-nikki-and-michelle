import pygame

class Player(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__(self)
    self.health = 3
    self.speed = 5
    self.direction = 2
    self.location = (x, y)
    self.image = pygame.image.load()
    self.rect = self.image.get_rect()
    

  def move_left(self):
    self.rect.x -= self.speed

  def move_right(self):
    self.rect.x += self.speed