"""
Main game engine class.
"""
import pygame
import sys
from typing import Optional

from ..systems.render_system import RenderSystem
from ..systems.input_system import InputSystem
from ..systems.audio_system import AudioSystem
from ..utils.constants import *

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
        
        # Simple player for testing
        self.player_x = SCREEN_WIDTH // 2
        self.player_y = SCREEN_HEIGHT // 2
        self.player_speed = 200  # pixels per second
        
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
        if self.input_system.is_key_pressed(pygame.K_LEFT):
            self.player_x -= self.player_speed * delta_time
        if self.input_system.is_key_pressed(pygame.K_RIGHT):
            self.player_x += self.player_speed * delta_time
        if self.input_system.is_key_pressed(pygame.K_UP):
            self.player_y -= self.player_speed * delta_time
        if self.input_system.is_key_pressed(pygame.K_DOWN):
            self.player_y += self.player_speed * delta_time
            
        # Keep player on screen
        self.player_x = max(25, min(SCREEN_WIDTH - 25, self.player_x))
        self.player_y = max(25, min(SCREEN_HEIGHT - 25, self.player_y))
        
    def cleanup(self):
        """Clean up resources."""
        pygame.quit()