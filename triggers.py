''' All the triggers '''

import time
from threading import Thread

from typing import Callable

import mouse
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



class Clicker(Trigger):
    ''' Clicker trigger '''
    
    def __init__(self, hotkey: str = 'f7', timeout: int = 1):
        super().__init__(hotkey, self.toggle, 'Clicker')
        self.active = False
        self.timeout = timeout
        self.thread = Thread(target=self.callback)
    
    
    def set_timeout(self, timeout: int) -> None:
        ''' Change delay between clicks '''
        self.timeout = timeout
    
     
    def toggle(self):
        ''' Starts and stops the clicker '''
        # The event handler could be called after the "active" is set to False,
        # but before the loop checks the condition,
        # leading to multiple threads runnign at the same time,
        # unless the thread handle is preserved between the event handler calls,
        # and checked to make sure that the previous thread id dead.
        self.active = not self.active
        
        if self.active and not self.thread.is_alive():
            self.thread = Thread(target=self.clicker)
            self.thread.start()
    
    
    def clicker(self) -> None:
        ''' Clicks the left mouse button witha set speed '''
        while self.active:
            mouse.click()
            time.sleep(self.timeout)



class Holder(Trigger):
    
    def __init__(self, hotkey: str = 'f8'):
        super().__init__(hotkey, self.holder, 'Holder')
    
    
    def holder(self):
        ''' Holds the left mouse button, until released manually '''
        mouse.press()