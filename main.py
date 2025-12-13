''' Autoclicker activated by a press of a keyboard key '''
import time
from threading import Thread

from typing import Callable

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


def holder():
    ''' Holds the left mouse button untill called again '''
    global holder_active
    if holder_active:
        mouse.release()
        holder_active = False
    mouse.press()
    holder_active = True


def add_hotkey(hotkey: str, func: Callable):
    ''' Add a trigger button '''
    handler = keyboard.add_hotkey(hotkey=hotkey, callback=func)
    return handler


def remap_hotkey(function_id: str):
    ''' Change the trigger button '''
    global trigger_map
    hotkey_handler = trigger_map[function_id][0]
    
    keyboard.remove_hotkey(hotkey_handler)
    
    # if new_hotkey:
    #     hotkey_handler = add_hotkey(new_hotkey, trigger_map[function_id][1])
    #     trigger_map[function_id][0] = hotkey_handler
    #     return hotkey_handler
    
    nh = keyboard.read_hotkey()
    hotkey_handler = add_hotkey(nh, trigger_map[function_id][1])
    trigger_map[function_id][0] = hotkey_handler

    return nh


def main():
    ''' The app '''
    clicking_trigger = add_hotkey('f7', trigger_map['0'][1])
    pressing_trigger = add_hotkey('f8', trigger_map['0'][1])
    
    with open("start_message.txt") as smf:
        sm = smf.read()
        print(sm)
    
    print('Changing the Holder trigger is currently not supported.')
    while True:
        input("Press Enter to change the trigger...")
        time.sleep(0.1)
        new_trigger = remap_hotkey('0')
        print(f"Your new Trigger is: {new_trigger}")
    #keyboard.wait()


if __name__ == "__main__":
    trigger_map = {
        '0' : [None, toggle],
        '1' : [None, holder]
    }
    holder_active = False
    active = False
    thread = Thread()
    main()
