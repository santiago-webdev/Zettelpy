import argparse
from os import getenv
from pathlib import Path
from posixpath import realpath
from zettelpy import slip_box, helper_module


def cli() -> argparse.Namespace:
    """Parses the user arguments"""
    parser = argparse.ArgumentParser(
        prog='zettelpy',
        description='Personal Knowledge System based on Zettelkasten',
    )
    parser.add_argument(
        'luhmann_id',
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
    NOTES_DIR: Path = Path(getenv('ZETTELPY_DIR'))  # Directory used to store the notes
    args = cli()

    slip_box_spawn = slip_box.SlipBox(NOTES_DIR)  # Instantiate a SlipBox Object
    slip_box_spawn.slipbox_init()  # Create base hierarchy of files

    db_spawn = slip_box.DatabaseManage(NOTES_DIR)  # Instantiate a DatabaseManage Object
    db_spawn.database_init()  # Create the database

    args.luhmann_id = Path(helper_module.first_actions(args.last, args.luhmann_id))

    if args.path is True and args.luhmann_id is not None:
        return realpath(
            args.luhmann_id
        )  # If the -p flag is present and the luhmann_id is present just print the path

    if args.luhmann_id is None:
        helper_module.open_note(
            slip_box.Zettel(NOTES_DIR).modf_temp_note()
        )  # This modf_temp_note returns a path, and we open it with open_note
    else:
        helper_module.open_note(
            slip_box.Zettel(NOTES_DIR).modf_zettel(args.luhmann_id)
        )  # The same but for permanent notes


if __name__ == '__main__':
    main()
