import argparse
from os import getenv
from pathlib import Path
from zettelpy import slip_box, helper_module


def cli() -> argparse.Namespace:
    """Parses the user arguments"""
    parser = argparse.ArgumentParser(
        prog='zettelpy',
        description='Personal Knowledge System based on Zettelkasten',
    )
    parser.add_argument(
        'main_argument',
        nargs='?',
        type=str,
        default=None,
        help='Provide path or id of the note',
    )
    parser.add_argument(
        '-l',
        '--last',
        action='store_true',
        help='Open the last permanent note that you have accessed',
    )
    # TODO: check for the --path flag, and instead of calling open_note, just call the
    # function to return the path
    # parser.add_argument(
    #     '-p', '--path', action='store_true', help='Shows real path of the note'
    # )
    # parser.add_argument('-d', '--delete', action='store_true', help='Delete note')
    return parser.parse_args()


def main():
    NOTES_DIR: Path = Path(getenv('ZETTELPY_DIR'))  # Directory used to store the notes
    user_args = cli()

    slip_box_spawn = slip_box.SlipBox(NOTES_DIR)  # Instantiate a SlipBox Object
    slip_box_spawn.slipbox_init()  # Create base hierarchy of files

    db_spawn = slip_box.DatabaseManage(NOTES_DIR)  # Instantiate a DatabaseManage Object
    db_spawn.database_init()  # Create the database

    # Check for -l flag and main_argument
    first_actions = helper_module.first_actions(user_args.last, user_args.main_argument)

    if first_actions is None:
        helper_module.open_note(
            slip_box.Zettel(NOTES_DIR).modf_temp_note()
        )  # This modf_temp_note returns a path, and we open it with open_note
    else:
        pass
        # helper_module.open_note(
        #     slip_box.Zettel(NOTES_DIR).modf_zettel()
        # )  # The same but for permanent notes


if __name__ == '__main__':
    main()
