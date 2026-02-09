from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label

from kivy.properties import (
    StringProperty,
    NumericProperty,
    VariableListProperty
)


class Header(Label):
    pass


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