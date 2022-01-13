import argparse
from os import getenv
from pathlib import Path
from zettelpy import slip_box, helper_module


def cli() -> argparse.Namespace:
    """Parses the user arguments"""
    parser = argparse.ArgumentParser(
        prog='zettelpy', description='Personal Knowledge System based on Zettelkasten'
    )
    parser.add_argument(
        'main_argument',
        nargs='?',
        type=str,
        default=None,
        help='Provide path or id of the note',
    )
    parser.add_argument(
        '-f', '--fleeting', action='store_true', help='Quick/Temp/Fleeting notes'
    )
    parser.add_argument('-l', '--last', action='store_true', help='Last accessed note')
    # parser.add_argument('-p', '--path', action='store_true', help='Shows real path of the note')
    # parser.add_argument('-d', '--delete', action='store_true', help='Delete note')
    return parser.parse_args()


def main():
    NOTES_DIR: Path = Path(getenv('ZETTELPY_DIR'))  # Directory used to store the notes
    user_args = cli()

    slip_box_spawn = slip_box.SlipBox(NOTES_DIR)  # Instantiate a SlipBox Object
    slip_box_spawn.slipbox_init()  # Create base hierarchy of files

    db_spawn = slip_box.DatabaseManage(NOTES_DIR)  # Instantiate a DatabaseManage Object
    db_spawn.database_init()  # Create the database

    # response_first_actions = helper_module.flags_first_actions(
    #     user_args.last, user_args.main_argument
    # )

    # if response_first_actions is None:
    #     FleetingZettelpy(NOTES_DIR)

    # print(user_args.main_argument)

    # note_spawn = slip_box.Zettel
    # note_spawn.modf_temp_note()

    # # Receive input from standard input
    # if not sys.stdin.isatty():
    #     data = sys.stdin.read()
    #     print(data.strip())


if __name__ == '__main__':
    main()
