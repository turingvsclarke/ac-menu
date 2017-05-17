import pygame
from Sprite import Sprite
from GridElement import GridElement
from GameUtils import GameUtils
from GameElement import GameElement

# Represents the game windows within the menu
class Grid (Sprite):
  def __init__ (self, games_dir, x, y, width, height):
    # call to super
    grid_image = pygame.Surface ((width, height))
    grid_image.fill ((0, 255, 0))
    Sprite.__init__ (self, grid_image, x, y, width, height)

    self.row_length = 3
    self.grid_elements = pygame.sprite.Group ()
    self.selected = 0

    # retrieve all games from the games directory
    games = GameUtils.get_all (games_dir)

    # populate the grid
    self.populate_grid (games)

    # toggle first element within the grid
    elements = self.grid_elements.sprites ()
    elements[self.selected].toggle_selected ()

  def populate_grid (self, games):
    # determine the dimensions of the grid element
    item_width = self.width / self.row_length
    item_height = item_width * 0.75

    # determine the dimensions of the interior game element
    game_element_x_pos = item_width / 8
    game_element_y_pos = item_height / 8
    game_element_width = item_width * 0.75
    game_element_height = item_height * 0.75

    grid_element_color = (0, 0, 0)

    # used to calculate new elements position during population
    x_pos = 0
    y_pos = 0
    row_count = 0

    # populate array of grid elements
    for index in range (len (games)):
      game = games[index]

      # update next elements position
      if (index != 0):
        wrap = (index % self.row_length) == 0
        if wrap:
          row_count += 1
          x_pos = 0
          y_pos = row_count * item_height
        else:
          x_pos += item_width

      # add element to grid_elements sprite group
      game_element = GameElement (game, (0, 0, 255), game_element_x_pos, game_element_y_pos, game_element_width,
                                  game_element_height)
      grid_element = GridElement (game_element, grid_element_color, x_pos, y_pos, item_width, item_height)
      self.grid_elements.add (grid_element)

  def update (self):
    Sprite.update (self)
    self.grid_elements.update ()
    self.grid_elements.draw (self.image)

  def getGridElements (self):
    return self.grid_elements

  def getSelected (self):
    return self.selected

  def setSelected (self, selected):
    self.selected = selected

  def getRowLength (self):
    return self.row_length
