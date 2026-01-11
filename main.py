''' Autoclicker activated by a press of a keyboard key '''
import sys

import triggers


def main():
    ''' The app '''
    clicker = triggers.Clicker()
    holder = triggers.Holder()
    
    triggers_list = [clicker, holder]
    
    # don't forget to include "-- " separator
    if '-g' in sys.argv:
        import gui
        app = gui.VadimsClickerApp(triggers_list)
        app.run()
        return

    import tui
    tui.tui(triggers_list)


if __name__ == "__main__":
    main()
