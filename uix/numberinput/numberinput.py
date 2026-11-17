from kivy.uix.textinput import TextInput
from kivy.properties import (
    BooleanProperty,
    ObjectProperty
)
from kivy.clock import Clock

from uix.behaviours.input import Input


class NumberInput(Input, TextInput):
    
    multiline = BooleanProperty(False)
    input_filter = ObjectProperty('float')
    trigger = ObjectProperty()

    def _calc_timeout(self):
        return 1 / float(self.text)

    def on_trigger(self, inst, trigger, *args, **kwargs):
        print('numberinput.timeout', trigger.timeout)
        self.text = str(1 / trigger.timeout)

    def on_touch_up(self, touch):
        if self.focus and self.collide_point(*touch.pos):
            Clock.schedule_once(lambda dt: self.select_all(), 0)

    def on_focus(self, instance, focused, *args, **kwargs):
        super().on_focus(instance, focused, *args, **kwargs)
        if not focused:
            timeout = self._calc_timeout()
            self.trigger.set_timeout(timeout)