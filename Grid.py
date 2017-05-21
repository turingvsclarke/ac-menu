import pygame
from Sprite import Sprite
from GameUtils import GameUtils
from Page import Page
from math import ceil

ROW_LENGTH = 3
PAGE_SIZE = 12
BLUE = (0, 0 , 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Represents the game windows within the menu
class Grid (Sprite):
  def __init__ (self, games_dir, x, y, width, height):
    # call to super
    dimensions = (width, height)
    grid_image = pygame.Surface (dimensions)
    grid_image.fill (GREEN)
    Sprite.__init__ (self, grid_image, x, y, width, height)

    # retrieve all games from the games directory
    games = GameUtils.get_all (games_dir)

    self.page_index = 0
    self.page_size = PAGE_SIZE
    self.page_count = ceil (len (games) / self.page_size)
    self.pages = self.create_pages (games)

    self.page = pygame.sprite.GroupSingle ()
    self.page.add (self.pages[self.page_index])

  def create_pages (self, games):
    pages = []

    page_games = []
    for index in range (len (games)):
      # after page_games has hit the page size limit, create a page and reset page_games
      if ((index % self.page_size) == 0) and (index != 0):
        page = Page (page_games, self.rect.x, self.rect.y, self.width, self.height)
        pages.append (page)
        page_games.clear ()

      # add the game to page_games
      game = games[index]
      page_games.append (game)

    # create last page for the remaining games
    page = Page (page_games, self.rect.x, self.rect.y, self.width, self.height)
    pages.append (page)

    return pages

  def update (self):
    Sprite.update (self)

    self.pages[self.page_index].update ()
    self.page.draw (self.image)

  def get_pages (self):
    return self.pages

  def get_current_page (self):
    return self.pages[self.page_index]

  def get_page_index (self):
    return self.page_index

  def set_page_index (self, new_page_index):
    self.page_index = new_page_index
    self.page.add (self.pages[self.page_index])

  def get_page_count (self):
    return self.page_count

  def get_page_size (self):
    return self.page_size