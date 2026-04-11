'''
class Trigger - trigger prototype.

Arguments:
    - hotkey - keyboard input sequence that activates the trigger;
    - calllback - method, called on trigger activation;
    - name - name of the trigger, displayed in UI.

Methods:
    - callback - the default trigger callback;
    - map_trigger - create a keyboard listener that executes the callback on hotkey detection;
    - remap_trigger - removes the old listener, and replaces it with a new one, that listens for the new hotkey;
'''

from typing import Callable
import time

import keyboard


class Trigger:
    ''' A base class for a trigger '''

    def __init__(self, hotkey: str, callback: Callable | None = None, name: str = 'Trigger'):
        self.name = name
        if callback:
            self.callback = callback
        self.map_trigger(hotkey)


    def callback(self) -> None:
        print('Default callback')


    def map_trigger(self, hotkey: str):
        ''' Set hotkey '''
        self.handler = keyboard.add_hotkey(hotkey, self.callback)
        self.hotkey = hotkey


    def remap_trigger(self, hotkey: str = '') -> str:
        ''' Change hotkey '''
        keyboard.remove_hotkey(self.handler)
        if hotkey:
            self.map_trigger(hotkey)
            return hotkey
        time.sleep(0.3)
        new_hotkey = keyboard.read_hotkey()
        self.map_trigger(new_hotkey)
        return new_hotkey