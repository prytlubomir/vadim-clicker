from kivy.config import Config

Config.set("kivy", "exit_on_escape", '0')
Config.set("input", "mouse", "mouse,multitouch_on_demand")  # remove red dots
Config.set("graphics", "width", "250")
Config.set("graphics", "height", "229")
Config.set("graphics", "resizable", False)
from kivy.app import App

from uix.triggerinput import TriggerInput
from uix.numberinput import NumberInput
from uix.root import RootWidget

from triggers import Trigger


class VadimsClickerApp(App):
    def __init__(self, triggers: Trigger, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def build(self):
        return RootWidget()
