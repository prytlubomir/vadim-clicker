from .trigger import Trigger
from .clicker import Clicker
from .holder import Holder


def __dir__():
    dir_list = dir()
    dir_list.append('triggers_list')
    return dir_list


def __getattr__(name):
    if name == "triggers_list":
        global triggers_list
        triggers_list = [Clicker(), Holder()]
        return triggers_list
    else:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")