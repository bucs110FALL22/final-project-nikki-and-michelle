import pygame
from src.weapon import Weapon


width = 750
height = 750

class Player():
  cool_down = 20
  
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.dog_img = pygame.transform.scale(pygame.image.load("assets/dog.png"), (85, 75))
    self.weapon_img = pygame.transform.scale(pygame.image.load("assets/ball.png"), (35, 35))
    self.mask = pygame.mask.from_surface(self.dog_img)

    self.weapons = []
    self.cool_down_counter = 0
      

  def weaponMovement(self, speed, objects):
    self.cooldown()
    for weapon in self.weapons:
      weapon.move(speed)
      if weapon.off_screen(height):
        self.weapons.remove(weapon)
      else:
        for object in objects:
          if weapon.collision(object):
            objects.remove(object)
            if weapon in self.weapons:
              self.weapons.remove(weapon)


  def cooldown(self):
    if self.cooldownCount >= self.cool_down:
      self.cooldownCount = 0
    elif self.cooldownCount > 0:
      self.cooldownCount += 1

  def shoot(self):
    if self.cooldownCount == 0:
      weapon = Weapon(self.x+15, self.y, self.weapon_img)
      self.weapons.append(weapon)
      self.cooldownCount = 1

  def draw(self, window):
    window.blit(self.dog_img, (self.x, self.y))
    for weapon in self.weapons:
      weapon.draw(window)

  def get_width(self):
    return self.dog_img.get_width()

  def get_height(self):
    return self.dog_img.get_height()

  def get_width(self):
    return self.dog_img.get_width()

  def get_height(self):
    return self.dog_img.get_height()
