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

  def get_image (self):
    return self.image

  def get_rect (self):
    return self.rect

  def get_x (self):
    return self.rect.x

  def get_y (self):
    return self.rect.y

  def get_width (self):
    return self.width

  def get_height (self):
    return self.height