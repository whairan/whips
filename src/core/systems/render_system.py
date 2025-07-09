"""
Rendering system for the game.
"""
import pygame
from typing import Optional

class RenderSystem:
    """Handles all rendering operations."""
    
    def __init__(self):
        self.screen: Optional[pygame.Surface] = None
        self._engine = None  # Reference to game engine (temporary solution)
        
    def initialize(self, screen: pygame.Surface):
        """Initialize the render system."""
        self.screen = screen
        
    def render(self):
        """Render the current frame."""
        if self.screen:
            # Clear screen to black
            self.screen.fill((0, 0, 0))
            
            # Draw player if we have engine reference
            if self._engine:
                # Draw white square for player
                player_size = 50
                player_rect = (
                    self._engine.player_x - player_size // 2,
                    self._engine.player_y - player_size // 2,
                    player_size,
                    player_size
                )
                pygame.draw.rect(self.screen, (255, 255, 255), player_rect)
                
                # Draw a simple border around the player
                pygame.draw.rect(self.screen, (100, 100, 100), player_rect, 2)
            
            # Update display
            pygame.display.flip()