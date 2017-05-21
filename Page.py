import pygame
from Sprite import Sprite
from GameElement import GameElement
from GridElement import GridElement

ROW_LENGTH = 3
COL_LENGTH = 4
PAGE_SIZE = 2
BLUE = (0, 0 , 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

class Page (Sprite):
  def __init__ (self, games, x, y, width, height):
    # call to super
    dimensions = (width, height)
    page_image = pygame.Surface (dimensions)
    page_image.fill (GREEN)
    Sprite.__init__ (self, page_image, x, y, width, height)

    self.games = games

    self.row_length = ROW_LENGTH
    self.col_length = COL_LENGTH
    self.navigation_elements = []
    self.grid_elements = pygame.sprite.Group ()
    self.selected = 0

    self.populate_page ()

    # toggle first element within the grid
    self.navigation_elements[self.selected].toggle_selected ()

  def populate_page (self):
    # determine the dimensions of the grid element
    item_width = self.width / self.row_length
    item_height = self.height / self.col_length

    # determine the dimensions of the interior game element
    game_element_x_pos = item_width / 8
    game_element_y_pos = item_height / 8
    game_element_width = item_width * 0.75
    game_element_height = item_height * 0.75

    # used to calculate new elements position during population
    x_pos = 0
    y_pos = 0
    row_count = 0

    # populate array of grid elements
    for index in range (len (self.games)):
      game = self.games[index]

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
      game_element = GameElement (game, BLUE, game_element_x_pos, game_element_y_pos, game_element_width,
                                  game_element_height)
      grid_element = GridElement (game_element, BLACK, x_pos, y_pos, item_width, item_height)

      # add element to the navigation element array
      self.navigation_elements.append (grid_element)

      # add element to the sprite group
      self.grid_elements.add (grid_element)

  def update (self):
    pygame.sprite.Sprite.update (self)

    self.grid_elements.update ()
    self.grid_elements.draw (self.image)

  def get_games (self):
    return self.games

  def get_navigation_elements (self):
    return self.navigation_elements

  def get_grid_elements (self):
    return self.grid_elements

  def get_selected (self):
    return self.selected

  def set_selected (self, selected):
    self.selected = selected

  def get_row_length (self):
    return self.row_length