'''
Important outsite paths are managed here.

Nuitka stores data files in a temporary folder, created on application startup, and removed after closing.
Relative paths are relative to the exe.
'''
from pathlib import Path
import os

dir = os.path.dirname(__file__)
home = Path.home()

def in_src(path_ext):
    path = Path(os.path.join(dir, path_ext)).resolve()
    return path

def in_home(path_ext):
    path = Path(os.path.join(home, path_ext)).resolve()
    return path

settings = in_home('vadims-clicker-settings.ini')