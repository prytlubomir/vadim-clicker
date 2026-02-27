from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty,
    ListProperty
)

from uix.section import Section


class TopLayout(Section):
    triggers = ListProperty()


class Background(Widget):
    line_gap = NumericProperty(7)
    line_width = NumericProperty(1)


class RootWidget(Widget):
    padding = NumericProperty(7)
    triggers = ListProperty()
