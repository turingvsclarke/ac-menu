import pygame
import config
import time
from Game import Game
from Paddle import Paddle
from Player import Player
from Ball import Ball


class Pong(Game):
    def __init__(self):
        Game.__init__(self, config.screen_size, "Pong", 60)
        self.players = []
        self.add_players()
        self.ball = Ball()
        self.add_handlers()
        self.add_objects()
        self.labels = []

    def handle_collisions(self):
        hit_time = pygame.time.get_ticks()
        if hit_time - Ball.last_hit < 100:
            return
        Ball.last_hit = hit_time


        def intersect(obj, ball):
            edges = dict(left=pygame.rect.Rect(obj.left, obj.top, 1, obj.height),
                         right=pygame.rect.Rect(obj.right, obj.top, 1, obj.height),
                         top=pygame.rect.Rect(obj.left, obj.top, obj.width, 1),
                         bottom=pygame.rect.Rect(obj.left, obj.bottom, obj.width, 1))
            collisions = set(edge for edge, rect in edges.items() if ball._rect.colliderect(rect))
            if not collisions:
                return None

            if len(collisions) == 1:
                return list(collisions)[0]

            if 'top' in collisions:
                if ball.centery >= obj.top:
                    return 'top'
                if ball.centerx < obj.left:
                    return 'left'
                else:
                    return 'right'

            if 'bottom' in collisions:
                if ball.centery >= obj.bottom:
                    return 'bottom'
                if ball.centerx < obj.left:
                    return 'left'
                else:
                    return 'right'

        for player in self.players:
            edge = intersect(player.paddle, self.ball)
            x, y = self.ball.speed
            if edge is not None:
                x *= config.ball_speed_mulitplier
            if player.player_number == 1:
                if edge == 'right':
                    self.ball.speed = (-x, y)
            elif player.player_number == 2:
                if edge == 'left':
                    self.ball.speed = (-x, y)

    def draw(self, surface_to_draw_on):
        for player in self.players:
            font = pygame.font.SysFont('Comic Sans MS', 30)
            label = font.render("Player {}: {}".format(player.player_number, player.score), False, (0, 0, 0))
            surface_to_draw_on.blit(label, (config.get_score_label_x(player), 25))

    def update(self):
        if self.ball.hit_edge_x:
            player_point = 1 if self.ball._rect.x > config.window_width / 2 else 2
            self.players[player_point - 1].score += 1
            time.sleep(1)
            for player in self.players:
                player.paddle.reset()
            self.ball.reset()
            pygame.event.clear()
        self.handle_collisions()
        if 8 in ([player.score for player in self.players]):
            self._game_over = True


    def add_players(self):
        self.players += [
            Player(1, (config.paddle_window_x_buffer, self.window.get_rect().centery - config.paddle_height / 2),
                   config.p1_up_key, config.p1_down_key),
            Player(2, (self.window.get_rect().w - config.paddle_window_x_buffer - config.paddle_width,
                       self.window.get_rect().centery - config.paddle_height / 2), config.p2_up_key, config.p2_down_key)
        ]


    def add_handlers(self):
        for player in self.players:
            super(self).add_keydown_handler(player.up_key, player.keydown_handler)
            super(self).add_keydown_handler(player.down_key, player.keydown_handler)
            super(self).add_keyup_handler(player.up_key, player.keyup_handler)
            super(self).add_keyup_handler(player.down_key, player.keyup_handler)


    def add_objects(self):
        super(self).add_objects(self.ball)
        for player in self.players:
            super(self).add_objects(player.paddle)


def main():
    Pong().run()


if __name__ == '__main__':
    main()
