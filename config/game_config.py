"""
Game configuration management.
"""
import yaml
import os
from typing import Dict, Any

class GameConfig:
    """Manages game configuration."""
    
    def __init__(self, config_path: str = "config/game.yaml"):
        self.config_path = config_path
        self.config: Dict[str, Any] = {}
        self.load_config()
    
    def load_config(self):
        """Load configuration from YAML file."""
        try:
            with open(self.config_path, 'r') as file:
                self.config = yaml.safe_load(file)
        except FileNotFoundError:
            self.config = self.get_default_config()
            self.save_config()
    
    def get_default_config(self) -> Dict[str, Any]:
        """Get default configuration."""
        return {
            "game": {
                "title": "My Python Game",
                "version": "1.0.0",
                "target_fps": 60,
                "resolution": {
                    "width": 1280,
                    "height": 720
                }
            },
            "graphics": {
                "quality": "high",
                "fullscreen": False,
                "vsync": True
            },
            "audio": {
                "master_volume": 1.0,
                "music_volume": 0.8,
                "sfx_volume": 1.0
            }
        }
    
    def save_config(self):
        """Save configuration to file."""
        os.makedirs(os.path.dirname(self.config_path), exist_ok=True)
        with open(self.config_path, 'w') as file:
            yaml.dump(self.config, file, default_flow_style=False)
    
    def get(self, key: str, default=None):
        """Get configuration value."""
        keys = key.split('.')
        value = self.config
        for k in keys:
            value = value.get(k, default)
            if value is None:
                return default
        return value
