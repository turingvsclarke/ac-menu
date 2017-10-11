import pygame
from Sprite import Sprite

class GameElement (Sprite):
  def __init__ (self, game, background_color, x, y, width, height):
    # call to super
    dimensions = (width, height)
    game_element_image = pygame.Surface (dimensions)
    game_element_image.fill (background_color)
    Sprite.__init__ (self, game_element_image, x, y, width, height)

    self.game = game

  def update (self):
    Sprite.update (self)

  def get_game (self):
    return self.game