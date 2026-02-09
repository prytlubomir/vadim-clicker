from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty,
    StringProperty
)

from uix.section import Section


class TopLayout(Section):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Background(Widget):
    line_gap = NumericProperty(7)
    line_width = NumericProperty(1)
    msg = StringProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class RootWidget(Widget):
    padding = NumericProperty(7)