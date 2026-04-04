'''
class Holder(Trigger) - press and hold LMB on hotkey

Arguments:
    - hotkey - keyboard input sequence that activates the holder.

Methods:
    - holder - the holder.
'''
from .trigger import Trigger

import mouse

class Holder(Trigger):
    
    def __init__(self, hotkey: str = 'f8'):
        super().__init__(hotkey, self.holder, 'Holder')
    
    
    def holder(self):
        ''' Holds the left mouse button, until released manually '''
        mouse.press()