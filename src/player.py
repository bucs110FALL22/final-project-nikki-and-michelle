import pygame
from src.utility import Utility

class Player(Utility):
  def __init__(self, x, y, health=100):
    super().__init__(x, y, health)
    self.character_img = pygame.transform.scale(pygame.image.load("assets/dog.png"), (85, 75))
    self.laser_img = pygame.transform.scale(pygame.image.load("assets/bone.png"), (60, 50))
    self.mask = pygame.mask.from_surface(self.character_img)

  def laser_movement(self, speed, objects):
    self.cooldown()
    for laser in self.lasers:
      laser.move(speed)
      if laser.off_screen(height):
        self.lasers.remove(laser)
      else:
        for object in objects:
          if laser.collision(object):
            objects.remove(object)
            if laser in self.lasers:
              self.lasers.remove(laser)

  def healthbar(self, window):
    pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.character_img.get_height() + 10, self.character_img.get_width(), 10))
    pygame.draw.rect(window, (0,255,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health/self.max_health), 10))

  def draw(self, window):
    super().draw(window)
    self.healthbar(window)
    




    


    

  def move_left(self):
    self.rect.x -= self.speed

  def move_right(self):
    self.rect.x += self.speed


