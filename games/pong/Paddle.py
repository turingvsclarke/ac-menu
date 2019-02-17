import pygame
import config
from GameObject import GameObject


class Paddle(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y, config.paddle_width, config.paddle_height)
        self.x = x
        self.y = y
        self.moving_up = False
        self.moving_down = False

    def draw(self, surface_to_draw_on):
        pygame.draw.rect(surface_to_draw_on, config.paddle_color, self._rect)

    def move(self, delta_x, delta_y):
        if self._rect.y < 0 and delta_y < 0:
            delta_y = 0
        elif self._rect.y + config.paddle_height > config.window_height and delta_y > 0:
            delta_y = config.window_height - (self._rect.y + config.paddle_height)
        GameObject.move(self, delta_x, delta_y)

    def reset(self):
        self._rect = pygame.rect.Rect(self.x, self.y, config.paddle_width, config.paddle_height)
        self.moving_up = False
        self.moving_down = False

    def move_up(self):
        self.move(0, -7)

    def move_down(self):
        self.move(0, 7)

    def update(self):
        if self.moving_up:
            self.move_up()
        if self.moving_down:
            self.move_down()
