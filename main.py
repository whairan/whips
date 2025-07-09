#!/usr/bin/env python3
"""
Main entry point for the game.
"""
import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.core.engine.game_engine import GameEngine
from src.core.utils.constants import GAME_CONFIG

def main():
    """Main function to start the game."""
    try:
        engine = GameEngine()
        if engine.initialize():
            engine.run()
        else:
            print("Failed to initialize game engine")
    except KeyboardInterrupt:
        print("Game interrupted by user")
    except Exception as e:
        print(f"Game crashed: {e}")
        raise
    finally:
        if 'engine' in locals():
            engine.cleanup()

if __name__ == "__main__":
    main()
