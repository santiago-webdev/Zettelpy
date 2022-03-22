import argparse
import os
from pathlib import Path
from posixpath import realpath
from sys import stdout
from zettelpy import slip_box, utils_module as utils  # Import helper functions


# CLI Arguments
def cli_arguments() -> argparse.Namespace:
    """Parses the user arguments"""
    parser = argparse.ArgumentParser(
        prog="zettelpy",
        description="Personal Knowledge System based on Zettelkasten",
    )
    parser.add_argument(
        "title",
        nargs="?",
        type=Path,
        default=None,
        help="Provide an ID or title to search or create a note",
    )
    parser.add_argument(
        "-l",
        "--last",
        action="store_true",
        help="""Open the last permanent note that you have
        accessed, if you provide a title it will be ignored""",
    )
    parser.add_argument(
        "-p",
        "--path",
        action="store_true",
        help="Prints the path to the note, it can be used for command replacement",
    )
    parser.add_argument(
        "-d", "--delete", action="store_true", help="Delete the note by title/ID"
    )

    return parser.parse_args()


def main():
    # If the env var ZETTELPY_DIR is not set assign a default value to NOTES_DIR
    if not (NOTES_DIR := os.getenv("ZETTELPY_DIR")):
        NOTES_DIR: Path = Path(os.getenv("HOME"), ".zettelpy")
        return NOTES_DIR

    # Instantiate both Objects and create the directories and database necessaries
    slip_box_spawn = slip_box.SlipBox(NOTES_DIR)
    db_spawn = slip_box.DatabaseManage(NOTES_DIR)
    slip_box_spawn.slipbox_init()
    db_spawn.database_init()

    zettel_mode = utils.first_actions(cli_arguments().last, cli_arguments().title)

    # Check -d flag
    if cli_arguments().delete is True and cli_arguments().title is None:
        print("You haven't specified the note you want to delete")
        return exit(1)
    elif cli_arguments().delete is True and cli_arguments().title is not None:
        return db_spawn.delete_row_and_file(zettel_mode)

    # For title and -p flags return a path through stdout without editing the note
    if cli_arguments().path is True and cli_arguments().last is True:
        with open("last_note", "r") as last_note:
            return realpath(last_note.read().rstrip("\n"))
    elif cli_arguments().path is True and zettel_mode is not None:
        if not zettel_mode.is_file():  # But only if that file exists
            return print("The file doesn't exists")
        return stdout.write(str(realpath(zettel_mode)))

    if zettel_mode is None:
        # This modf_temp_note returns a path, and we open it with open_note
        utils.open_note(slip_box.Zettel(NOTES_DIR).modf_temp_note())
    else:
        # Query the database for a path first, return_path actually returns a tuple when
        # there's a value present or a NoneType, so if the walrus operator works we
        # assign the first and only element of this tuple to zettel_mode
        if db_can_return_path := db_spawn.return_path(Path(zettel_mode).stem):
            zettel_mode = db_can_return_path[0]

        # The same but for permanent notes
        utils.open_note(slip_box.Zettel(NOTES_DIR).modf_zettel(Path(zettel_mode)))

        if os.stat(zettel_mode).st_size == 0:  # Check the size of the file
            # If it's empty delete the file
            db_spawn.delete_row_and_file(zettel_mode)
        else:
            # If the file is not empty, try to insert it into the database, which will
            # be ignored if it's detected that there's a note with the same title
            db_spawn.insert_note(Path(zettel_mode).stem, realpath(zettel_mode))


if __name__ == "__main__":
    main()
