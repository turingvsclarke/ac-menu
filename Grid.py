import pygame
from GridElement import GridElement

# Represents the game windows within the menu
class Grid (pygame.sprite.Sprite):
  def __init__ (self, x, y, width, height):
    pygame.sprite.Sprite.__init__ (self)

    # initializing internal surface
    self.image = pygame.Surface ((width, height))
    self.image.fill ((0, 255, 0))

    # initializing internal rectangle
    self.rect = self.image.get_rect ()
    self.rect.x = x
    self.rect.y = y

    # initializing group of grid elements
    self.grid_elements = pygame.sprite.Group ()
    item_width = width / 3
    item_height = item_width * 0.75
    x_pos = 0
    y_pos = 0
    for position in range (3):
      info_pane = GridElement ((0, 0, 0), x_pos, y_pos, item_width, item_height)
      self.grid_elements.add (info_pane)
      x_pos += item_width

  def update (self):
    pygame.sprite.Sprite.update (self)

    self.grid_elements.draw (self.image)
