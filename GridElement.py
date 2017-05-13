import pygame

# Represents the game windows within the menu
class GridElement (pygame.sprite.Sprite):
  def __init__ (self, game_element, color, x, y, width, height):
    pygame.sprite.Sprite.__init__ (self)
    self.game_element = pygame.sprite.GroupSingle (game_element)

    self.image = pygame.Surface ((width, height))
    self.image.fill (color)

    self.rect = self.image.get_rect ()
    self.rect.x = x
    self.rect.y = y

  def update (self):
    pygame.sprite.Sprite.update (self)
    self.game_element.draw (self.image)