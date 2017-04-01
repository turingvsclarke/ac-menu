import pygame
from Game import Game

pygame.init ()

def initGames ():
  # create sprite group
  games = pygame.sprite.Group ()

  # instantiate games
  game = Game ()

  # add games to sprite group
  games.add (game)

  return games

def main ():
  # initialize screen
  size = (320, 240)
  screen = pygame.display.set_mode (size)
  screen.fill ((255, 255, 255))

  # set window title
  title = "Arcade Menu"
  pygame.display.set_caption (title)

  # instantiate sprites
  games = initGames ()

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
          print("up")
        elif event.key == pygame.K_DOWN:
          print("down")
        elif event.key == pygame.K_LEFT:
          print("left")
        elif event.key == pygame.K_RIGHT:
          print("right")

    # draw sprites on screen
    games.draw (screen)

    # update the display to reflect screen changes
    pygame.display.update ()

  pygame.quit ()

if __name__ == "__main__":
  main ()