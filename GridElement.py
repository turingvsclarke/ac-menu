import pygame
from Sprite import Sprite

# Represents the game windows within the menu
class GridElement (Sprite):
  def __init__ (self, game_element, color, x, y, width, height):
    # call to super
    grid_element_image = pygame.Surface ((width, height))
    grid_element_image.fill (color)
    Sprite.__init__ (self, grid_element_image, x, y, width, height)

    # initialize GridElement specific properties
    self.game_element = pygame.sprite.GroupSingle (game_element)

  def update (self):
    Sprite.update (self)

    self.game_element.draw (self.image)