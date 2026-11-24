"""Ракета."""

import pygame

from src import config
from src.objects.base import GameObject
from src.utils import angle_to_vector


class Bullet(GameObject):
    """Ракета с ограниченным временем жизни."""

    def __init__(self, x, y, angle):
        """Создаёт ракету."""
        surf = pygame.Surface((6, 6), pygame.SRCALPHA)
        pygame.draw.circle(surf, config.COLOR_BULLET, (3, 3), 3)
        super().__init__(x, y, surf)
        self.angle = angle
        dx, dy = angle_to_vector(angle)
        self.vx = dx * config.BULLET_SPEED
        self.vy = dy * config.BULLET_SPEED
        self.life_ms = config.BULLET_LIFETIME * (1000 // config.FPS)

    def update(self, dt_ms):
        """Двигает и уменьшает время жизни."""
        self.life_ms -= dt_ms
        super().update(dt_ms)

    @property
    def expired(self):
        """Истекло ли время жизни."""
        return self.life_ms <= 0
