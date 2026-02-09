from kivy.uix.textinput import TextInput
from kivy.properties import (
    BooleanProperty,
    ObjectProperty
)

from uix.behaviours.input import Input


class NumberInput(Input, TextInput):
    
    multiline = BooleanProperty(False)
    input_filter = ObjectProperty('float')