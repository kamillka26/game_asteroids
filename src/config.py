"""Глобальные параметры игры «Астероиды».

Все константы собраны в одном месте для удобной настройки.
"""

# Окно
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
FPS = 60

# Корабль
SHIP_START_X = SCREEN_WIDTH // 2
SHIP_START_Y = SCREEN_HEIGHT // 2
SHIP_ROTATION_SPEED = 3        # градусов за кадр
SHIP_THRUST_ACCEL = 0.15       # ускорение при двигателе
SHIP_FRICTION = 0.995          # сопротивление среды
SHIP_MAX_SPEED = 5.0
SHIP_COOLDOWN = 250            # мс между выстрелами

# Ракеты
BULLET_SPEED = 7.0
BULLET_LIFETIME = int((SCREEN_HEIGHT / BULLET_SPEED) * 0.4)  # кадров

# Астероиды
ASTEROID_MIN_SPEED = 0.5
ASTEROID_MAX_SPEED = 2.0
ASTEROID_MIN_ANG_VEL = -2.0
ASTEROID_MAX_ANG_VEL = 2.0
ASTEROID_SPAWN_INTERVAL = 2000  # мс
ASTEROID_MIN_RADIUS = 15
ASTEROID_MAX_RADIUS = 35

# Правила
START_LIVES = 3
START_SCORE = 0

# Фон
BG_SCROLL_SPEED = 0.6
BG_ALPHA = 120

# Взрыв
EXPLOSION_FRAME_MS = 60

# Цвета
COLOR_BG = (10, 10, 30)
COLOR_SHIP = (230, 230, 230)
COLOR_ASTEROID = (150, 150, 150)
COLOR_BULLET = (255, 220, 80)
COLOR_TEXT = (220, 255, 180)

# Размеры спрайтов после масштабирования
SHIP_SPRITE_SIZE = (40, 50)       # корабль
ASTEROID_SPRITE_SIZE = (80, 80)   # базовый астероид
