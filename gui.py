from enum import Enum

from kivy.clock import Clock
from kivy.config import Config
from kivy.metrics import Metrics
from kivy.uix.gridlayout import GridLayout
from kivy.utils import rgba

from kivy.app import App
from kivy.properties import (
    ColorProperty,
    NumericProperty,
    ObjectProperty,
    StringProperty,
    VariableListProperty,
    BooleanProperty,
)
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget

# from kivy.config import Config
# from kivy.core import core_select_lib
from triggers import Trigger

Config.set("input", "mouse", "mouse,multitouch_on_demand")  # remove red dots
Config.set("graphics", "width", "250")
Config.set("graphics", "height", "229")
Config.set("graphics", "resizable", False)

from kivy.core.window import Window


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
        # self.fbind('on_spacing', self.on_spacing)
    
    
    def add_widget(self, widget, *args, **kwargs):
        
        if self.ids:
            # print('Add', widget, 'to', self)
            if widget not in (self.ids.layout, self.children[0]):
                # print('--- passed ---')
                # print(f'--- pos: {widget.pos} ---')
                # print(self.ids.layout)
                self.ids.layout.add_widget(widget, *args, **kwargs)
                # print(dir(self.ids.layout))
                # print(self.children)
                # print(self.ids.layout.children)
                return
            else:
                print('--- not passed ---')
                print(widget)
                print('--- layout ---')
                print(self.ids.layout)
                print('--- child ---')
                print(self.children[0])
        
        super(Section, self).add_widget(widget, *args, **kwargs)
    
    
    # def on_spacing(self, instance, value):
    #     print('spacing value:', value)



class TopLayout(Section):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



class TriggerInput(Button):
    current_trigger = StringProperty()
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
        if "text" in kwargs.keys():
            self.current_trigger = kwargs["text"]
        else:
            self.current_trigger = "f7"
            Window.bind(on_motion=self.on_motion)

    def on_status(self, *args):
        print("on_status", *args)
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
        print(self.current_trigger)

    def on_release(self):
        if self.collide_point(*Window.mouse_pos):
            self.status = ButtonStatus.hover
        else:
            self.status = ButtonStatus.idle

    # def _hover(self, window, etype, me):
    #     print(etype, self.status, me)
    #     pos_x = me.spos[0] * window.width
    #     pos_y = me.spos[1] * window.height
    #     collision = self.collide_point(pos_x, pos_y)
    #     if collision and self.status is ButtonStatus.idle:
    #         self.status = ButtonStatus.hover
    #         return True
    #     elif not collision and self.status is ButtonStatus.hover:
    #         self.status = ButtonStatus.idle
    #     return False

    def on_motion(self, window, etype, me):
        print(etype, self.status, me)
        pos_x = me.spos[0] * window.width
        pos_y = me.spos[1] * window.height
        collision = self.collide_point(pos_x, pos_y)
        if collision and self.status is ButtonStatus.idle:
            self.status = ButtonStatus.hover
            return True
        elif not collision:
            self.status = ButtonStatus.idle
        return False
        # return self._hover(window, etype, me)


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f"++++++++++++++++ {self.size} ++++++++++++++++")
        Clock.schedule_interval(self._print_density, 1)

    def _print_density(self, dt):
        print(f"dt={dt}, density={Metrics.density}, db={Metrics.dp}, sp={Metrics.sp}")


class VadimsClickerApp(App):
    def __init__(self, triggers: Trigger, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def build(self):
        return RootWidget()
