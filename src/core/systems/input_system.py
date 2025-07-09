"""
Input handling system.
"""
import pygame

class InputSystem:
    """Handles input from keyboard, mouse, and other devices."""
    
    def __init__(self):
        self.keys_pressed = set()
        self.keys_just_pressed = set()
        self.keys_just_released = set()
        
    def initialize(self):
        """Initialize the input system."""
        pass
        
    def process_input(self):
        """Process input events."""
        # Update key states
        current_keys = set()
        keys = pygame.key.get_pressed()
        
        for key_code in range(len(keys)):
            if keys[key_code]:
                current_keys.add(key_code)
                
        # Calculate just pressed/released
        self.keys_just_pressed = current_keys - self.keys_pressed
        self.keys_just_released = self.keys_pressed - current_keys
        self.keys_pressed = current_keys
        
    def update(self, delta_time: float):
        """Update input system."""
        pass
        
    def is_key_pressed(self, key) -> bool:
        """Check if a key is currently pressed."""
        return key in self.keys_pressed
        
    def is_key_just_pressed(self, key) -> bool:
        """Check if a key was just pressed this frame."""
        return key in self.keys_just_pressed
