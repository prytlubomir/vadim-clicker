import kivy
from kivy.app import App
from kivy.uix.button import Button
 
 
class VadimsClicker(App):
     
     def build(self):
         return Button(text='f7')

if __name__ == "__main__":
    VadimsClicker().run()