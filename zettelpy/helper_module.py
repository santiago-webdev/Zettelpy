import shutil
import subprocess
from datetime import datetime, date
from os import getenv
from pathlib import Path
from sys import stdin
from typing import Optional


def get_date_as_path(WD_TEMP_NOTE: Path) -> Path:
    """Get the entire date, and return it as a path"""
    return Path(WD_TEMP_NOTE, date.today().strftime("%Y%m%d") + ".md")


def receive_from_stdin(NOTE_PATH: Path) -> True:
    if stdin.isatty():
        return False
    else:
        try:
            data = stdin.read()  # Read information comming from standard input
            with open(NOTE_PATH, 'a') as note_stdin:
                note_stdin.write(data.strip())  # And write it without withspaces
        # TODO, change the exception like so
        # `raise SystemExit("Something has gone terribly wrong")`
        # or use `sys.exit()`
        except Exception as OSError:
            print(OSError)
            exit(1)
        else:
            return True


def open_note(PATH_TO_NOTE: Path):
    return subprocess.run([getenv('EDITOR'), PATH_TO_NOTE])


def check_extension(TO_CHECK: Path):
    if TO_CHECK.stem == TO_CHECK.name:
        return TO_CHECK.with_suffix('.md')
    else:
        return TO_CHECK


def first_actions(flag_is_last: bool, flag_perm: Optional[Path] = None) -> str or None:
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

    if flag_is_last is True:
        with open('last_note', 'r') as last_note:  # Read mode
            return last_note.read().rstrip('\n')
    elif flag_is_last is False and flag_perm is not None:
        with open('last_note', 'w') as last_accessed:  # Write mode
            flag_perm = check_extension(flag_perm)  # Make flag_perm a .md file
            main_arg_check = Path('permanent', flag_perm)  # Correct the path
            last_accessed.write(str(main_arg_check))  # And write the Path to the file
            return main_arg_check
    elif flag_is_last is False and flag_perm is None:
        return None
    else:
        raise TypeError('Something is wrong with the parameters given to this function')


def template_do(request: str, NOTE_PATH: Path):
    if request == 'title fleeting':
        NEW_TITLE = '# Notes for today ' + str(
            date.today().strftime('%d of %B, %Y') + '\n'
        )
        with open(NOTE_PATH, 'w') as title_note:
            title_note.write(NEW_TITLE)
        template_do('new insertion', NOTE_PATH)
    elif request == 'new insertion':
        NEW_INSERTION = '\n## At ' + str(
            datetime.today().strftime('%H:%M:%S') + '\n' + '\n'
        )
        with open(NOTE_PATH, 'a') as fleeting_note:  # Write mode
            return fleeting_note.write(NEW_INSERTION)
    elif request == 'title zettel':
        # TODO replace text in the file after doing the copy of the file
        NEW_ZETTEL = Path(__file__).parent / 'templates' / 'title_header.md'
        shutil.copyfile(NEW_ZETTEL, NOTE_PATH)
        return NOTE_PATH
    else:
        raise TypeError('The given parameter doesn\'t correspond to any template')
