from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty,
    ListProperty
)

from uix.framebackground import FrameBackground

from uix.section import Section


class TopLayout(Section):
    triggers = ListProperty()


class RootWidget(Widget):
    padding = NumericProperty(7)
    triggers = ListProperty()
