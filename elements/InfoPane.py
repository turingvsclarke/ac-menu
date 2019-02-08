import pygame
from elements.Sprite import Sprite
from config import Colors

# Represents the game windows within the menu
class InfoPane (Sprite):
  def __init__ (self, grid, background_color, x, y, width, height, cur_page_index, page_length_index):
    # call to super
    dimensions = (width, height)
    info_pane_image = pygame.Surface (dimensions)
    self.background_color = background_color
    info_pane_image.fill (background_color)
    Sprite.__init__ (self, info_pane_image, x, y, width, height)

    self.cur_page = cur_page_index
    self.page_length = page_length_index

    self.game = grid.get_current_game()

    self.height = height
    self.width = width

    self.font = pygame.font.Font (None, 32)
    self.font_color = Colors.BLACK
    self.font_background_color = Colors.WHITE

    self.set_info (grid)

  def update (self):
    Sprite.update (self)

  def set_info (self, grid):
    self.image.fill (self.background_color)

    self.game = grid.get_current_game()

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
    
    self.cur_page = grid.get_page_index() + 1
    self.page_length = grid.get_page_count()

    #ui page bubbles
    circle_radius = 10
    small_circle_radius = 7
    circle_x = 0
    circle_y = self.height - 50

    #center of the current surface & average page #
    image_center = int(self.image.get_width()/2)
    page_center = (self.page_length-1)/2

    #draws circles for every page
    for i in range(0, self.page_length):
      circle_x = image_center + int((i-page_center)*(circle_radius + 20))
      pygame.draw.circle(self.image, pygame.Color("black"), (circle_x, circle_y), circle_radius)
      if(i == self.cur_page - 1):
        pygame.draw.circle(self.image, pygame.Color("white"), (circle_x, circle_y), small_circle_radius)
