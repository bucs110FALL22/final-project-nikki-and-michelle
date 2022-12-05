import pygame
from src.controller import Controller
from src import menu


def main():
  pygame.init()
    #Create an instance on your controller object
    #Call your mainloop

  menu.main_menu()

  c = Controller()
  c.main_menu()
  
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
