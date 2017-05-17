import pygame
from Sprite import Sprite

CYAN = (0, 255, 255)

# Represents the game windows within the menu
class GridElement (Sprite):
  def __init__ (self, game_element, color, x, y, width, height):
    # call to super
    self.unselected_image = pygame.Surface ((width, height))
    self.unselected_image.fill (color)
    self.selected_image = pygame.Surface ((width, height))
    self.selected_image.fill (CYAN)

    Sprite.__init__ (self, self.unselected_image, x, y, width, height)

    self.selected = False

    # initialize GridElement specific properties
    self.game_element = pygame.sprite.GroupSingle (game_element)

  def update (self):
    Sprite.update (self)

    self.game_element.draw (self.image)

  def toggle_selected (self):
    self.selected = not self.selected
    self.image = self.selected_image if self.selected else self.unselected_image
