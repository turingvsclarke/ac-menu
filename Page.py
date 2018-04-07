import pygame
from Sprite import Sprite
from GameElement import GameElement
from GridElement import GridElement
import Colors

ROW_LENGTH = 3
COL_LENGTH = 4
PAGE_SIZE = 12

class Page (Sprite):
  def __init__ (self, games, x, y, width, height):
    # call to super
    dimensions = (width, height)
    page_image = pygame.Surface (dimensions)
    page_image.fill (Colors.BLACK)
    Sprite.__init__ (self, page_image, x, y, width, height)

    self.games = games

    self.row_length = ROW_LENGTH
    self.col_length = COL_LENGTH

    self.grid_elements = []
    self.grid_elements_group = pygame.sprite.Group ()

    # the index of the currently selected grid element
    self.selected = 0

    self.populate_page ()

    # toggle first element within the grid
    self.grid_elements[self.selected].toggle_selected ()

  def populate_page (self):
    # determine the dimensions of the grid element
    item_width = self.width / self.row_length
    item_height = self.height / self.col_length

    # determine the dimensions of the interior game element
<<<<<<< HEAD
    game_element_x_pos = 25
    game_element_y_pos = 13
    game_element_width = item_width * 0.9
    game_element_height = item_height * 0.9
=======
    game_element_x_pos = int(item_width / 8)
    game_element_y_pos = int(item_height / 8)
    game_element_width = int(item_width * 0.75)
    game_element_height = int(item_height * 0.75)
>>>>>>> 2f46a4aa38d8d58884eaafc1de1691b3cba7e5e3

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
      game_element_background_color = Colors.BLUE
      game_element = GameElement (game, game_element_background_color, game_element_x_pos, game_element_y_pos,
                                  game_element_width, game_element_height)

      grid_element_background_color = Colors.BLACK
      grid_element = GridElement (game_element, grid_element_background_color, x_pos, y_pos, item_width, item_height)

      self.grid_elements.append (grid_element)

      # add element to the sprite group
      self.grid_elements_group.add (grid_element)

  def update (self):
    pygame.sprite.Sprite.update (self)

    # calls update on all GridElements
    self.grid_elements_group.update ()

    self.grid_elements_group.draw (self.image)

  def get_current_game (self):
    return self.games[self.selected]

  def get_games (self):
    return self.games

  def get_grid_elements (self):
    return self.grid_elements

  def get_selected (self):
    return self.selected

  def set_selected (self, selected):
    self.selected = selected

  def get_row_length (self):
    return self.row_length