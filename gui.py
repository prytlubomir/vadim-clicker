import kivy
from kivy.app import App
from kivy.uix.button import Button

from triggers import Trigger
 
 
class VadimsClicker(App):
     
     def __init__(self, triggers: Trigger, *args, **kwargs):
         super().__init__(*args, **kwargs)
     
     def build(self):
         return Button(text='f7')
