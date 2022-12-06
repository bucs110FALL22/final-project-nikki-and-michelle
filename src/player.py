import pygame
from src.weapon import Weapon


class Player():
  '''Attributes for the Player.'''
  weapon_pause = 10
  
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.dogImage = pygame.transform.scale(pygame.image.load("assets/dog.png"), (140, 120)) #load and resize dog image.
    self.weaponImage = pygame.transform.scale(pygame.image.load("assets/ball.png"), (40, 40)) #load and resize weapon image.
    self.mask = pygame.mask.from_surface(self.dogImage) #creates a mask of dogImage, which tells where the image pixels are, allowing for pixel-perfect collisions. 
    self.weapons = []
    self.weaponPauseCounter = 0 #Wait a certain amount of time before player can shoot weapon again. 

  def weaponMovement(self, speed, enemies):
    '''Move weapon upwards by the speed and remove weapon upon collision with enemy or if off the screen'''
    self.weaponPause()
    for weapon in self.weapons:
      weapon.move(speed)
      if weapon.off_screen(800):
        self.weapons.remove(weapon)
      else:
        for enemy in enemies:
          if weapon.collision(enemy):
            enemies.remove(enemy)
            if weapon in self.weapons:
              self.weapons.remove(weapon)

  def weaponPause(self):
    '''Creates a break between each shooting of the weapon. '''
    if self.weaponPauseCounter >= self.weapon_pause:
      self.weaponPauseCounter = 0
    elif self.weaponPauseCounter > 0:
      self.weaponPauseCounter += 1

  def shoot(self):
    '''Make a weapon and add it to the list when spacebar is pressed.'''
    if self.weaponPauseCounter == 0:
      weapon = Weapon(self.x+50, self.y, self.weaponImage)
      self.weapons.append(weapon)
      self.weaponPauseCounter = 1

  def draw(self, window):
    '''Draw the image'''
    window.blit(self.dogImage, (self.x, self.y))
    for weapon in self.weapons:
      weapon.draw(window)

  def get_width(self):
    '''Return the width of the dog image.'''
    return self.dogImage.get_width()

  def get_height(self):
    '''Return the height of the dog image.'''
    return self.dogImage.get_height()