import pygame
import random
from src.player import Player
from src.enemy import Enemy

pygame.font.init()

width = 750
height = 750
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("CAT ATTACK")
background = pygame.transform.scale(pygame.image.load("assets/grass.png"), (width, height))

# class Controller:
  
  # def __init__(self):
  #   #setup pygame data

  # def mainloop(self):
    #select state loop
    
  ### below are some sample loop states ###

  # def menuloop(self):
      #event loop
      #update data
      #redraw

  # def gameoverloop(self):
      #event loop
      #update data
      #redraw

  

def main():
    run = True
    fps = 60
    level = 0
    lives = 5
    main_font = pygame.font.SysFont("ariel", 40)
    lost_font = pygame.font.SysFont("ariel", 40)

    enemies = []
    wave = 5
    enemySpeed = 1

    playerSpeed = 5
    weaponSpeed = 5

    player = Player(300, 630)

    clock = pygame.time.Clock()

    lost = False
    lostCount = 0

    def redraw_window():
        screen.blit(background, (0,0))
        # draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255))

        screen.blit(lives_label, (10, 10))
        screen.blit(level_label, (width - level_label.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(screen)

        player.draw(screen)

        if lost:
            lost_label = lost_font.render("You Lost!!", 1, (255,255,255))
            screen.blit(lost_label, (width/2 - lost_label.get_width()/2, 350))

        pygame.display.update()

    while run:
        clock.tick(fps)
        redraw_window()

        if lives <= 0:
            lost = True
            lostCount += 1

        if lost:
            if lostCount > fps * 3:
                run = False
            else:
                continue

        if len(enemies) == 0:
            level += 1
            wave += 5
            for i in range(wave):
                enemy = Enemy(random.randrange(50, width-100), random.randrange(-1500, -100))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

              
      
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - playerSpeed > 0:
            player.x -= playerSpeed
        if keys[pygame.K_RIGHT] and player.x + playerSpeed + player.get_width() < width:
            player.x += playerSpeed
        if keys[pygame.K_UP] and player.y - playerSpeed > 0:
            player.y -= playerSpeed
        if keys[pygame.K_DOWN] and player.y + playerSpeed + player.get_height() + 15 < height: 
            player.y += playerSpeed
        if keys[pygame.K_SPACE]:
            player.shoot()

        for enemy in enemies[:]:          
            enemy.move(enemySpeed)
            
            if enemy.y + enemy.get_height() > height:
              lives -= 1
              enemies.remove(enemy)

        player.move_weapons(-weaponSpeed, enemies)

def main_menu():
    title_font = pygame.font.SysFont("ariel", 70)
    run = True
    while run:
        screen.blit(background, (0,0))
        title_label = title_font.render("Press to begin", 1, (0,0,0))
        screen.blit(title_label, (width/2 - title_label.get_width()/2, 350))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()


main_menu()