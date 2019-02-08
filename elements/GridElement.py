import pygame
from elements.Sprite import Sprite
from config import Colors

# Represents the game windows within the menu
class GridElement (Sprite):
  def __init__ (self, game_element, background_color, x, y, width, height):
    # call to super
    dimensions = (width, height)
    self.unselected_image = pygame.Surface (dimensions)
    self.unselected_image.fill (background_color)
    self.selected_image = pygame.Surface (dimensions)
    self.selected_image.fill (Colors.CYAN)

    Sprite.__init__ (self, self.unselected_image, x, y, width, height)

    self.selected = False

    # initialize GridElement specific properties
    self.game_element = game_element
    self.game_element_group = pygame.sprite.GroupSingle (self.game_element)

  def update (self):
    Sprite.update (self)

    self.game_element_group.draw (self.image)

  def toggle_selected (self):
    self.selected = not self.selected
    self.image = self.selected_image if self.selected else self.unselected_image

  def get_game_element (self):
    return self.game_element