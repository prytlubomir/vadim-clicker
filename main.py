''' Autoclicker activated by a press of a keyboard key '''
import time
from threading import Thread

import mouse
import keyboard


def toggle():
    ''' Starts and stops the clicker '''
    # The event handler could be called after the "active" is set to False,
    # but before the loop checks the condition,
    # leading to multiple threads runnign at the same time,
    # unless the thread handle is preserved between the event handler calls,
    # and checked to make sure that the previous thread id dead.
    global active
    global thread
    active = not active
    
    if active and not thread.is_alive():
        thread = Thread(target=clicker)
        thread.start()


def clicker(timeout: int = 1):
    ''' Clicks the left mouse button with a set speed '''
    while active:
        time.sleep(timeout)
        mouse.click()


def add_hotkey(hotkey: str):
    ''' Add a trigger button '''
    handler = keyboard.add_hotkey(hotkey=hotkey, callback=toggle)
    return handler


def remap_hotkey(new_hotkey: str = ''):
    ''' Change the trigger button '''
    global hotkey_handler
    keyboard.remove_hotkey(hotkey_handler)
    if new_hotkey:
        hotkey_handler = add_hotkey(new_hotkey)
        return hotkey_handler
    nh = keyboard.read_hotkey()
    hotkey_handler = add_hotkey(nh)
    return nh
        


def main():
    ''' The app '''
    global hotkey_handler
    hotkey_handler = add_hotkey('f7')
    
    print('Your current Trigger is: f7')
    while True:
        input("Press Enter to change the trigger...")
        time.sleep(0.1)
        new_trigger = remap_hotkey()
        print(f"Your new Trigger is: {new_trigger}")
    #keyboard.wait()


if __name__ == "__main__":
    active = False
    thread = Thread()
    main()
