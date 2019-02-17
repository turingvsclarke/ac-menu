import pygame
import sys
import config
from collections import defaultdict


class Game:
    def __init__(self, window_size, caption, frame_rate):
        self._game_over = False
        pygame.init()
        # pygame.key.set_repeat(1, 1)
        self.window = pygame.display.set_mode(window_size)
        pygame.display.set_caption(caption)
        self._clock = pygame.time.Clock()
        self._frame_rate = frame_rate
        self._color = config.screen_color
        self._objects = []
        self._keydown_handlers = defaultdict(list)
        self._keyup_handlers = defaultdict(list)

        config.init(self.window.get_rect().w, self.window.get_rect().h)

    def add_object(self, object):
        self._objects.append(object)

    def add_objects(self, *objects):
        for object in objects:
            self.add_object(object)

    def add_keydown_handler(self, key, handler):
        self._keydown_handlers[key].append(handler)

    def add_keydown_handlers(self, *handlers):
        for handler_config in handlers:
            for key, handler in handler_config:
                self.add_keydown_handler(key, handler)

    def add_keyup_handler(self, key, handler):
        self._keyup_handlers[key].append(handler)

    def add_keyup_handlers(self, *handlers):
        for handler_config in handlers:
            for key, handler in handler_config:
                self.add_keyup_handler(key, handler)

    def add_handler(self, key, handler):
        self._keydown_handlers[key].append(handler)
        self._keyup_handlers[key].append(handler)

    def add_handlers(self, *handlers):
        for handler_config in handlers:
            for key, handler in handler_config:
                self.add_keydown_handler(key, handler)
                self.add_keyup_handler(key, handler)

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_SLASH):
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if not config.a_key_has_been_pressed:
                    config.a_key_has_been_pressed = True
                for handler in self._keydown_handlers[event.key]:
                    handler(event.key)
            elif event.type == pygame.KEYUP and config.a_key_has_been_pressed:
                for handler in self._keyup_handlers[event.key]:
                    handler(event.key)

    def _draw_objects(self):
        for object in self._objects:
            object.draw(self.window)

    def _update_objects(self):
        for object in self._objects:
            object.update()

    def draw(self, surface_to_draw_on):
        pass

    def update(self):
        pass

    def run(self):
        while not self._game_over:
            self.window.fill(self._color)

            self._handle_events()
            self._update_objects()
            self._draw_objects()

            self.update()
            self.draw(self.window)

            pygame.display.update()
            self._clock.tick(self._frame_rate)
