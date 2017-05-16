from abc import abstractmethod

import pygame

class Sprite (pygame.sprite.Sprite):
  def __init__ (self, image, x, y, width, height):
    pygame.sprite.Sprite.__init__ (self)

    self.image = image
    self.rect = self.image.get_rect ()
    self.rect.x = x
    self.rect.y = y
    self.width = width
    self.height = height

  @abstractmethod
  def update (self):
    pygame.sprite.Sprite.update (self)