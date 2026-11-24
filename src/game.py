"""Главный класс игры."""

import random

import pygame

from src import config
from src.background import Background
from src.objects.asteroid import Asteroid
from src.objects.explosion import Explosion
from src.objects.ship import Ship
from src.utils import wrap_delta


class Game:
    """Управляет игровым циклом и объектами."""

    def __init__(self, screen, assets):
        """Инициализирует игру."""
        self.screen = screen
        self.assets = assets
        self.clock = pygame.time.Clock()
        self.background = Background(assets["bg_static"], assets["bg_dynamic"])
        self.ship = Ship(assets["ship"], assets["ship_thrust"])
        self.asteroids = []
        self.bullets = []
        self.explosions = []
        self.spawn_timer = 0

    def update(self, dt_ms):
        """Обновляет фон и объекты."""
        self.background.update(dt_ms)
        self.ship.handle_input(pygame.key.get_pressed())
        self.ship.update(dt_ms)

        self.spawn_timer += dt_ms
        if self.spawn_timer >= config.ASTEROID_SPAWN_INTERVAL:
            self.spawn_timer = 0
            x = random.uniform(0, config.SCREEN_WIDTH)
            y = random.uniform(0, config.SCREEN_HEIGHT)
            r = random.randint(config.ASTEROID_MIN_RADIUS,
                               config.ASTEROID_MAX_RADIUS)
            self.asteroids.append(Asteroid(x, y, self.assets["asteroid"], r))

        for a in self.asteroids:
            a.update(dt_ms)
        for b in self.bullets:
            b.update(dt_ms)
        self.bullets = [b for b in self.bullets if not b.expired]

        for exp in self.explosions:
            exp.update(dt_ms)
        self.explosions = [e for e in self.explosions if not e.finished]

    def draw(self):
        """Рисует всё на экране."""
        self.background.draw(self.screen)
        for a in self.asteroids:
            a.draw(self.screen)
        for b in self.bullets:
            b.draw(self.screen)
        self.ship.draw(self.screen)
        for exp in self.explosions:
            exp.draw(self.screen)
        pygame.display.flip()

    def run(self):
        """Главный цикл."""
        running = True
        while running:
            dt_ms = self.clock.tick(config.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.update(dt_ms)
            self.draw()
