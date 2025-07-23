"""
Main game engine class.
"""
import pygame
import sys
from typing import Optional
from game.entities.player import Player

from ..systems.render_system import RenderSystem
from ..systems.input_system import InputSystem
from ..systems.audio_system import AudioSystem
from ..utils.constants import *


from src.core.utils.constants import (
    SCREEN_WIDTH, SCREEN_HEIGHT, TARGET_FPS, GAME_TITLE,
    RED, BLUE, P1_CONTROLS, P2_CONTROLS
)


class GameEngine:
    """Main game engine that manages all systems."""
    
    def __init__(self):
        self.running = False
        self.clock = pygame.time.Clock()
        self.screen: Optional[pygame.Surface] = None
        
        # Systems
        self.render_system = RenderSystem()
        self.input_system = InputSystem()
        self.audio_system = AudioSystem()
        
        # # Simple player for testing
        # self.player_x = SCREEN_WIDTH // 2
        # self.player_y = SCREEN_HEIGHT // 2
        # self.player_speed = 200  # pixels per second
        
        #testing with simple 2 players
        # self.player1 = Player(
        #     100, 100, 20, 'red', 3,
        #     controls={'up': pygame.K_UP, 'down': pygame.K_DOWN,
        #               'left': pygame.K_LEFT, 'right': pygame.K_RIGHT}
        # )
        # self.player2 = Player(
        #     200, 100, 20, 'green', 5,
        #     controls={'up': pygame.K_w, 'down': pygame.K_s,
        #               'left': pygame.K_a, 'right': pygame.K_d}
        # # )


        # self.player1 = Player((100, 100), P1_CONTROLS, RED)
        # self.player2 = Player((700, 500), P2_CONTROLS, BLUE)
        # self.player1 = Player((100, 100), 20, RED, 3, P1_CONTROLS)
        # self.player2 = Player((700, 500), 20, BLUE, 5, P2_CONTROLS)
        self.player1 = Player(100, 100, 20, RED, 3, P1_CONTROLS)
        self.player2 = Player(700, 500, 20, BLUE, 5, P2_CONTROLS)



        # Add this line:
        self.players = pygame.sprite.Group(self.player1, self.player2)



        
    def initialize(self) -> bool:
        """Initialize the game engine."""
        try:
            pygame.init()
            self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
            pygame.display.set_caption(GAME_TITLE)
            
            # Initialize systems
            self.render_system.initialize(self.screen)
            self.input_system.initialize()
            self.audio_system.initialize()
            
            # Pass engine reference to render system (temporary solution)
            self.render_system._engine = self
            
            return True
        except Exception as e:
            print(f"Failed to initialize engine: {e}")
            return False
    
    def run(self):
        """Main game loop."""
        self.running = True
        
        while self.running:
            delta_time = self.clock.tick(TARGET_FPS) / 1000.0
            
            # Process input
            self.input_system.process_input()
            
            # Update game logic
            self.update(delta_time)
            
            # Render
            self.render_system.render()
            
            # Check for quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
    
    def update(self, delta_time: float):
        """Update game logic."""
        # Update systems
        self.input_system.update(delta_time)
        self.audio_system.update(delta_time)
        
        # Simple player movement with arrow keys
        # if self.input_system.is_key_pressed(pygame.K_LEFT):
        #     self.player_x -= self.player_speed * delta_time
        # if self.input_system.is_key_pressed(pygame.K_RIGHT):
        #     self.player_x += self.player_speed * delta_time
        # if self.input_system.is_key_pressed(pygame.K_UP):
        #     self.player_y -= self.player_speed * delta_time
        # if self.input_system.is_key_pressed(pygame.K_DOWN):
        #     self.player_y += self.player_speed * delta_time
            
        # Keep player on screen
        # self.player_x = max(25, min(SCREEN_WIDTH - 25, self.player_x))
        # self.player_y = max(25, min(SCREEN_HEIGHT - 25, self.player_y))
        

        # Update players
        self.players.update()

        # Clamp players to screen bounds
        for player in self.players:
            x, y = player.pos.x, player.pos.y
            r = player.radius
            x = max(r, min(SCREEN_WIDTH - r, x))
            y = max(r, min(SCREEN_HEIGHT - r, y))
            player.pos = pygame.Vector2(x, y)
            player.rect.center = player.pos


    def cleanup(self):
        """Clean up resources."""
        pygame.quit()