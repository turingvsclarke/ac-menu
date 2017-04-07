import pygame
from Sprite import Sprite

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
  # initialize screen
  size = (320, 240)
  screen = pygame.display.set_mode (size)
  screen.fill ((255, 255, 255))

  # set Sprite title
  title = "Arcade Menu"
  pygame.display.set_caption (title)

  # instantiate sprites
  sprites = initSprites ()

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
    sprites.draw (screen)

    # update the display to reflect screen changes
    pygame.display.update ()

  pygame.quit ()

if __name__ == "__main__":
  main ()
