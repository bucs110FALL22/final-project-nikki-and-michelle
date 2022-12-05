import pygame, sys
from src.button import Button
pygame.init()


SCREEN = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/background.jpg")

def get_font(size):
 return pygame.font.Font("assets/font.ttf", size)
  
def play():
  pygame.display.set_caption("Play")
  while True:
    PLAY_MOUSE_POS = pygame.mouse.get_pos()
    SCREEN.fill("black")
   
    
    PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
    PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
    SCREEN.blit(PLAY_TEXT, PLAY_RECT)
    PLAY_BACK = Button(image=None, pos=(640, 460), text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")
    PLAY_BACK.changeColor(PLAY_MOUSE_POS)
    PLAY_BACK.update(SCREEN)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
          main_menu()
    pygame.display.update()
  
def main_menu():
  pygame.display.set_caption("Menu")

  while True:
    SCREEN.blit(BG, (0, 0))
    MENU_MOUSE_POS = pygame.mouse.get_pos()
    MENU_TEXT = get_font(50).render("MAIN MENU", True, "white")
    MENU_RECT = MENU_TEXT.get_rect(center=(640,200))
    PLAY_BUTTON = Button(image=None, pos=(640,585), text_input="PLAY", font=get_font(40), base_color="red", hovering_color="green")
    SCREEN.blit(MENU_TEXT, MENU_RECT)
    for button in [PLAY_BUTTON]:
      button.changeColor(MENU_MOUSE_POS)
      button.update(SCREEN)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
          # clear screen before getting of main menu
          SCREEN.fill(0)          
          # break out to next main.py line
          return
    pygame.display.update()
