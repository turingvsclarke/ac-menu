import pygame
from Sprite import Sprite

class GameElement (Sprite):
  def __init__ (self, game, background_color, x, y, width, height):
    # call to super
    dimensions = (width, height)
    try:
      icon = pygame.image.load("{}icon.png".format(game.directory))
      icon = pygame.transform.scale(icon, dimensions)
    except:
      icon = pygame.Surface (dimensions)
      icon.fill (background_color)
    Sprite.__init__ (self, icon, x, y, width, height)

    self.game = game

  def update (self):
    Sprite.update (self)

  def get_game (self):
    return self.game