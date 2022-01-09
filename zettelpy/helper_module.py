from datetime import datetime
from pathlib import Path
from sys import stdin


def get_date_as_path() -> Path:
    """Get the entire date, and return it as a path"""
    return Path('fleeting', datetime.today().strftime('%Y%m%d') + '.md')


def receive_from_stdin() -> str:
    if stdin.isatty():
        return ''
    else:
        data = stdin.read()
        print(data.strip())
        return data


def temp_note_template(title_insertion: int) -> str:
    """This function generates a template that will be inserted inside a fleeting note depending on the mode"""

    match title_insertion:
        case 0:
            # New header for a temp note
            return str('# Notes for today ' + datetime.today().strftime('%Y-%m-%d') + '\n\n')
        case 1:
            # New insertion for a temp note
            return str('\n## ' + datetime.today().strftime('%H:%M:%S') + '\n')
        case _:
            raise TypeError('Option not valid')
