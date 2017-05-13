import pygame

class GameElement (pygame.sprite.Sprite):
  def __init__ (self, game, color, x, y, width, height):
    pygame.sprite.Sprite.__init__ (self)
    self.game = game

    self.image = pygame.Surface ((width, height))
    self.image.fill (color)

    self.rect = self.image.get_rect ()
    self.rect.x = x
    self.rect.y = y