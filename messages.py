import loc
# loc = Path(os.path.join(os.path.dirname(__file__), 'src/ascii.txt')).resolve()
path = loc.in_src('src/ascii.txt')
f = open(path)
start_message = f.read()
f.close()
# remapping_instruction = "To change a trigger map, type in the ID of the functio you want to remap, and press the new trigger key."
remapping_instruction = "Remap - Enter the function ID and press the new trigger key."
quit_instruction = 'Quit - Enter "q".'
