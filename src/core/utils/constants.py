"""
Game constants and configuration.
"""

# Display settings
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
TARGET_FPS = 60

# Game settings
GAME_TITLE = "game1"
GAME_VERSION = "1.0.0"

# Colors (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Physics
GRAVITY = 9.81
PIXELS_PER_METER = 64

# Audio
MASTER_VOLUME = 1.0
MUSIC_VOLUME = 0.8
SFX_VOLUME = 1.0

# Paths
ASSETS_PATH = "assets"
AUDIO_PATH = f"{ASSETS_PATH}/audio"
GRAPHICS_PATH = f"{ASSETS_PATH}/graphics"
DATA_PATH = f"{ASSETS_PATH}/data"

# Configuration placeholder
GAME_CONFIG = {
    "initialized": True
}







import pygame

P1_CONTROLS = {
    'up': pygame.K_UP,
    'down': pygame.K_DOWN,
    'left': pygame.K_LEFT,
    'right': pygame.K_RIGHT
}

P2_CONTROLS = {
    'up': pygame.K_w,
    'down': pygame.K_s,
    'left': pygame.K_a,
    'right': pygame.K_d
}
