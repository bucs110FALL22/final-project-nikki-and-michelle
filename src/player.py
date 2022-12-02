import pygame
from src.weapon import Weapon


width = 750
height = 750

class Player():
  COOLDOWN = 30
  
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.ship_img = pygame.transform.scale(pygame.image.load("assets/dog.png"), (85, 75))
    self.weapon_img = pygame.transform.scale(pygame.image.load("assets/ball.png"), (35, 35))
    self.mask = pygame.mask.from_surface(self.ship_img)

    self.weapons = []
    self.cool_down_counter = 0
      

  def move_weapons(self, speed, objs):
    self.cooldown()
    for weapon in self.weapons:
      weapon.move(speed)
      if weapon.off_screen(height):
        self.weapons.remove(weapon)
      else:
        for obj in objs:
          if weapon.collision(obj):
            objs.remove(obj)
            if weapon in self.weapons:
              self.weapons.remove(weapon)


  def cooldown(self):
    if self.cool_down_counter >= self.COOLDOWN:
      self.cool_down_counter = 0
    elif self.cool_down_counter > 0:
      self.cool_down_counter += 1

  def shoot(self):
    if self.cool_down_counter == 0:
      weapon = Weapon(self.x+15, self.y, self.weapon_img)
      self.weapons.append(weapon)
      self.cool_down_counter = 1


  def draw(self, window):
    window.blit(self.ship_img, (self.x, self.y))
    for weapon in self.weapons:
      weapon.draw(window)


  def get_width(self):
    return self.ship_img.get_width()

  def get_height(self):
    return self.ship_img.get_height()


  def move_left(self):
    self.rect.x -= self.speed

  def move_right(self):
    self.rect.x += self.speed


