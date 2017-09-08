import pygame
from InfoPane import InfoPane
from Grid import Grid
from NavigationCommandFlyweightFactory import NavigationCommandFlyweightFactory

WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 720
GAMES_DIR = "./games/"
WHITE = (255, 255, 255)

pygame.init ()

def start_menu ():
  # initialize screens
  window_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
  # screen = pygame.display.set_mode ((0, 0), pygame.FULLSCREEN)
  screen = pygame.display.set_mode (window_size)
  screen.fill (WHITE)

  screen_width = screen.get_width ()
  screen_height = screen.get_height ()

  # set Sprite title
  title = "Arcade Menu"
  pygame.display.set_caption (title)

  # instantiate sprites
  sprites = pygame.sprite.Group ()

  info_pane = InfoPane (WHITE, screen_width * 0.75, 0, screen_width * 0.25, screen_height)
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

        elif event.key == pygame.K_ESCAPE:
          keepGoing = False
          break

        if command is not None:
          command.execute (grid)

    # draw sprites on screen
    sprites.draw (screen)
    grid.update ()

    # update the display to reflect screen changes
    pygame.display.update ()

  pygame.quit ()

def main ():
  start_menu ()

if __name__ == "__main__":
  main ()
