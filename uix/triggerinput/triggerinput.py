from threading import Thread

from kivy.uix.button import Button
from kivy.properties import (
    StringProperty,
    ObjectProperty
)

from uix.behaviours.input import Input


class TriggerInput(Input, Button):

    trigger = ObjectProperty()

    
    def on_trigger(self, obj, trigger):
        ''' Update trigger's hotkey when the trigger is the in the layout. '''
        self.text = trigger.get_hotkey()

    
    def _compile_hotkey(self, progress):
        return '+'.join(progress)
    
    
    def on_press(self):
        super().on_press()
        self.remap_finished = False
        Thread(target=self.trigger.remap_trigger).start()
        print(self.text)
    
    
    def keyboard_on_key_down(self, window, keycode, text, modifiers):
        if self.focus:
            self.text = self._compile_hotkey(self.trigger.input_progress())
    
    
    def keyboard_on_key_up(self, window, keycode):
        ''' Stop updating the text '''
        if self.focus:
            self.remap_finished = True
            self.focus = False
    
    
    def on_focus(self, inst, focused):
        super().on_focus(inst, focused)
        if not focused:
            if not self.remap_finished:
                self.trigger.cancel_remap()
            self.text = self.trigger.get_hotkey(ensure=True)
