''' Autoclicker activated by a press of a keyboard key '''
import triggers
import tui


def main():
    ''' The app '''
    clicker = triggers.Clicker()
    holder = triggers.Holder()
    
    triggers_list = [clicker, holder]
    
    tui.tui(triggers_list)


if __name__ == "__main__":
    main()
