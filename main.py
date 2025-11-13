import time
from threading import Thread

import keyboard


active = False
thread = Thread()


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
        print(active)


def main():
    keyboard.add_hotkey('f7', toggle)
    keyboard.wait()


if __name__ == "__main__":
    main()
