from enum import Enum

from kivy.config import Config
from kivy.uix.behaviors.focus import FocusBehavior

Config.set("kivy", "exit_on_escape", '0')
Config.set("input", "mouse", "mouse,multitouch_on_demand")  # remove red dots
Config.set("graphics", "width", "250")
Config.set("graphics", "height", "229")
Config.set("graphics", "resizable", False)
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.metrics import Metrics, dp
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    NumericProperty,
    ObjectProperty,
    StringProperty,
    VariableListProperty,
)
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.stacklayout import StackLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.utils import rgba

from triggers import Trigger


class InputStatus(Enum):
    idle = "idle"
    default = idle
    hover = "hover"
    active = "active"


class Section(StackLayout):
    
    text = StringProperty('Section title')
    font_size = NumericProperty()
    label_height = NumericProperty()
    inner_spacing = VariableListProperty(length=2)
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    
    def add_widget(self, widget, *args, **kwargs):
        
        if self.ids:
            if widget not in (self.ids.layout, self.children[0]):
                self.ids.layout.add_widget(widget, *args, **kwargs)
                return
            else:
                print('--- not passed ---')
                print(widget)
                print('--- layout ---')
                print(self.ids.layout)
                print('--- child ---')
                print(self.children[0])
        
        super().add_widget(widget, *args, **kwargs)
        


class TopLayout(Section):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



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


class TriggerInput(Input, Button):

    current_trigger = StringProperty()
    input_progress = []


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "text" in kwargs.keys():
            self.current_trigger = kwargs["text"]
        else:
            self.current_trigger = "f7"
    
    
    def on_current_trigger(self, inst, hotkey):
        self.text = hotkey
    
    
    def _compile_hotkey(self, progress):
        return '+'.join(progress)
    
    
    def on_press(self):
        super().on_press()
        print(self.current_trigger)
    
    
    def keyboard_on_key_down(self, window, keycode, text, modifiers):
        if self.input_progress and self.input_progress[-1] is keycode[1]:
            return
        self.input_progress.append(keycode[1])
        self.text = self._compile_hotkey(self.input_progress)
    
    
    def keyboard_on_key_up(self, window, keycode):
        if self.input_progress:
            self.current_trigger = self._compile_hotkey(self.input_progress)
            self.input_progress = []
            self.focus = False
    
    
    def on_focus(self, inst, focused):
        super().on_focus(inst, focused)
        if not focused and self.input_progress:
            self.input_progress = []
            self.text = self.current_trigger



class NumberInput(Input, TextInput):
    
    multiline = BooleanProperty(False)
    input_filter = ObjectProperty('float')


class Header(Label):
    pass


class Background(Widget):
    line_gap = NumericProperty(7)
    line_width = NumericProperty(1)
    msg = StringProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



class MyLayout(StackLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def on_pos(self, *args, **kwargs):
        print(f'layout pos: {self.pos}')
    
    def on_size(self, *args, **kwargs):
        print(f'layout size: {self.size}')


class RootWidget(Widget):
    padding = NumericProperty(7)

    def _print_density(self, dt):
        print(f"dt={dt}, density={Metrics.density}, db={Metrics.dp}, sp={Metrics.sp}")


class VadimsClickerApp(App):
    def __init__(self, triggers: Trigger, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def build(self):
        return RootWidget()
