"""
Autocomplete commands in console.
Need to install pkg prompt_toolkit
First time need to enter command from terminal:
pip install prompt_toolkit
"""

from datetime import datetime
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.validation import Validator
from abc import ABC, abstractmethod

import pyCliAddressBook.sorting as sorting

kb = KeyBindings()


@kb.add("c-space")
def _(event):

    # Start auto completion. If the menu is showing already, select the next completion
    b = event.app.current_buffer

    if b.complete_state:
        b.complete_next()
    else:
        b.start_completion(select_first=False)


def autocomplete():
    """
    Autocompleting commands by inputted first letters
    :return: str
        inputted command
    """
    text: str = prompt("Type cmd: ", completer=cmd, validator=validator,
                       complete_while_typing=True, key_bindings=kb)
    return text


class Command(ABC):
    @abstractmethod
    def execute(self) -> bool:
        pass


class Command_add(Command):

    def __init__(self, subject):
        self.subject = subject

    def execute(self) -> bool:

        self.subject.add_record()
        return True


class Command_view_all(Command):

    def __init__(self, subject):
        self.subject = subject

    def execute(self) -> bool:

        if self.subject.data:
            self.subject.print_in_table(self.subject.data.values(), "#")
        else:
            print("No match records in database")

        return True


class Command_search(Command):

    def __init__(self, subject):
        self.subject = subject

    def execute(self) -> bool:

        records = self.subject.get_records_dy_key()

        if records:
            self.subject.print_in_table(records, "#")
        else:
            print("No match records in database")

        return True


class Command_find(Command):

    def __init__(self, subject):
        self.subject = subject

    def execute(self) -> bool:

        records = self.subject.find_records()

        if records:
            self.subject.print_in_table(records, "#")
        else:
            print("No match records in database")

        return True


class Command_sort_birthday(Command):

    def __init__(self, subject):
        self.subject = subject

    def execute(self) -> bool:

        gap_days = int(input("Enter timedelta for birthday: "))
        current_date = datetime.now()
        result = {}

        for name in self.subject.data:
            bday = self.subject.data[name]["birthday"]
            try:
                mappedbday = bday.replace(year=current_date.year)
            except ValueError:
                # 29 February cannot be mapped to non-leap year. Choose 28-Feb instead
                mappedbday = bday.replace(year=current_date.year, day=28)

            if 0 <= (mappedbday - current_date).days < gap_days:
                try:
                    result[mappedbday.strftime('%A')].append(name)
                except KeyError:
                    result[mappedbday.strftime('%A')] = [name]
            elif current_date.weekday() == 0:
                if -2 <= (mappedbday - current_date).days < 0:
                    try:
                        result[current_date.strftime('%A')].append(name)
                    except KeyError:
                        result[current_date.strftime('%A')] = [name]

        for day, names in result.items():
            print(f"Start reminder on {day}: {', '.join(names)}")

        return True


class Command_update(Command):

    def __init__(self, subject):
        self.subject = subject

    def execute(self) -> bool:

        records = self.subject.get_records_dy_key()

        if records:
            for record in records:
                self.subject.update_record(record)
        else:
            print("Records not found")

        return True


class Command_delete(Command):

    def __init__(self, subject):
        self.subject = subject

    def execute(self) -> bool:

        records = self.subject.get_records_dy_key()

        if records:
            for record in records:
                self.subject.delete_record(record)
        else:
            print("Records not found")

        return True


class Command_reset(Command):

    def __init__(self, subject):
        self.subject = subject

    def execute(self) -> bool:

        self.subject.data = {}

        return True


class Command_file_sort(Command):

    def execute(self) -> bool:
        sorting.perform()
        return True


class Command_exit(Command):

    def execute(self) -> bool:
        print("Good bye!")
        return False


class Command_help(Command):

    def execute(self) -> bool:

        for command in command_list:
            print(f"{command['command_name']}: {command['help']}")

        return True


