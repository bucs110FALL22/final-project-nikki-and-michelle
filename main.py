import pygame
#import your controller
from src.sample_controller import Controller


def main():
  pygame.init()
    #Create an instance on your controller object
    #Call your mainloop

  c = Controller()
  c.mainloop()
  
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
