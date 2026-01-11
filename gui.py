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
)
from kivy.uix.boxlayout import BoxLayout
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


class TopLayout(BoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.orientation = "vertical"

    # def _iterate_layout(self, sizes):
    #     # optimize layout by preventing looking at the same attribute in a loop
    #     len_children = len(sizes)
    #     padding_left, padding_top, padding_right, padding_bottom = self.padding
    #     spacing = self.spacing
    #     orientation = self.orientation
    #     padding_x = padding_left + padding_right
    #     padding_y = padding_top + padding_bottom

    #     # calculate maximum space used by size_hint
    #     stretch_sum = 0.0
    #     has_bound = False
    #     hint = [None] * len_children
    #     # min size from all the None hint, and from those with sh_min
    #     minimum_size_bounded = 0

    #     minimum_size_x = 0
    #     minimum_size_none = padding_y + spacing * (len_children - 1)
    #     for i, ((w, h), (shw, shh), _, (shw_min, shh_min), (_, shh_max)) in enumerate(
    #         sizes
    #     ):
    #         if shh is None:
    #             minimum_size_none += h
    #         else:
    #             hint[i] = shh
    #             if shh_min:
    #                 has_bound = True
    #                 minimum_size_bounded += shh_min
    #             elif shh_max is not None:
    #                 has_bound = True
    #             stretch_sum += shh
    #         if shw is None:
    #             minimum_size_x = max(minimum_size_x, w)
    #         elif shw_min:
    #             minimum_size_x = max(minimum_size_x, shw_min)
    #     minimum_size_y = minimum_size_bounded + minimum_size_none
    #     minimum_size_x += padding_x

    #     self.minimum_size = minimum_size_x, minimum_size_y
    #     # do not move the w/h get above, it's likely to change on above line
    #     selfx = self.x
    #     selfy = self.y

    #     stretch_space = max(0.0, self.height - minimum_size_none)
    #     dim = 1

    #     if has_bound:
    #         # make sure the size_hint_min/max are not violated
    #         if stretch_space < 1e-9:
    #             # there's no space, so just set to min size or zero
    #             stretch_sum = stretch_space = 1.0

    #             for i, val in enumerate(sizes):
    #                 sh = val[1][dim]
    #                 if sh is None:
    #                     continue

    #                 sh_min = val[3][dim]
    #                 if sh_min is not None:
    #                     hint[i] = sh_min
    #                 else:
    #                     hint[i] = 0.0  # everything else is zero
    #         else:
    #             # hint gets updated in place
    #             self.layout_hint_with_bounds(
    #                 stretch_sum,
    #                 stretch_space,
    #                 minimum_size_bounded,
    #                 (val[3][dim] for val in sizes),
    #                 (elem[4][dim] for elem in sizes),
    #                 hint,
    #             )

    #     y = padding_bottom + selfy
    #     size_x = self.width - padding_x
    #     for i, (sh, ((w, h), (shw, _), pos_hint, _, _)) in enumerate(zip(hint, sizes)):
    #         cx = selfx + padding_left
    #         if sh:
    #             h = max(0.0, stretch_space * sh / stretch_sum)
    #         if shw:
    #             w = max(0, shw * size_x)
    #         for key, value in pos_hint.items():
    #             posx = value * size_x
    #             if key == "x":
    #                 cx += posx
    #             elif key == "right":
    #                 cx += posx - w
    #             elif key == "center_x":
    #                 cx += posx - (w / 2.0)
    #         yield i, cx, y, w, h
    #         y += h + spacing


    # def _iterate_layout(self, sizes):
    #     print(sizes)
    #     for i, ((w, h), _, _, _, _) in enumerate(sizes):
    #         yield i, 0, self.height - h * (i + 1), w, h


    # def do_layout(self, *largs):
    #     children = self.children
    #     if not children:
    #         l, t, r, b = self.padding
    #         self.minimum_size = l + r, t + b
    #         return

    #     children_sizes = []

    #     for i, x, y, w, h in self._iterate_layout(
    #         [
    #             (c.size, c.size_hint, c.pos_hint, c.size_hint_min, c.size_hint_max)
    #             for c in children
    #         ]
    #     ):
    #         c = children[i]
    #         children_sizes.append(h)
    #         c.pos = x, y
    #         shw, shh = c.size_hint
    #         if shw is None:
    #             if shh is not None:
    #                 c.height = h
    #         else:
    #             if shh is None:
    #                 c.width = w
    #             else:
    #                 c.size = (w, h)



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
    msg = StringProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class MyLayout(GridLayout):
    pass


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
        # Window = core_select_lib('window', [('sdl2', 'window_sdl2', 'WindowSDL')], True)
        # Window.borderless = True
        # Window.size = (250, 229)
        # Window.clearcolor = (0, 0, 5/255, 0)
        # Window.resizable = False
        # Config.set('graphics', 'resizable', False)
        # Config.set('graphics', 'width', '250')
        # Config.set('graphics', 'height', '229')
        super().__init__(*args, **kwargs)

    def build(self):
        return RootWidget()
