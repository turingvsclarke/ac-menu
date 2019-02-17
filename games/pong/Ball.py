import pygame
import config
import time
from GameObject import GameObject


class Ball(GameObject):

    last_hit = 0

    def __init__(self, speed=config.get_initial_ball_speed()):
        GameObject.__init__(self, config.window_width / 2 - config.ball_radius,
                            config.window_height / 2 - config.ball_radius, config.ball_radius * 2,
                            config.ball_radius * 2)
        self.speed = speed
        self.hit_edge_x = False

    def draw(self, surface_to_draw_on):
        pygame.draw.circle(surface_to_draw_on, config.ball_color, self._rect.center, config.ball_radius)

    def reset(self):
        self.hit_edge_x = False
        self.speed = config.get_initial_ball_speed()
        self._rect = pygame.rect.Rect(config.window_width / 2 - config.ball_radius,
                                      config.window_height / 2 - config.ball_radius, config.ball_radius * 2,
                                      config.ball_radius * 2)

    def update(self):
        delta_x, delta_y = self.speed
        if self.right > config.window_width:
            self.hit_edge_x = True
        elif self._rect.x < 0 and delta_x < 0:
            self.hit_edge_x = True
        elif self._rect.y < 0 and delta_y < 0:
            self.speed = (delta_x, -delta_y)
        elif self._rect.y + config.ball_radius * 2 > config.window_height and delta_y > 0:
            self.speed = (delta_x, -delta_y)
        self.move(delta_x, delta_y)
