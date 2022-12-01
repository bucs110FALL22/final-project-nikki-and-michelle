import pygame


width = 750
height = 750
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("CAT ATTACK")

class Utility(pygame.sprite.Sprite):
  cooldowns = 20
  width = 750
  height = 750

  def __init__(self, x, y, health=100):
    super().__init__(self)
    self.x = x
    self.y = y
    self.character_img = None
    self.laser_img = None
    self.lasers = []
    self.cooldown_counter = 0

  def draw(self, window): 
    self.blit(self.character_img, (self.x, self.y))
    for laser in self.lasers:
      laser.draw(window)

  def laser_movement(self, speed, object):
    self.cooldown()
    for laser in self.lasers:
      laser.move(speed)
      if laser.off_screen(height):
        self.lasers.remove
      elif laser.collision(object):
        object.health -= 10
        self.lasers.remove(laser)

  def cooldown(self):
    if self.cooldown_counter >= self.cooldowns:
      self.cooldown_counter = 0 
    elif self.cooldown_counter > 0:
      self.cooldown_counter = 1

  def get_width(self):
    return self.character_img.get_width()

  def get_height(self):
    return self.character_img.get_height()