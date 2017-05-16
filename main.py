import pygame
from InfoPane import InfoPane
from Grid import Grid
from NavigationCommandFlyweightFactory import NavigationCommandFlyweightFactory

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
GAMES_DIR = "./games/"

pygame.init ()

def main ():
  # initialize screene
  window_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
  # screen = pygame.display.set_mode ((0, 0), pygame.FULLSCREEN)
  screen = pygame.display.set_mode (window_size)
  screen.fill ((255, 255, 255))

  screen_width = screen.get_width ()
  screen_height = screen.get_height ()

  # set Sprite title
  title = "Arcade Menu"
  pygame.display.set_caption (title)

  # instantiate sprites
  sprites = pygame.sprite.Group ()

  info_pane = InfoPane ((255, 255, 255), screen_width * 0.75, 0, screen_width * 0.25, screen_height)
  sprites.add (info_pane)

  grid = Grid (GAMES_DIR, 0, 0, screen_width * 0.75, screen_height)
  sprites.add (grid)

  factory = NavigationCommandFlyweightFactory ()

  # start game loop
  keepGoing = True
  while keepGoing:

    for event in pygame.event.get ():
      command = None

      # quit event
      if event.type == pygame.QUIT:
        keepGoing = False
        break

      # key events
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
          # navigate up
          factory.create_up_command ().execute (grid)
        elif event.key == pygame.K_DOWN:
          # navigate down
          factory.create_down_command ().execute (grid)
        elif event.key == pygame.K_LEFT:
          # navigate left
          factory.create_left_command ().execute (grid)
        elif event.key == pygame.K_RIGHT:
          # navigate right
          factory.create_right_command ().execute (grid)

    # draw sprites on screen
    sprites.draw (screen)
    grid.update ()

    # update the display to reflect screen changes
    pygame.display.update ()

  pygame.quit ()

if __name__ == "__main__":
  main ()
