from threading import Thread

from kivy.uix.button import Button
from kivy.properties import (
    StringProperty,
    ObjectProperty
)

from uix.behaviours.input import Input


class TriggerInput(Input, Button):

    hotkey = StringProperty()
    trigger = ObjectProperty()


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "text" in kwargs.keys():
            self.hotkey = kwargs["text"]

    
    def on_trigger(self, obj, trigger):
        ''' Update trigger's hotkey when the trigger is the in the layout. '''
        self.hotkey = trigger.hotkey
    
    
    def on_hotkey(self, inst, hotkey):
        self.text = hotkey

    
    def _compile_hotkey(self, progress):
        return '+'.join(progress)
    
    
    def on_press(self):
        super().on_press()
        Thread(target=self.trigger.remap_trigger).start()
        print(self.hotkey)
    
    
    def keyboard_on_key_down(self, window, keycode, text, modifiers):
        if self.focus:
            self.hotkey = self._compile_hotkey(self.trigger.input_progress())
    
    
    def keyboard_on_key_up(self, window, keycode):
        ''' Stop updating the text '''
        if self.focus:
            self.focus = False
    
    
    def on_focus(self, inst, focused):
        super().on_focus(inst, focused)
        if not focused:
            self.trigger.remap_proceed = False
            self.hotkey = self.trigger.hotkey
