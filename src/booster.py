import pygame

class Booster():
  '''Attribute for Booster.'''
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.boneImage = pygame.transform.scale(pygame.image.load("assets/bone.png"), (70,70))
    self.mask = pygame.mask.from_surface(self.boneImage)

  def move(self, vel):
    '''Booster moves down the screen'''
    self.y += vel

  def draw(self, window):
    '''Draw booster image.'''
    window.blit(self.boneImage, (self.x, self.y))