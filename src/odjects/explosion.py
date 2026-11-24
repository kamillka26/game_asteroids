"""Анимация взрыва."""

from src import config


class Explosion:
    """Последовательность кадров взрыва."""

    def __init__(self, x, y, frames):
        """Создаёт взрыв в точке (x, y)."""
        self.x = x
        self.y = y
        self.frames = frames
        self.frame_index = 0
        self.timer_ms = 0

    def update(self, dt_ms):
        """Переключает кадры по таймеру."""
        self.timer_ms += dt_ms
        if self.timer_ms >= config.EXPLOSION_FRAME_MS:
            self.timer_ms = 0
            self.frame_index += 1

    @property
    def finished(self):
        """Анимация завершена."""
        return self.frame_index >= len(self.frames)
