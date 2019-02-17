import pygame


class GameObject:
    def __init__(self, x, y, width, height):
        self._rect = pygame.rect.Rect(x, y, width, height)

    # should be implemented by subclasses, depending on their shape
    def draw(self, surface_to_draw_on):
        pass

    def move(self, delta_x, delta_y):
        self._rect = self._rect.move(delta_x, delta_y)

    # should be implemented by subclasses, depending on their functionality
    def update(self):
        pass

    @property
    def left(self):
        return self._rect.left

    @property
    def right(self):
        return self._rect.right

    @property
    def top(self):
        return self._rect.top

    @property
    def bottom(self):
        return self._rect.bottom

    @property
    def width(self):
        return self._rect.width

    @property
    def height(self):
        return self._rect.height

    @property
    def center(self):
        return self._rect.center

    @property
    def centerx(self):
        return self._rect.centerx

    @property
    def centery(self):
        return self._rect.centery
