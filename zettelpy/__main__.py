import argparse
import os
from pathlib import Path
from posixpath import realpath
from sys import stdout
from typing import Final
from zettelpy import slip_box, helper_module


def cli() -> argparse.Namespace:
    """Parses the user arguments"""
    parser = argparse.ArgumentParser(
        prog='zettelpy',
        description='Personal Knowledge System based on Zettelkasten',
    )
    parser.add_argument(
        'title',
        nargs='?',
        type=Path,
        default=None,
        help='Provide path or id of the note',
    )
    parser.add_argument(
        '-l',
        '--last',
        action='store_true',
        help='Open the last permanent note that you have accessed',
    )
    parser.add_argument(
        '-p', '--path', action='store_true', help='Shows real path of the note'
    )
    # parser.add_argument('-d', '--delete', action='store_true', help='Delete note')
    return parser.parse_args()


def main():
    NOTES_DIR: Final = Path(
        os.getenv('ZETTELPY_DIR')
    )  # Directory used to store the notes
    user_args = cli()

    slip_box_spawn = slip_box.SlipBox(NOTES_DIR)  # Instantiate a SlipBox Object
    slip_box_spawn.slipbox_init()  # Create base hierarchy of files

    db_spawn = slip_box.DatabaseManage(NOTES_DIR)  # Instantiate a DatabaseManage Object
    db_spawn.database_init()  # Create the database

    user_args.title = Path(helper_module.first_actions(user_args.last, user_args.title))

    # If the flag -p and title are present return a path through standard output
    if user_args.path is True and user_args.title is not None:
        if not user_args.title.is_file():  # But only if that file exists
            return print('The file doesn\'t exists')
        return stdout.write(str(realpath(user_args.title)))

    if user_args.title is None:
        helper_module.open_note(
            slip_box.Zettel(NOTES_DIR).modf_temp_note()
        )  # This modf_temp_note returns a path, and we open it with open_note
    else:
        helper_module.open_note(
            slip_box.Zettel(NOTES_DIR).modf_zettel(user_args.title)
        )  # The same but for permanent notes

        # TODO, apart from deleting the file, also delete the entry on the database
        # and this should work with the -d flag, which is not implemented right now.
        if os.stat(user_args.title).st_size == 0:
            os.remove(user_args.title)
        else:
            print(realpath(user_args.title))


if __name__ == '__main__':
    main()
