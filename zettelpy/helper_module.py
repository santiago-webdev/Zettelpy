import subprocess
import shutil
from datetime import datetime
from os import getenv
from pathlib import Path
from sys import stdin
from typing import Optional


def get_date_as_path(NOTE_PATH: Path) -> Path:
    """Get the entire date, and return it as a path"""
    return Path(NOTE_PATH, datetime.today().strftime("%Y%m%d") + ".md")


def receive_from_stdin() -> str:
    if stdin.isatty():
        return ''  # TODO fix this return
    else:
        data = stdin.read()
        print(data.strip())
        return data
    # # Receive input from standard input
    # if not sys.stdin.isatty():
    #     data = sys.stdin.read()
    #     print(data.strip())


def open_note(PATH_TO_NOTE: Path):
    return subprocess.run([getenv('EDITOR'), PATH_TO_NOTE])


def first_actions(flag_last: bool, main_arg: Optional[str] = None) -> str or None:
    """
    Checks for the -l flag, which stands for last accessed note, do some logic explained
    below, and after this return either a str or None.
    IF True means the -l flag is present, in that case read and return from last_note,
    and ignore everything else.
    ELIF the flag_last is not present(False) and main_arg is present it means the user
    wants to access a permanent note, so we write which note(str from main_arg) is and
    return that string.
    ELIF the flag_last is not present(False) and main_arg being None means the user has
    not specified an ID, so it means it wants to open a fleeting note.
    """

    if flag_last is True:
        with open('last_note', 'r') as last_note:  # Read mode
            return last_note.read().rstrip('\n')
    elif flag_last is False and main_arg is not None:
        with open('last_note', 'w') as last_accessed:  # Write mode
            last_accessed.write(main_arg)
            return main_arg
    elif flag_last is False and main_arg is None:
        return None
    else:
        raise TypeError('Something is wrong with the parameters given to this function')


def template_do(request: str, NOTE_PATH: Path):
    if request == 'title fleeting':
        TITLE_TEMPLATE = Path(__file__).parent / 'templates' / 'title_header.md'
        return shutil.copyfile(TITLE_TEMPLATE, NOTE_PATH)
    elif request == 'new insertion':
        NEW_INSERTION = '\n# At ' + str(datetime.today().strftime('%H:%M:%S') + '\n\n')
        with open(NOTE_PATH, 'a') as fleeting_note:  # Write mode
            return fleeting_note.write(NEW_INSERTION)
    else:
        raise TypeError('The given parameter doesn\'t correspond to any template')
