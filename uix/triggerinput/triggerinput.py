from kivy.uix.button import Button
from kivy.properties import StringProperty

from uix.behaviours.input import Input


class TriggerInput(Input, Button):

    current_trigger = StringProperty()
    input_progress = []


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "text" in kwargs.keys():
            self.current_trigger = kwargs["text"]
        else:
            self.current_trigger = "f7"
    
    
    def on_current_trigger(self, inst, hotkey):
        self.text = hotkey
    
    
    def _compile_hotkey(self, progress):
        return '+'.join(progress)
    
    
    def on_press(self):
        super().on_press()
        print(self.current_trigger)
    
    
    def keyboard_on_key_down(self, window, keycode, text, modifiers):
        if self.input_progress and self.input_progress[-1] is keycode[1]:
            return
        self.input_progress.append(keycode[1])
        self.text = self._compile_hotkey(self.input_progress)
    
    
    def keyboard_on_key_up(self, window, keycode):
        if self.input_progress:
            self.current_trigger = self._compile_hotkey(self.input_progress)
            self.input_progress = []
            self.focus = False
    
    
    def on_focus(self, inst, focused):
        super().on_focus(inst, focused)
        if not focused and self.input_progress:
            self.input_progress = []
            self.text = self.current_trigger