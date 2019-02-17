import pygame
from Paddle import Paddle


class Player:
    def __init__(self, player_number, paddle_position, up_key, down_key):
        self.score = 0
        x, y = paddle_position
        self.paddle_position = paddle_position
        self.paddle = Paddle(x, y)
        self.up_key = up_key
        self.down_key = down_key
        self.move_up = False
        self.move_down = False
        self.player_number = player_number
        self.label_x = x

    def update(self):
        pass

    def keyup_handler(self, key):
        if key == self.up_key:
            self.paddle.moving_up = False
        elif key == self.down_key:
            self.paddle.moving_down = False

    def keydown_handler(self, key):
        if key == self.up_key:
            self.paddle.moving_down = False
            self.paddle.moving_up = True
        elif key == self.down_key:
            self.paddle.moving_up = False
            self.paddle.moving_down = True
