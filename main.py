import time

import pynput.mouse as mouse
import pynput.keyboard as keys


activated = False


def on_release(key):
    global activated
    activated = not activated
    sk = str(key).strip()
    if isinstance(key, keys.Key):
        print('key', key.name)
    elif isinstance(key, keys.KeyCode):
        print('keycode', key.char)

def clicker(period: int = 1):
    controller = mouse.Controller()
    while True:
        if activated:
            time.sleep(period)
            controller.click(mouse.Button.left)


def main():
    listener = keys.Listener(on_release=on_release)
    listener.start()
    while True:
        pass


if __name__ == "__main__":
    main()
