import pygame
from InfoPane import InfoPane
from Grid import Grid
import Colors

GAMES_DIR = "./games/"

class Menu (object):
  def __init__(self, screen):
    object.__init__(self)

    self.screen = screen
    screen_width = screen.get_width ()
    screen_height = screen.get_height ()

    # instantiate sprites
    self.menu_sections = pygame.sprite.Group ()

    # initialize the menu grid
    grid_width = screen_width * 0.75
    self.grid = Grid (GAMES_DIR, 0, 0, grid_width, screen_height)
    self.menu_sections.add (self.grid)

    # initialize the info pane which displays the current game info
    info_pane_x = screen_width * 0.75
    info_pane_y = 0
    info_pane_width = screen_width * 0.25
    current_game = self.grid.get_current_game ()
    inf_pane_background_color = Colors.WHITE
    self.game_info_pane = InfoPane (current_game, inf_pane_background_color, info_pane_x, info_pane_y, info_pane_width,
                          screen_height)
    self.menu_sections.add (self.game_info_pane)

  def update (self):
    self.menu_sections.update ()
    self.menu_sections.draw (self.screen)

  def process (self, command):
    command.execute (self.grid)
    self.game_info_pane.set_info (self.grid.get_current_game ())