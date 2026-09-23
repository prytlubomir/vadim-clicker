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

    def _calc_timeout(self):
        return 1 / float(self.text)

    def on_focus(self, instance, value, *args, **kwargs):
        super().on_focus(instance, value, *args, **kwargs)
        if not value:
            timeout = self._calc_timeout()
            self.trigger.set_timeout(timeout)