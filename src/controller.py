import pygame
import random
from src.player import Player
from src.enemy import Enemy
from src.booster import Booster


width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
background = pygame.transform.scale(pygame.image.load("assets/grass.png"), (width, height)) 

def get_font(size):
 return pygame.font.Font("assets/font.ttf", size)

def collide(object1, object2):
  offset_x = object2.x - object1.x
  offset_y = object2.y - object1.y
  return object1.mask.overlap(object2.mask, (offset_x, offset_y)) != None


class Controller():
  def __init__(self):
    pygame.init()
    pygame.font.init()

  def collide(object1, object2):
    offset_x = object2.x - object1.x
    offset_y = object2.y - object1.y
    return object1.mask.overlap(object2.mask, (offset_x, offset_y)) != None
      
  def main(self):
    print("running main")
    running = True
    fps = 60
    level = 0
    strength = 5
    player = Player(580, 610)
    clock = pygame.time.Clock()

    enemies = []
    numEnemy = 2
    enemySpeed = 2

    boosters = []
    numBooster = random.randrange(1,3)
    boosterSpeed = 5

    playerSpeed = 9
    weaponSpeed = 9

    mainFont = get_font(30)
    lostFont = get_font(50)

    lost = False
    lostCount = 0

    def drawScreen():
      '''Draw all the images onto the screen.'''
      screen.blit(background, (0,0)) #draw background onto the screen.
    
      for enemy in enemies: #draw the enemies (cat images).
        enemy.draw(screen) 
      
      for booster in boosters: #draw the boosters (bone images).
        booster.draw(screen) 
      
      player.draw(screen) #draw the player character (dog image).
    
      strengthLabel = mainFont.render("Strength: " + str(strength), (255,255,255), 0)
      screen.blit(strengthLabel, (10,10)) #draw text "Strength" and its number onto the screen.
    
      levelLabel = mainFont.render("Level: " + str(level), (255,255,255), 0)
      screen.blit(levelLabel, (width - levelLabel.get_width() - 10, 10)) #draw text "Level" and its number onto the screen.
    
      if lost:
        lostLabel = lostFont.render("Cat Victory", (255,255,255), 25)
        screen.blit(lostLabel, (width/2 - lostLabel.get_width()/2, 350)) #draw text "Cat Victory" onto the screen when player loses. 

      pygame.display.update()

    while running:
      clock.tick(fps)
      drawScreen() #Draw images.

      if strength <= 0:
        lost = True
        lostCount += 1

      if lost:
        if lostCount > fps*3: #Show lost screen for 3 seconds.
          running = False
        else:
          continue

      '''Increase level, enemy number, and random positioning of enemies' entrance.'''
      if len(enemies) == 0:
        level += 1
        numEnemy += 5
        for i in range (numEnemy):
          enemy = Enemy(random.randrange(50, width - 100), random.randrange(-1600,-100), random.choice(["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8"])) 
          enemies.append(enemy)

      '''Generate boosters at certain levels and random positioning of boosters' entrance.'''
      if level % 5 == 0 and len(boosters) == 0:
        numBooster += 0
        for i in range(numBooster):
          booster = Booster(random.randrange(50, width - 100), random.randrange(-1500, -100))
          boosters.append(booster)

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False

      '''Keyboard detection and restriction of the player movement boundary.'''
      keyPressed = pygame.key.get_pressed() #Return a dictionary of all the keys and tells you whether the keys are pressed or not.
      if keyPressed[pygame.K_UP] and player.y - playerSpeed > 0:
        player.y -= playerSpeed
      if keyPressed[pygame.K_DOWN] and player.y + playerSpeed + player.get_height() < height:
        player.y += playerSpeed
      if keyPressed[pygame.K_LEFT] and player.x - playerSpeed > 0:
        player.x -= playerSpeed
      if keyPressed[pygame.K_RIGHT] and player.x + playerSpeed + player.get_width() < width:
        player.x += playerSpeed
      if keyPressed[pygame.K_SPACE]:
        player.shoot()
      
      '''Decrease in strength and removal of enemy that went off screen.'''
      for enemy in enemies[:]:
        enemy.move(enemySpeed) #Enemy moves down the screen.
        if enemy.y + enemy.get_height() > height:
          strength -= 1
          enemies.remove(enemy)

      '''Increase in strength upon collision between booster image and dog image.'''
      for booster in boosters[:]:
        booster.move(boosterSpeed)
        if collide(booster, player):
          strength += 1
          boosters.remove(booster)

      player.weaponMovement(-weaponSpeed, enemies) #Move weapon upwards and remove upon collision with enemy. 

      pygame.display.update()

  def main_menu(self):
    startFont = get_font(50)
    running = True
    while running:
      screen.blit(background, (0, 0))
      startLabel = startFont.render("Press to begin...", 1, (0, 0, 0))
      screen.blit(startLabel, (width / 2 - startLabel.get_width() / 2, 350))
      pygame.display.update()
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
          self.main()
    pygame.quit()

