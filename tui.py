''' Terminal User Interface for remapping triggers '''

from os import system

from prettytable import PrettyTable

from triggers import Trigger
import messages


type Table = list[list]


def generate_trigger_table(triggers: list[Trigger]) -> Table:
    ''' Put the data into a 2d list '''
    table = []
    for id, trigger in enumerate(triggers):
        table.append([id, trigger.name, trigger.hotkey])
    
    return table


def create_trigger_table(table: Table) -> PrettyTable:
    ''' Make a drawable table from the 2d list '''
    pt = PrettyTable(title="Trigger map")
    pt.field_names = ['Id', 'Function', 'Trigger key']
    for row in table:
        pt.add_row(row)
    
    return pt


def print_info(triggers: list[Trigger]):
    print(messages.start_message)
    trigger_table: Table = generate_trigger_table(triggers)
    pretty_table: PrettyTable = create_trigger_table(trigger_table)
    print(pretty_table)
    print(messages.remapping_instruction)


def validate_id(id: str, triggers: list[Trigger]) -> int | None:
    if not id.isdigit():
        print('Id has to be a number!')
        return
    index = int(id)
    index_range = len(triggers) - 1
    if index > index_range:
        print(f'ID is out of range!\nA trigger with ID: {index} does not exits.')
        return
    return index


def tui(triggers: list[Trigger]):
    print_info(triggers)
    while True:
        id = input('ID: ')
        index = validate_id(id, triggers)
        if index != None:
            print(f'debug: index={index}')
            triggers[index].remap_trigger()
            system('cls')
            print_info(triggers)