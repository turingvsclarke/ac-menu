import pygame

width = 32
height = 32

# Represents the game windows within the menu
class Game(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)

    self.image = pygame.Surface((width, height))
    self.image.fill((0, 0, 0))

    self.rect = self.image.get_rect()