import time
from threading import Thread

import mouse
import keyboard


def toggle():
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
    while active:
        time.sleep(timeout)
        mouse.click()


def add_hotkey(hotkey: str):
    handler = keyboard.add_hotkey(hotkey=hotkey, callback=toggle)
    return handler


def remap_hotkey(new_hotkey: str = ''):
    global hotkey_handler
    keyboard.remove_hotkey(hotkey_handler)
    if new_hotkey:
        hotkey_handler = add_hotkey(new_hotkey)
    else:
        nh = keyboard.read_hotkey()
        hotkey_handler = add_hotkey(nh)


def main():
    global hotkey_handler
    hotkey_handler = add_hotkey('f7')
    keyboard.wait()


if __name__ == "__main__":
    active = False
    thread = Thread()
    main()
