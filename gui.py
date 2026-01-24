from enum import Enum

from kivy.config import Config

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


class ButtonStatus(Enum):
    idle = "idle"
    default = "idle"
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
    
    # def do_layout(self, *args):
    #     res = super().do_layout(*args)
    #     for c in self.ids.layout.children:
    #         print(f'--- {c.size} ---')
    #     return res



class Input(Widget):
    
    value = StringProperty()
    status = ObjectProperty(ButtonStatus.idle)
    
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
            case ButtonStatus.idle:
                self.bg_color = self.bg_color_idle
                self.border_color = self.border_color_idle
            case ButtonStatus.hover:
                self.bg_color = self.bg_color_hover
                self.border_color = self.border_color_hover
            case ButtonStatus.active:
                self.bg_color = self.bg_color_active
                self.border_color = self.border_color_active


    def on_press(self):
        self.status = ButtonStatus.active


    def on_release(self):
        if self.collide_point(*Window.mouse_pos):
            self.status = ButtonStatus.hover
        else:
            self.status = ButtonStatus.idle

    def on_motion(self, window, etype, me):
        pos_x = me.spos[0] * window.width
        pos_y = me.spos[1] * window.height
        collision = self.collide_point(pos_x, pos_y)
        if collision and self.status is ButtonStatus.idle:
            self.status = ButtonStatus.hover
            return True
        elif not collision:
            self.status = ButtonStatus.idle
        return False


class TriggerInput(Input, Button):
    current_trigger = StringProperty()


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "text" in kwargs.keys():
            self.current_trigger = kwargs["text"]
        else:
            self.current_trigger = "f7"
    
    
    def on_current_trigger(self, *args):
        self.text = self.current_trigger
    
    
    def on_press(self):
        super().on_press()
        print(self.current_trigger)


class NumberInput(Input, TextInput):
    
    multiline = BooleanProperty(False)
    input_filter = ObjectProperty('float')
    
    def on_touch_down(self, touch):
        hit = super().on_touch_down(touch)
        if hit:
            super().on_press()
        return hit


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
