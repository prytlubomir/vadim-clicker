from kivy.uix.textinput import TextInput
from kivy.properties import (
    BooleanProperty,
    ObjectProperty
)

from uix.behaviours.input import Input


class NumberInput(Input, TextInput):
    
    multiline = BooleanProperty(False)
    input_filter = ObjectProperty('float')
    trigger = ObjectProperty()


    def __init__(self, *args, **kwargs):
        print('NumberInput init')
        super().__init__(*args, **kwargs)


    def _calc_timeout(self, period):
        return 1 / period

    def on_enter(self, i, value, *args, **kwargs):
        super().on_enter(i, value, *args, **kwargs)
        print('entered:', value)

    def on_text(self, i, value, *args, **kwargs):
        # super().on_text(i, value, *args, **kwargs)
        print('texted:', value)

    def on_focus(self, i, v, *args, **kwargs):
        super().on_focus(i, v, *args, **kwargs)
        print('text input focus', v)
        if not v:
            print('Entered:', self.text)
            self.trigger.set_timeout(self._calc_timeout(float(self.text)))