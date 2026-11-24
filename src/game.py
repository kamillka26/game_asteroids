"""Главный класс игры «Астероиды»."""

import random

import pygame

from src import config
from src.background import Background
from src.objects.asteroid import Asteroid
from src.objects.explosion import Explosion
from src.objects.ship import Ship
from src.splash import SplashScreen
from src.utils import wrap_delta


class Game:
    """Управляет игровым циклом, состояниями и всеми объектами."""

    SPLASH = "splash"
    PLAYING = "playing"

    def __init__(self, screen, assets):
        """Инициализирует игру в состоянии заставки."""
        self.screen = screen
        self.assets = assets
        self.clock = pygame.time.Clock()

        self.font_big = pygame.font.SysFont("arial", 40, bold=True)
        self.font_small = pygame.font.SysFont("arial", 24)

        self.splash = SplashScreen(self.font_big, self.font_small)
        self.background = Background(assets["bg_static"], assets["bg_dynamic"])

        self.state = self.SPLASH
        self.lives = config.START_LIVES
        self.score = config.START_SCORE

        self.ship = None
        self.asteroids = []
        self.bullets = []
        self.explosions = []
        self.spawn_timer = 0

    # Управление состоянием
    def start_game(self):
        """Начинает новую игру: сброс счётчиков и объектов."""
        self.lives = config.START_LIVES
        self.score = config.START_SCORE
        self.ship = Ship(self.assets["ship"], self.assets["ship_thrust"])
        self.asteroids.clear()
        self.bullets.clear()
        self.explosions.clear()
        self.spawn_timer = 0
        self.state = self.PLAYING

    def game_over(self):
        """Возвращает в состояние заставки, очищает объекты."""
        self.ship = None
        self.asteroids.clear()
        self.bullets.clear()
        self.explosions.clear()
        self.state = self.SPLASH

    # Обработка событий
    def handle_event(self, event):
        """Клик по заставке запускает игру; Space — выстрел."""
        if self.state == self.SPLASH:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.splash.is_click_inside(event.pos):
                    self.start_game()
        elif self.state == self.PLAYING:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if self.ship and self.ship.can_shoot():
                    self.bullets.append(self.ship.shoot())

    # Обновление
    def update(self, dt_ms):
        """Обновляет фон и объекты в зависимости от состояния."""
        self.background.update(dt_ms)

        for exp in self.explosions:
            exp.update(dt_ms)
        self.explosions = [e for e in self.explosions if not e.finished]

        if self.state != self.PLAYING:
            return

        self.ship.handle_input(pygame.key.get_pressed())
        self.ship.update(dt_ms)

        self._spawn_asteroids(dt_ms)

        for a in self.asteroids:
            a.update(dt_ms)
        for b in self.bullets:
            b.update(dt_ms)
        self.bullets = [b for b in self.bullets if not b.expired]

        self._check_collisions()

    def _spawn_asteroids(self, dt_ms):
        """Спавн астероидов с заданной частотой в случайных местах."""
        self.spawn_timer += dt_ms
        if self.spawn_timer >= config.ASTEROID_SPAWN_INTERVAL:
            self.spawn_timer = 0
            x = random.uniform(0, config.SCREEN_WIDTH)
            y = random.uniform(0, config.SCREEN_HEIGHT)
            radius = random.randint(config.ASTEROID_MIN_RADIUS,
                                    config.ASTEROID_MAX_RADIUS)
            self.asteroids.append(
                Asteroid(x, y, self.assets["asteroid"], radius)
            )

    def _check_collisions(self):
        """Проверяет столкновения с учётом тороидальной геометрии."""
        # пуля-астероид
        for b in list(self.bullets):
            for a in list(self.asteroids):
                dx, dy = wrap_delta(a.x - b.x, a.y - b.y,
                                    config.SCREEN_WIDTH, config.SCREEN_HEIGHT)
                if (dx ** 2 + dy ** 2) ** 0.5 < a.radius() + b.radius():
                    self.bullets.remove(b)
                    self.asteroids.remove(a)
                    self.explosions.append(
                        Explosion(a.x, a.y, self.assets["explosion"])
                    )
                    self.score += 1
                    break

        # корабль-астероид
        for a in list(self.asteroids):
            dx, dy = wrap_delta(a.x - self.ship.x, a.y - self.ship.y,
                                config.SCREEN_WIDTH, config.SCREEN_HEIGHT)
            if (dx ** 2 + dy ** 2) ** 0.5 < a.radius() + self.ship.radius():
                self.asteroids.remove(a)
                self.explosions.append(
                    Explosion(a.x, a.y, self.assets["explosion"])
                )
                self.lives -= 1
                if self.lives <= 0:
                    self.game_over()
                    return
                self.ship.reset()

    # Отрисовка
    def draw(self):
        """Рисует фон, объекты, HUD и заставку (если нужно)."""
        self.background.draw(self.screen)

        if self.state == self.PLAYING and self.ship:
            for a in self.asteroids:
                a.draw(self.screen)
            for b in self.bullets:
                b.draw(self.screen)
            self.ship.draw(self.screen)
            for exp in self.explosions:
                exp.draw(self.screen)

        self._draw_hud()

        if self.state == self.SPLASH:
            self.splash.draw(self.screen)

        pygame.display.flip()

    def _draw_hud(self):
        """Рисует счёт и жизни в верхних углах."""
        lives = self.font_small.render(f"Lives: {self.lives}",
                                       True, config.COLOR_TEXT)
        score = self.font_small.render(f"Score: {self.score}",
                                       True, config.COLOR_TEXT)
        self.screen.blit(lives, (20, 20))
        self.screen.blit(score,
                         (config.SCREEN_WIDTH - score.get_width() - 20, 20))

    # Главный цикл
    def run(self):
        """Запускает бесконечный игровой цикл."""
        running = True
        while running:
            dt_ms = self.clock.tick(config.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.handle_event(event)
            self.update(dt_ms)
            self.draw()
