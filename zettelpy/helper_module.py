# Imports
import shutil
import subprocess
from datetime import datetime, date
from os import getenv
from pathlib import Path
from sys import stdin
from typing import Optional


# Create the title of a note as a date
def get_date_as_path(WD_TEMP_NOTE: Path) -> Path:
    """Get the entire date, and return it as a path"""
    return Path(WD_TEMP_NOTE, date.today().strftime("%Y%m%d") + ".md")


# Actual date, long format with suffix on the number
def pretty_date() -> str:
    """Return a nicely formatted string based on the actual date"""
    date_suffix = ['th', 'st', 'nd', 'rd']  # Suffix for the number of days in the month
    day_number = int(date.today().strftime('%d'))  # Get the number of the day

    # Check the number, and apply 'th', 'st', 'nd', or 'rd' respectively
    if day_number % 10 in [1, 2, 3] and day_number not in [11, 12, 13]:
        fixed_day = str(day_number) + date_suffix[day_number % 10]
    else:
        fixed_day = str(day_number) + date_suffix[0]

    # Format the note to be more pretty
    return date.today().strftime('%A, %B {}, %Y.').format(fixed_day)


# Receive data from stdin
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


# Open the note with your $EDITOR
def open_note(PATH_TO_NOTE: Path):
    return subprocess.run([getenv('EDITOR'), PATH_TO_NOTE])


# Check the extension of the note
def check_extension(TO_CHECK: Path):
    if TO_CHECK.stem == TO_CHECK.name:
        return TO_CHECK.with_suffix('.md')
    else:
        return TO_CHECK


# First actions taken when starting the program
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


# Template actions
def template_do(request: str, NOTE_PATH: Path):
    """Set of actions used to manage the contents of the notes"""

    # Used in temporary/fleeting notes
    if request == 'title fleeting':
        NEW_TITLE: str = '# Notes for today -> ' + pretty_date() + '\n'
        with open(NOTE_PATH, 'w') as title_note:
            title_note.write(NEW_TITLE)
        template_do('new insertion', NOTE_PATH)
    elif request == 'new insertion':
        NEW_INSERTION = '\n### At ' + str(
            datetime.today().strftime('%H:%M:%S') + '\n' + '\n'
        )
        with open(NOTE_PATH, 'a') as fleeting_note:  # Write mode
            return fleeting_note.write(NEW_INSERTION)

    # Used in zettel/permanent notes
    elif request == 'title zettel':
        NEW_ZETTEL = Path(__file__).parent / 'templates' / 'title_header.md'
        shutil.copyfile(NEW_ZETTEL, NOTE_PATH)

        title_of_note = NOTE_PATH.stem + ' -'
        subprocess.run(['sed', '-i', '1s/TODO/{}/g'.format(title_of_note), NOTE_PATH])
        subprocess.run(['sed', '-i', '3s/TODO/{}/g'.format(pretty_date()), NOTE_PATH])
        return NOTE_PATH
    else:
        raise TypeError('The given parameter doesn\'t correspond to any template')
