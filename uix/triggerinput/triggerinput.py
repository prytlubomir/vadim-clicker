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
        self.text = trigger.hotkey

    
    def _compile_hotkey(self, progress):
        return '+'.join(progress)
    
    
    def on_press(self):
        super().on_press()
        Thread(target=self.trigger.remap_trigger).start()
        print(self.text)
    
    
    def keyboard_on_key_down(self, window, keycode, text, modifiers):
        if self.focus:
            self.text = self._compile_hotkey(self.trigger.input_progress())
    
    
    def keyboard_on_key_up(self, window, keycode):
        ''' Stop updating the text '''
        if self.focus:
            self.focus = False
    
    
    def on_focus(self, inst, focused):
        super().on_focus(inst, focused)
        if not focused:
            self.trigger.cancel_remap()
            race_counter = 0
            while self.trigger.remapping:
                race_counter += 1
            print("Race condition prevented", race_counter, "times")
            self.text = self.trigger.hotkey
