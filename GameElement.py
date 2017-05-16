import pygame
from Sprite import Sprite

class GameElement (Sprite):
  def __init__ (self, game, color, x, y, width, height):
    # call to super
    game_element_image = pygame.Surface ((width, height))
    game_element_image.fill (color)
    Sprite.__init__ (self, game_element_image, x, y, width, height)

    self.game = game

  def update (self):
    Sprite.update (self)