import argparse
import os
from pathlib import Path
from posixpath import realpath
from sys import stdout
from zettelpy import slip_box, helper_module as helper


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
        '-p',
        '--path',
        action='store_true',
        help='Prints the path to the note, it can also be used for command replacement',
    )
    # parser.add_argument(
    #     '-d', '--delete', action='store_true', help='Delete the note by title'
    # )
    return parser.parse_args()


def main():
    # If the env var $ZETTELPY_DIR is not set, assign a default value to NOTES_DIR
    if not (NOTES_DIR := os.getenv('ZETTELPY_DIR')):
        NOTES_DIR = Path(os.getenv('HOME'), 'zettelpy')
    user_args = cli()

    slip_box_spawn = slip_box.SlipBox(NOTES_DIR)  # Instantiate a SlipBox Object
    slip_box_spawn.slipbox_init()  # Create base hierarchy of files

    db_spawn = slip_box.DatabaseManage(NOTES_DIR)  # Instantiate a DatabaseManage Object
    db_spawn.database_init()  # Create the database

    zettel_mode = helper.first_actions(user_args.last, user_args.title)

    # If the argument/flag title(which in this case would be zettel_mode) and -p are
    # present return a path through standard output
    if user_args.path is True and zettel_mode is not None:
        if not zettel_mode.is_file():  # But only if that file exists
            return print('The file doesn\'t exists')
        return stdout.write(str(realpath(zettel_mode)))

    if zettel_mode is None:
        # This modf_temp_note returns a path, and we open it with open_note
        helper.open_note(slip_box.Zettel(NOTES_DIR).modf_temp_note())
    else:
        # The same but for permanent notes
        helper.open_note(slip_box.Zettel(NOTES_DIR).modf_zettel(Path(zettel_mode)))

        # TODO, apart from deleting the file, also delete the entry on the database
        # and this should work with the -d flag, which is not implemented right now.
        if os.stat(zettel_mode).st_size == 0:
            db_spawn.delete_on_empty_file(zettel_mode)
        else:
            db_spawn.insert_note(zettel_mode, realpath(zettel_mode))

        # TODO Query the db for information about the path
        # c.execute("SELECT path FROM notes WHERE title='test'")

        # conn = sqlite3.connect(self.db_path)  # Connect to the database
        # with conn:
        #     conn.cursor().execute(
        #         """INSERT OR IGNORE INTO notes (title, path, date) VALUES ('{}', '{}',
        #         DATETIME('now'))""".format(
        #             TITLE, REAL_PATH
        #         )
        #     )


if __name__ == '__main__':
    main()
