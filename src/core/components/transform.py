"""
Transform component for position, rotation, and scale.
"""
import math
from typing import Tuple

class Transform:
    """Represents position, rotation, and scale of an entity."""
    
    def __init__(self, x: float = 0, y: float = 0, rotation: float = 0, scale: float = 1):
        self.x = x
        self.y = y
        self.rotation = rotation  # in radians
        self.scale = scale
        
    @property
    def position(self) -> Tuple[float, float]:
        """Get position as tuple."""
        return (self.x, self.y)
        
    @position.setter
    def position(self, pos: Tuple[float, float]):
        """Set position from tuple."""
        self.x, self.y = pos
        
    def translate(self, dx: float, dy: float):
        """Move by the given offset."""
        self.x += dx
        self.y += dy
        
    def rotate(self, angle: float):
        """Rotate by the given angle (in radians)."""
        self.rotation += angle
        
    def get_forward_vector(self) -> Tuple[float, float]:
        """Get the forward direction vector."""
        return (math.cos(self.rotation), math.sin(self.rotation))
