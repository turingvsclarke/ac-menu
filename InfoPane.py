import pygame
from Sprite import Sprite
import Colors

# Represents the game windows within the menu
class InfoPane (Sprite):
  def __init__ (self, game, background_color, x, y, width, height):
    # call to super
    self.dimensions = (width, height)
    info_pane_image = pygame.Surface (self.dimensions)
    self.background_color = background_color
    info_pane_image.fill (background_color)
    Sprite.__init__ (self, info_pane_image, x, y, width, height)

    self.game = game

    self.font = pygame.font.Font (None, 32)
    self.font_color = Colors.BLACK
    self.font_background_color = Colors.WHITE

    self.set_info (self.game)

  def update (self):
    Sprite.update (self)

  def set_info (self, game):
    self.image.fill (self.background_color)

    self.game = game

    x_offset = self.dimensions[0] / 4


    self.title = self.font.render ("Title: {}".format(self.game.title), True, self.font_color, self.font_background_color)
    self.title_rect = self.title.get_rect ()
    self.title_rect.x = x_offset
    self.image.blit (self.title, self.title_rect)

    self.author = self.font.render ("Author: {}".format(self.game.author), True, self.font_color, self.font_background_color)
    self.author_rect = self.author.get_rect ()
    self.author_rect.x = x_offset
    self.author_rect.y = self.rect.y + self.title_rect.height
    self.image.blit (self.author, self.author_rect)

    self.language = self.font.render ("Programming Language: {}".format(self.game.language), True, self.font_color, self.font_background_color)
    self.language_rect = self.language.get_rect ()
    self.language_rect.x = x_offset
    self.language_rect.y = self.author_rect.y + self.author_rect.height
    self.image.blit (self.language, self.language_rect)

def drawText(surface, text, color, rect, font, aa=False, bkg=None):
    rect = pygame.Rect(rect)
    y = rect.top
    lineSpacing = -2

    # get the height of the font
    fontHeight = font.size("Tg")[1]

    while text:
      i = 1

      # determine if the row of text will be outside our area
      if y + fontHeight > rect.bottom:
        break

      # determine maximum width of line
      while font.size(text[:i])[0] < rect.width and i < len(text):
        i += 1

      # if we've wrapped the text, then adjust the wrap to the last word
      if i < len(text):
        i = text.rfind(" ", 0, i) + 1

      # render the line and blit it to the surface
      if bkg:
        image = font.render(text[:i], 1, color, bkg)
        image.set_colorkey(bkg)
      else:
        image = font.render(text[:i], aa, color)

      surface.blit(image, (rect.left, y))
      y += fontHeight + lineSpacing

      # remove the text we just blitted
      text = text[i:]

    return text
