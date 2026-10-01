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


class Config:
    __filepath = "./settings.ini"
    
    def __init__(self, section=''):
        self.section = section if section else type(self).__name__
        self.config = self.read_file()
        if not self.config.has_section(self.section):
            self.config[self.section] = {}
            self._update()
        self.options = {}

    def read_file(self):
        config = configparser.ConfigParser()
        config.read(self.__filepath)
        return config

    def add_option(self, option, transformer=lambda x: x, **kwargs):
        setting = {option: transformer}
        self.options.update(setting)
        value = self.read(option)
        if not value and 'value' in kwargs:
            value = kwargs['value']
            self.config[self.section][option] = str(value)
        return value

    def write(self, option, value=''):
        if not self.config.has_option(self.section, option):
            raise KeyError(f'option "{option}" is not registered!')
        self.config[self.section][option] = str(value)
        thr = threading.Thread(target=self.update_file)
        thr.start()
        thr.join()
    
    def read(self, option):
        if not self.config.has_option(self.section, option):
            return ""
        self.update_instace()
        config_value = self.config[self.section][option]
        final_value = self.options[option](config_value)
        return final_value

    def update_instace(self, stale_only=False):
        config = self.read_file()
        for section in config.sections():
            if stale_only and section == self.section:
                continue
            for opt in config.options(section):
                self.config[section][opt] = config[section][opt]

    def update_file(self):
        self.update_instace(stale_only=True)
        with open(self.__filepath, mode="w", encoding="utf-8") as config_file:
            self.config.write(config_file)

    # def _update(self):
    #     '''
    #     Read the config file again and update the parts of self.config that are not related to the current instance with the values from the file.
    #     Then, rewrite the file with the data from self.config.
    #     Why?
    #     Because an instance of this class is responsible for only one section of the whole config, and instances don't talk to each other,
    #     so data from other sections becomes stale.
    #     ConfigParser does not allow to override only a single section, so updating the file without updating the instance first
    #     overrides changes made by other instances.
    #     '''
    #     current_config = configparser.ConfigParser()
    #     current_config.read(self.__filepath)
        
    #     for section in current_config.sections():
    #         if section == self.section:
    #             continue
    #         for opt in current_config.options(section):
    #             self.config[section][opt] = current_config[section][opt]

    #     with open(self.__filepath, mode="w", encoding="utf-8") as configfile:
    #         self.config.write(configfile)
        


class Trigger:
    ''' A base class for a trigger '''

    def __init__(self, hotkey: str, callback: Callable | None = None, name: str = 'Trigger'):
        self.name = name
        self.config = Config(self.name)
        self.hotkey = self.config.add_option('hotkey')
        if callback:
            self.callback = callback
        self.map_trigger(hotkey)


    def __setattr__(self, name: str, value: Any, /) -> None:
        config = self.__dict__.get('config')
        if (
            config is not None
            and isinstance(name, str)
            and name in config.options
        ):
            config.write(name, value)
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
