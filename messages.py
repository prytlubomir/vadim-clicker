from pathlib import Path
import os
# nuitka stores data files in a temporary folder, created on application startup, and removed after closing
# relative paths are relative to the exe
loc = Path(os.path.join(os.path.dirname(__file__), 'src/ascii.txt')).resolve()
f = open(loc)
start_message = f.read()
f.close()
remapping_instruction = "To change a trigger map, type in the ID of the functio you want to remap, and press the new trigger key."
