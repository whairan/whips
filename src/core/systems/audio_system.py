"""
Audio system for music and sound effects.
"""
import pygame.mixer

class AudioSystem:
    """Handles audio playback and management."""
    
    def __init__(self):
        self.initialized = False
        
    def initialize(self):
        """Initialize the audio system."""
        try:
            pygame.mixer.init()
            self.initialized = True
        except Exception as e:
            print(f"Failed to initialize audio: {e}")
            
    def update(self, delta_time: float):
        """Update audio system."""
        pass
        
    def play_sound(self, sound_path: str):
        """Play a sound effect."""
        if not self.initialized:
            return
            
        try:
            sound = pygame.mixer.Sound(sound_path)
            sound.play()
        except Exception as e:
            print(f"Failed to play sound {sound_path}: {e}")
            
    def play_music(self, music_path: str, loop: bool = True):
        """Play background music."""
        if not self.initialized:
            return
            
        try:
            pygame.mixer.music.load(music_path)
            pygame.mixer.music.play(-1 if loop else 0)
        except Exception as e:
            print(f"Failed to play music {music_path}: {e}")
