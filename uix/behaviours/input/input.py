from enum import Enum

from kivy.core.window import Window
from kivy.uix.behaviors.focus import FocusBehavior
from kivy.utils import rgba
from kivy.properties import (
    ColorProperty, 
    NumericProperty, 
    ObjectProperty, 
    StringProperty
)



class InputStatus(Enum):
    idle = "idle"
    default = idle
    hover = "hover"
    active = "active"


class Input(FocusBehavior):

    value = StringProperty()
    status = ObjectProperty(InputStatus.idle)
    
    bg_color = ColorProperty(rgba((1, 1, 1, 1)))
    bg_color_idle = ColorProperty(rgba((1, 1, 1, 1)))
    bg_color_hover = ColorProperty(rgba((1, 1, 1, 1)))
    bg_color_active = ColorProperty(rgba((1, 1, 1, 1)))

    border_color = ColorProperty(rgba((1, 1, 1, 1)))
    border_color_idle = ColorProperty(rgba((1, 1, 1, 1)))
    border_color_hover = ColorProperty(rgba((1, 1, 1, 1)))
    border_color_active = ColorProperty(rgba((1, 1, 1, 1)))
    
    border_width = NumericProperty(1)
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Window.bind(on_motion=self.on_motion)
    
    
    def on_status(self, *args):
        match self.status:
            case InputStatus.idle:
                self.bg_color = self.bg_color_idle
                self.border_color = self.border_color_idle
            case InputStatus.hover:
                self.bg_color = self.bg_color_hover
                self.border_color = self.border_color_hover
            case InputStatus.active:
                self.bg_color = self.bg_color_active
                self.border_color = self.border_color_active


    def on_focus(self, inst, focused):
        if focused:
            self.status = InputStatus.active
        else:
            self.status = InputStatus.idle


    def on_motion(self, window, etype, me):
        pos_x = me.spos[0] * window.width
        pos_y = me.spos[1] * window.height
        collision = self.collide_point(pos_x, pos_y)
        if collision and self.status is InputStatus.idle:
            self.status = InputStatus.hover
            return True
        elif not collision and self.status == InputStatus.hover:
            self.status = InputStatus.idle
        return False