from .trigger import Trigger
from .clicker import Clicker
from .holder import Holder


def __dir__():
    dir_list = dir()
    dir_list.append('triggers_list')
    return dir_list


def read_config(config, section, option, fallback):
    if config.has_section(section) and config.has_option(section, option):
        return config[section][option]
    return fallback

def __getattr__(name):
    if name == "triggers_list":
        from configparser import ConfigParser
        config = ConfigParser()
        config.read('./settings.ini')

        clicker_hotkey = read_config(config, 'Clicker', 'hotkey', 'f7')
        holder_hotkey = read_config(config, 'Holder', 'hotkey', 'f8')

        global triggers_list
        triggers_list = [Clicker(clicker_hotkey), Holder(holder_hotkey)]
        return triggers_list
    else:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")