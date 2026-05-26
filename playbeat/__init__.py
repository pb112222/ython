"""
PlayBeat Digital — Site Generator v2
A professional digital marketplace website generator.

Package structure:
  - playbeat/
    - __init__.py
    - templates/     (HTML fragments: header, footer, modals)
    - pages/         (Page generation logic)
    - config/        (Configuration and constants)
    - utils/         (Helper functions)
    - build_site.py  (Main entry point)
"""

__version__ = "2.0.0"
__author__ = "PlayBeat Team"

from pathlib import Path

# Base directories
PROJECT_ROOT = Path(__file__).parent.parent
DIST_DIR = PROJECT_ROOT / "dist"
