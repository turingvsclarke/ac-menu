import pygame
from pygame.locals import*
from Menu import Menu
from InputCommandFlyweightFactory import InputCommandFlyweightFactory
import Colors
import json

config = open ("config.json").read ()
data = json.loads (config)

pygame.init ()

#configure window size to match that of machine

InfoObject=pygame.display.Info()
WINDOW_WIDTH=InfoObject.current_w
WINDOW_HEIGHT=InfoObject.current_h

def start_menu ():
  window_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
  #screen = pygame.display.set_mode ((0, 0), pygame.FULLSCREEN)
  screen = pygame.display.set_mode (window_size)
  screen.fill (Colors.WHITE)

  # set Sprite title
  title = "Arcade Menu"
  pygame.display.set_caption (title)

  menu = Menu (screen)

  factory = InputCommandFlyweightFactory ()

  # start game loop
  keepGoing = True
  while keepGoing:

    for event in pygame.event.get ():
      # quit event
      if event.type == pygame.QUIT:
        keepGoing = False
        break

      # key events
      elif event.type == pygame.KEYDOWN:
        command = None

        # navigate up
        if event.key == pygame.K_w:
          command = factory.create_up_command ()

        # navigate down
        elif event.key == pygame.K_s:
          command = factory.create_down_command ()

        # navigate left
        elif event.key == pygame.K_a:
          command = factory.create_left_command ()

        # navigate right
        elif event.key == pygame.K_d:
          command = factory.create_right_command ()

        # page left
        elif event.key == pygame.K_LEFT:
          command = factory.create_page_left_command ()

        # page right
        elif event.key == pygame.K_RIGHT:
          command = factory.create_page_right_command ()

        elif event.key == pygame.K_1:
          command = factory.create_enter_command ()

        elif event.key == pygame.K_ESCAPE:
          keepGoing = False
          break

        elif event.key == pygame.K_SLASH:
          menu.launch()

        if command is not None:
          menu.process (command)

    menu.update ()

    # update the display to reflect screen changes
    pygame.display.update ()

  pygame.quit ()

def main ():
  start_menu ()

if __name__ == "__main__":
  main ()
