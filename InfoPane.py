import pygame
from Sprite import Sprite

# Represents the game windows within the menu
class InfoPane (Sprite):
  def __init__ (self, color, x, y, width, height):
    # call to super
    dimensions = (width, height)
    info_pane_image = pygame.Surface (dimensions)
    info_pane_image.fill (color)
    Sprite.__init__ (self, info_pane_image, x, y, width, height)

  def update (self):
    Sprite.update (self)