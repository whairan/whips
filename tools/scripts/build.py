#!/usr/bin/env python3
"""
Build script for different platforms.
"""
import os
import sys
import shutil
import subprocess
from pathlib import Path

def build_desktop():
    """Build for desktop using PyInstaller."""
    try:
        subprocess.run([
            sys.executable, "-m", "PyInstaller",
            "--onefile",
            "--windowed",
            "--add-data", "assets:assets",
            "--add-data", "config:config",
            "main.py"
        ], check=True)
        print("Desktop build completed successfully!")
    except subprocess.CalledProcessError:
        print("Desktop build failed!")

def build_web():
    """Build for web."""
    web_dir = Path("build/web")
    web_dir.mkdir(parents=True, exist_ok=True)
    
    # Copy assets
    if Path("assets").exists():
        shutil.copytree("assets", web_dir / "assets", dirs_exist_ok=True)
    
    # Copy source
    if Path("src").exists():
        shutil.copytree("src", web_dir / "src", dirs_exist_ok=True)
    
    # Copy main file
    if Path("main.py").exists():
        shutil.copy("main.py", web_dir)
    
    print("Web build completed! Files copied to build/web/")

def build_android():
    """Build for Android using Buildozer."""
    try:
        subprocess.run(["buildozer", "android", "debug"], check=True)
        print("Android build completed successfully!")
    except subprocess.CalledProcessError:
        print("Android build failed! Make sure Buildozer is installed.")
    except FileNotFoundError:
        print("Buildozer not found! Install with: pip install buildozer")

if __name__ == "__main__":
    platform = sys.argv[1] if len(sys.argv) > 1 else "desktop"
    
    if platform == "desktop":
        build_desktop()
    elif platform == "web":
        build_web()
    elif platform == "android":
        build_android()
    else:
        print(f"Unknown platform: {platform}")
        print("Available platforms: desktop, web, android")
