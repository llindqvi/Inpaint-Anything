"""
Inpaint Anything: Segment Anything Meets Image Inpainting

A package for inpainting anything in images, videos and 3D scenes.
"""

__version__ = "0.1.0"
__author__ = "Tao Yu, Runseng Feng, Ruoyu Feng, Jinming Liu, Xin Jin, Wenjun Zeng, Zhibo Chen"

# Import main modules
from . import utils
from . import inpaint_anything

# Main functionality imports
try:
    from .remove_anything import main as remove_anything
    from .fill_anything import main as fill_anything  
    from .replace_anything import main as replace_anything
except ImportError:
    # Handle cases where dependencies might not be installed
    pass

__all__ = [
    "remove_anything",
    "fill_anything", 
    "replace_anything",
    "utils",
    "inpaint_anything"
]