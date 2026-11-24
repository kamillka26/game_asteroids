"""Астероид."""

import random

import pygame

from src import config
from src.objects.base import GameObject
from src.utils import angle_to_vector


class Asteroid(GameObject):
    """Астероид со случайной линейной и угловой скоростью."""

    def __init__(self, x, y, image, radius=None):
        """Создаёт астероид."""
        super().__init__(x, y, image)
        if radius:
            self.image = pygame.transform.scale(image, (radius * 2, radius * 2))
        speed = random.uniform(config.ASTEROID_MIN_SPEED,
                               config.ASTEROID_MAX_SPEED)
        direction = random.uniform(0, 360)
        dx, dy = angle_to_vector(direction)
        self.vx = dx * speed
        self.vy = dy * speed
        self.angle_vel = random.uniform(
            config.ASTEROID_MIN_ANG_VEL, config.ASTEROID_MAX_ANG_VEL
        )

    def update(self, dt_ms):
        """Вращение и перемещение."""
        self.angle += self.angle_vel
        super().update(dt_ms)
