''' Autoclicker activated by a press of a keyboard key '''
import sys

import triggers


def main():
    ''' The app '''
    clicker = triggers.Clicker()
    holder = triggers.Holder()
    
    triggers_list = [clicker, holder]
    # triggers_dict = {}
    # for trigger in triggers_list:
    #     triggers_dict.update({trigger.name.lower(): trigger})
    # print(f"--- Triggers dict: \n\n{triggers_dict}\n\n")
    
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
