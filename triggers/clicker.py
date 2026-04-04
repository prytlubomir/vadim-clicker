'''
class Clicker(Trigger) - togglable and flexible autoclicker.

Arguments:
    - hotkey - keyboard input sequence that toggles the autoclicker
    - timeout - delay between clicks.

Methods:
    set_timeout - change timeout;
    toggle - starts the clicker, if inactive, and stops if active;
    clicker - the autoclicker;
'''
from threading import Thread
from .trigger import Trigger

import time
import mouse


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