"""Корабль игрока."""

import pygame

from src import config
from src.objects.base import GameObject
from src.utils import angle_to_vector


class Ship(GameObject):
    """Корабль: вращение, ускорение, стрельба."""

    def __init__(self, image, image_thrust):
        """Создаёт корабль в центре поля."""
        super().__init__(config.SHIP_START_X, config.SHIP_START_Y, image)
        self.image_idle = image
        self.image_thrust = image_thrust
        self.thrusting = False
        self.cooldown_ms = 0

    def reset(self):
        """Возвращает корабль в центр с нулевой скоростью."""
        self.x = config.SHIP_START_X
        self.y = config.SHIP_START_Y
        self.vx = self.vy = 0.0
        self.angle = 0.0
        self.thrusting = False

    def handle_input(self, keys):
        """Вращение и ускорение по нажатым клавишам."""
        if keys[pygame.K_LEFT]:
            self.angle += config.SHIP_ROTATION_SPEED
        if keys[pygame.K_RIGHT]:
            self.angle -= config.SHIP_ROTATION_SPEED
        self.thrusting = bool(keys[pygame.K_UP])
        if self.thrusting:
            dx, dy = angle_to_vector(self.angle)
            self.vx += dx * config.SHIP_THRUST_ACCEL
            self.vy += dy * config.SHIP_THRUST_ACCEL

    def update(self, dt_ms):
        """Трение, ограничение скорости, перемещение."""
        if not self.thrusting:
            self.vx *= config.SHIP_FRICTION
            self.vy *= config.SHIP_FRICTION
        speed = (self.vx ** 2 + self.vy ** 2) ** 0.5
        if speed > config.SHIP_MAX_SPEED:
            k = config.SHIP_MAX_SPEED / speed
            self.vx *= k
            self.vy *= k
        if self.cooldown_ms > 0:
            self.cooldown_ms -= dt_ms
        super().update(dt_ms)

    def can_shoot(self):
        """Готов ли к выстрелу."""
        return self.cooldown_ms <= 0

    def shoot(self):
        """Создаёт ракету из «носа» корабля."""
        from src.objects.bullet import Bullet
        dx, dy = angle_to_vector(self.angle)
        nose_x = self.x + dx * self.radius()
        nose_y = self.y + dy * self.radius()
        self.cooldown_ms = config.SHIP_COOLDOWN
        return Bullet(nose_x, nose_y, self.angle)
