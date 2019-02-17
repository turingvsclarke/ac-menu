import pygame
import random
from palettable.colorbrewer import qualitative as color_pallets


def get_initial_ball_speed():
    random.seed()
    _initial_ball_direction_1 = random.choice((-1, 1))
    _initial_ball_direction_2 = random.choice((-1, 1))
    _initial_ball_speed_1 = random.randrange(3, 7)
    _initial_ball_speed_2 = 10 - _initial_ball_speed_1
    _initial_ball_speed_x = max(_initial_ball_speed_1, _initial_ball_speed_2)
    _initial_ball_speed_y = min(_initial_ball_speed_1, _initial_ball_speed_2)
    _initial_ball_speed_x *= _initial_ball_direction_1
    _initial_ball_speed_y *= _initial_ball_direction_2
    return (_initial_ball_speed_x, _initial_ball_speed_y)


colors = color_pallets.Dark2_8.colors

a_key_has_been_pressed = False

screen_width = 0
screen_height = 0
screen_size = (screen_width, screen_height)
screen_color = (180, 180, 180)

window_width = 0
window_height = 0

paddle_width = 0
paddle_height = 0
paddle_window_x_buffer = 0
paddle_window_y_buffer = 0
paddle_color = colors[0]

ball_radius = 0
ball_color = colors[1]
ball_speed_mulitplier = 1.05

p1_up_key = pygame.K_w
p1_down_key = pygame.K_s
p2_up_key = pygame.K_i
p2_down_key = pygame.K_k


def get_score_label_x(player):
    switcher = {
        1: 12,
        2: player.label_x + paddle_width + 5
    }
    return switcher[player.player_number]


def init(window_w, window_h):
    global \
        window_width, window_height, \
        paddle_width, paddle_height, \
        paddle_window_x_buffer, paddle_window_y_buffer, \
        ball_radius

    window_width = window_w
    window_height = window_h

    paddle_width = window_w / 40
    paddle_height = window_h / 6.5
    paddle_window_x_buffer = window_w / 12

    ball_radius = round(window_w / 90)
