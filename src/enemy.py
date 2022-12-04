import pygame

class Enemy():
  def __init__(self, x, y):
      self.x = x
      self.y = y
      self.cat_img = pygame.transform.scale(pygame.image.load("assets/cat.png"), (60, 50))
      self.mask = pygame.mask.from_surface(self.cat_img)

  def move(self, speed):
      self.y += speed

  def draw(self, window):
      window.blit(self.cat_img, (self.x, self.y))

  def get_width(self):
      return self.cat_img.get_width()

  def get_height(self):
      return self.cat_img.get_height()
