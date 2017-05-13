import pygame
from Sprite import Sprite
from InfoPane import InfoPane
from Grid import Grid
from GameElement import GameElement
from GameUtils import GameUtils

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
GAMES_DIR = "./games/"

pygame.init ()

def initSprites ():
  # create sprite group
  sprites = pygame.sprite.Group ()

  # instantiate games
  sprite = Sprite ()

  # add sprites to sprite group
  sprites.add (sprite)

  return sprites

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
  sprites = initSprites ()

  info_pane = InfoPane ((255, 255, 255), screen_width * 0.75, 0, screen_width * 0.25, screen_height)
  sprites.add (info_pane)

  grid = Grid (GAMES_DIR, 0, 0, screen_width * 0.75, screen_height)
  sprites.add (grid)

  # start game loop
  keepGoing = True
  while keepGoing:
    for event in pygame.event.get ():
      # quit event
      if event.type == pygame.QUIT:
        keepGoing = False

      # key events
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
          print ("up")
        elif event.key == pygame.K_DOWN:
          print ("down")
        elif event.key == pygame.K_LEFT:

          print ("left")
        elif event.key == pygame.K_RIGHT:
          print ("right")

    # draw sprites on screen
    sprites.draw (screen)
    grid.update ()

    # update the display to reflect screen changes
    pygame.display.update ()

  pygame.quit ()

if __name__ == "__main__":
  main ()
