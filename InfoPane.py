import pygame
from Sprite import Sprite
import Colors

# Represents the game windows within the menu
class InfoPane (Sprite):
  def __init__ (self, game, background_color, x, y, width, height, cur_page_index, page_length_index):
    # call to super
    dimensions = (width, height)
    info_pane_image = pygame.Surface (dimensions)
    self.background_color = background_color
    info_pane_image.fill (background_color)
    Sprite.__init__ (self, info_pane_image, x, y, width, height)

    self.cur_page = cur_page_index
    self.page_length = page_length_index

    self.game = game

    self.height = height
    self.width = width

    self.font = pygame.font.Font (None, 32)
    self.font_color = Colors.BLACK
    self.font_background_color = Colors.WHITE

    self.set_info (self.game)

  def update (self):
    Sprite.update (self)

  def set_info (self, game):
    self.image.fill (self.background_color)

    self.game = game

    self.title = self.font.render (self.game.title, True, self.font_color, self.font_background_color)
    self.title_rect = self.title.get_rect ()
    self.title_rect.x = 0
    self.image.blit (self.title, self.title_rect)

    self.author = self.font.render (self.game.author, True, self.font_color, self.font_background_color)
    self.author_rect = self.author.get_rect ()
    self.author_rect.x = 0
    self.author_rect.y = self.rect.y + self.title_rect.height
    self.image.blit (self.author, self.author_rect)

    self.language = self.font.render (self.game.language, True, self.font_color, self.font_background_color)
    self.language_rect = self.language.get_rect ()
    self.language_rect.x = 0
    self.language_rect.y = self.author_rect.y + self.author_rect.height
    self.image.blit (self.language, self.language_rect)

    self.page_number = self.font.render ('Page: ' + str(self.cur_page) + '/' + str(self.page_length), True, self.font_color, self.font_background_color)
    self.page_number_rect = self.title.get_rect()
    self.page_number_rect.x = 0
    self.page_number_rect.y = self.height - 50
    self.image.blit (self.page_number, self.page_number_rect)