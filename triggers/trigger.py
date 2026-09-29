'''
class Trigger - trigger prototype.

Arguments:
    - hotkey - keyboard input sequence that activates the trigger;
    - calllback - method, called on trigger activation;
    - name - name of the trigger, displayed in UI.

Methods:
    - callback - the default trigger callback;
    - map_trigger - create a keyboard listener that executes the callback on hotkey detection;
    - remap_trigger - removes the old listener, and replaces it with a new one, that listens for the new hotkey;
'''

from typing import Callable, Any
import configparser
import threading
import time

import keyboard


class PersistantSettings:
    __filepath = "./settings.ini"
    
    def __init__(self, name=''):
        self.name = name if name else type(self).__name__
        self.config = configparser.ConfigParser()
        self.config.read(self.__filepath)
        if not self.config.has_section(self.name):
            self.config[self.name] = {}
            self._update()
        self.registered = {}

    def register(self, name, transformer=lambda x: x, **kwargs):
        setting = {name: transformer}
        value = ''
        if 'value' in kwargs:
            value = kwargs['value']
            setattr(self, name, value)
        self.config[self.name][name] = str(value)
        print('setting:', setting)
        self.registered.update(setting)

    def write(self, name, value=''):
        if not self.config.has_option(self.name, name):
            raise KeyError(f'option "{name}" is not registered!')
        self.config[self.name][name] = value
        thr = threading.Thread(target=self._update, args=[name])
        thr.start()
        thr.join()
        
    def read(self, name):
        if not self.config.has_option(self.name, name):
            return None
        config_value = self.config[self.name][name]
        final_value = self.registered['name'](config_value)
        return final_value

    def _update(self, name):
        config_ = configparser.ConfigParser()
        config_.read(self.__filepath)
        for section in config_.sections():
            if section != self.name:
                for option in config_.options(section):
                    self.config[section][option] = config_[section][option]

        with open(self.__filepath, mode="w", encoding="utf-8") as configfile:
            self.config.write(configfile)
        


class Trigger:
    ''' A base class for a trigger '''

    def __init__(self, hotkey: str, callback: Callable | None = None, name: str = 'Trigger'):
        self.name = name
        self.persistant = PersistantSettings(self.name)
        self.persistant.register('hotkey')
        if callback:
            self.callback = callback
        self.map_trigger(hotkey)


    def __setattr__(self, name: str, value: Any, /) -> None:
        persistant = self.__dict__.get('persistant')
        if (
            persistant is not None
            and isinstance(name, str)
            and name in persistant.registered
        ):
            persistant.write(name, value)
        super().__setattr__(name, value)


    def callback(self) -> None:
        print('Default callback')


    def map_trigger(self, hotkey: str):
        ''' Set hotkey '''
        self.handler = keyboard.add_hotkey(hotkey, self.callback)
        self.hotkey = hotkey


    def remap_trigger(self, hotkey: str = '') -> str:
        ''' Change hotkey '''
        self.remap_proceed = True
        
        if hotkey:
            new_hotkey = hotkey
        else:
            time.sleep(0.3)
            new_hotkey = keyboard.read_hotkey()

        if self.remap_proceed:
            keyboard.remove_hotkey(self.handler)
            self.map_trigger(new_hotkey)
            return new_hotkey

    def cancel_remap(self):
        self.remap_proceed = False


    def input_progress(self):
        ''' Lookup hotkey input progress'''
        return [key.name for key in keyboard._pressed_events.values()]
