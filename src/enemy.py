import pygame

class Enemy():
  '''Attribute for the Enemy.'''
  cat1 = pygame.transform.scale(pygame.image.load("assets/cat1.png"), (80, 70))
  cat2 = pygame.transform.scale(pygame.image.load("assets/cat2.png"), (80, 80))
  cat3 = pygame.transform.scale(pygame.image.load("assets/cat3.png"), (100, 110))
  cat4 = pygame.transform.scale(pygame.image.load("assets/cat4.png"), (80, 70))
  cat5 = pygame.transform.scale(pygame.image.load("assets/cat5.png"), (80, 70))
  cat6 = pygame.transform.scale(pygame.image.load("assets/cat6.png"), (100, 110))
  cat7 = pygame.transform.scale(pygame.image.load("assets/cat7.png"), (100, 90))
  cat8 = pygame.transform.scale(pygame.image.load("assets/cat8.png"), (80, 70))
  Options = {"c1": (cat1), "c2": (cat2), "c3": (cat3), "c4": (cat4), "c5": (cat5), "c6": (cat6), "c7": (cat7), "c8": (cat8)}

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