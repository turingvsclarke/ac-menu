import pygame
from Sprite import Sprite
from GameUtils import GameUtils
from Page import Page
from math import ceil
import Colors

ROW_LENGTH = 3
PAGE_SIZE = 12

# Represents the game windows within the menu
class Grid (Sprite):
  def __init__ (self, games_dir, x, y, width, height):
    # call to super
    dimensions = (width, height)
    grid_image = pygame.Surface (dimensions)
    grid_image.fill (Colors.GREEN)
    Sprite.__init__ (self, grid_image, x, y, width, height)

    # retrieve all games from the games directory
    games = GameUtils.get_all (games_dir)

    # the currently active page
    self.page_index = 0

    # number of GridElements per page
    self.page_size = PAGE_SIZE

    # number of pages
    self.page_count = int(ceil(len (games) / self.page_size))

    # list of Page objects
    self.pages = self.create_pages (games)

    # current_page is a cache of the currently active Page object
    self.current_page = self.pages[self.page_index]

    # current_page_group is used to draw the current_page object
    # pygame requires that a sprite be within a group in order to draw it
    # therefore, current_page is stored in a GroupSingle which only ever holds
    # one sprite, if you add another one it overwrites the old one
    self.current_page_group = pygame.sprite.GroupSingle ()
    self.current_page_group.add (self.current_page)

  # creates an array of Page objects generated from the list of Games
  def create_pages (self, games):
    pages = []

    page_games = []
    for index in range (len (games)):
      # after page_games has hit the page size limit, create a page and reset page_games
      if (((index % self.page_size) == 0) and (index != 0)):
        page = Page (page_games[:], self.rect.x, self.rect.y, self.width, self.height)
        pages.append (page)

        page_games.clear()

      # add the game to page_games
      game = games[index]
      page_games.append (game)

    # create last page for the remaining games
    page = Page (page_games, self.rect.x, self.rect.y, self.width, self.height)
    pages.append (page)

    return pages

  def update (self):
    Sprite.update (self)

    self.current_page.update ()
    self.current_page_group.draw (self.image)

  def get_current_game (self):
    return self.current_page.get_current_game ()

  def get_pages (self):
    return self.pages

  def get_current_page (self):
    return self.current_page

  def get_page_index (self):
    return self.page_index

  def set_page_index (self, new_page_index):
    self.page_index = new_page_index
    self.current_page = self.pages[self.page_index]
    self.current_page_group.add (self.current_page)

  def get_page_count (self):
    return self.page_count

  def get_page_size (self):
    return self.page_size