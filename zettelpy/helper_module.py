from datetime import datetime
import os
from pathlib import Path
from sys import stdin
from typing import Optional


def get_date_as_path() -> Path:
    """Get the entire date, and return it as a path"""
    return Path("fleeting", datetime.today().strftime("%Y%m%d") + ".md")


def receive_from_stdin() -> str:
    if stdin.isatty():
        return ''
    else:
        data = stdin.read()
        print(data.strip())
        return data


# def flags_first_actions(flag_last: bool or None, main_arg: Optional[str] = None) -> None or Path:
def flags_first_actions(flag_last: bool, main_arg: Optional[str] = None) -> str or None:
    """
    This function checks for the -l flag, which stands for last accessed note, do
    some logic explained below, and after this return either a str or None.
    IF True means the -l flag is present, in that case read and return from last_note,
    and ignore everything else.
    ELIF the flag_last is not present(False) and main_arg is present it means the user
    wants to access a permanent note, so we write which note(str from main_arg) is and
    return that string.
    ELIF the flag_last is not present(False) and main_arg being None means the user
    has not specified an ID, so it means it wants to open a fleeting note.
    """

    if flag_last is True:
        with open('last_note', 'r') as last_note:  # Read mode
            print(last_note)
            # file_size = os.path.getsize(last_note)
            # print(file_size)
            return last_note.read().rstrip('\n')
    elif flag_last is False and main_arg is not None:
        with open('last_note', 'w') as last_accessed:  # Write mode
            last_accessed.write(main_arg)
            return main_arg
    elif flag_last is False and main_arg is None:
        return None
    else:
        raise TypeError('Something wrong with the parameters given to this function')

    # if flag_last is None:
    #     return main_arg
    # elif flag_last is True:
    #     with open('last_note', 'r') as last_note:  # Read mode
    #         return last_note.read().rstrip('\n')
    # elif flag_last is False:
    #     return main_arg
    # else:
    #     raise TypeError('Something wrong with the parameters given to this function')


# def last_accessed_note(main_arg: bool, save_rel_path: Optional[Path]) -> Path:
#     if main_arg is True:
#         with open('last_accessed', 'r') as last_accessed:  # Read mode
#             return last_accessed.read().rstrip('\n')
#     elif main_arg is False:
#         with open('last_accessed', 'w') as last_accessed:  # Write mode
#             last_accessed.write(save_rel_path)
#     else:
#         raise OSError('main_arg should be a boolean')