command_list = [{'command_name': 'add',
                 'command_cls': Command_add, 'subject': 'addressBook',
                 'help': 'Adding record to the address book with fields: name, address, phone, email, birthday'},
                {'command_name': 'add_notes',
                 'command_cls': Command_add, 'subject': 'noteBook',
                 'help': 'Adding record to diary with fields note & keywords.\nKeywords are written down together with note, each keyword is enclosed on both sides by symbol  # '},
                {'command_name': 'view_all',
                 'command_cls': Command_view_all, 'subject': 'addressBook',
                 'help': 'Printing all address book as a formatted table'},
                {'command_name': 'view_all_notes',
                 'command_cls': Command_view_all, 'subject': 'noteBook',
                 'help': 'Printing all notes as a formatted table'},
                {'command_name': 'search',
                 'command_cls': Command_search, 'subject': 'addressBook',
                 'help': 'Searching record in address book by name and printing found record as a formatted table'},
                {'command_name': 'search_notes',
                 'command_cls': Command_search, 'subject': 'noteBook',
                 'help': 'Searching note keyword and printing found notes as a formatted table'},
                {'command_name': 'find',
                 'command_cls': Command_find, 'subject': 'addressBook',
                 'help': 'Searching contact in address book by any field and printing found contacts as a formatted table'},
                {'command_name': 'find_notes',
                 'command_cls': Command_find, 'subject': 'noteBook',
                 'help': 'Searching notes in note book by any words'},
                {'command_name': 'sort_birthday',
                 'command_cls': Command_sort_birthday, 'subject': 'addressBook',
                 'help': 'Printing contacts which have birthday in defined period'},
                {'command_name': 'update',
                 'command_cls': Command_update, 'subject': 'addressBook',
                 'help': 'Updating record in address book. You can change one field or all ones immediately'},
                {'command_name': 'update_notes',
                 'command_cls': Command_update, 'subject': 'noteBook',
                 'help': 'Amending notes and keywords by searching keyword'},
                {'command_name': 'delete',
                 'command_cls': Command_delete, 'subject': 'addressBook',
                 'help': 'Deleting record in address book by name'},
                {'command_name': 'delete_notes',
                 'command_cls': Command_delete, 'subject': 'noteBook',
                 'help': 'Deleting notes by keyword'},
                {'command_name': 'reset',
                 'command_cls': Command_reset, 'subject': 'addressBook',
                 'help': 'Deleting all records in address book'},
                {'command_name': 'reset_notes',
                 'command_cls': Command_reset, 'subject': 'noteBook',
                 'help': 'Deleting all notes in diary'},
                {'command_name': 'file_sort',
                 'command_cls': Command_file_sort,
                 'help': 'Sorting files to categorical folders. Normalising names of files & folders.\nRemoting empty folders. Unpacking archives.'},
                {'command_name': 'exit',
                 'command_cls': Command_exit,
                 'help': 'Exit'},
                {'command_name': 'help',
                 'command_cls': Command_help,
                 'help': "I'm a personal assistant. I'm able to keep an address book & a diary, to sort files.\nYou can use next functions"}]

command_name_list = [command['command_name'] for command in command_list]

cmd = WordCompleter(
    command_name_list,
    ignore_case=True,
)


def is_in_command_name_list(text):
    return text.lower() in command_name_list


validator = Validator.from_callable(
    is_in_command_name_list,
    error_message='Invalid choice.',
    move_cursor_to_end=True)


class Invoker():
    def __init__(self, app) -> None:
        self.commands = {}
        for command in command_list:
            if command.get('subject'):
                self.commands[command['command_name']] = command['command_cls'](
                    app.components.get(command['subject']))
            else:
                self.commands[command['command_name']
                              ] = command['command_cls']()

    def choose_command(self) -> Command:
        choice = autocomplete().lower()
        return self.commands.get(choice)


if __name__ == "__main__":
    autocomplete()
