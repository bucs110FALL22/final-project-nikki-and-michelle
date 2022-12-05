import pygame

class Enemy():
  '''Attribute for the Enemy.'''
  cat1 = pygame.transform.scale(pygame.image.load("assets/cat1.png"), (70, 60))
  cat2 = pygame.transform.scale(pygame.image.load("assets/cat2.png"), (90, 80))
  cat3 = pygame.transform.scale(pygame.image.load("assets/cat3.png"), (80, 90))
  cat4 = pygame.transform.scale(pygame.image.load("assets/cat4.png"), (90, 70))
  Options = {"c1": (cat1), "c2": (cat2), "c3": (cat3), "c4": (cat4)}
  
  def __init__(self, x, y, options):
    self.x = x
    self.y = y
    self.catImage = self.Options[options]
    self.mask = pygame.mask.from_surface(self.catImage) #creates a mask of catImage, which tells where the image pixels are, allowing for pixel-perfect collisions. 

  def move(self, speed):
    '''Enemy moves down the screen.'''
    self.y += speed

  def draw(self, window):
    '''Draw cat image. '''
    window.blit(self.catImage, (self.x, self.y))

  def get_width(self):
    '''Return width of the cat image.'''
    return self.catImage.get_width()

  def get_height(self):
    '''Return height of the cat image'''
    return self.catImage.get_height()