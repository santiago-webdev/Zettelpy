import argparse
from os import getenv
from .slip_box import SlipBox


def cli() -> argparse.Namespace:  # Parse the arguments
    parser = argparse.ArgumentParser(prog='zettelpy', description='Personal Knowledge System based on Zettelkasten')
    parser.add_argument('destination', nargs='?', type=str, default='', help='Provide path or id of the note')
    return parser.parse_args()


def main():
    NOTES_DIR: str = getenv('ZETTELPY_DIR')  # Directory used to the notes
    user_args = cli()  # Arguments given by the user

    checks_slip_box = SlipBox(NOTES_DIR)  # This Class creates an Object in the defined directory
    checks_slip_box.initialize_box()  # The Object checks if the directory it exists

    # index_notes(NOTES_DIRECTORY, NOTES_EDITOR, user_args.index)

    # actual_path_note = retrieve_path(user_args.destination)

    # edit_zettel = Zettel(actual_path_note, user_args.view)
    # edit_zettel.create_zettel(NOTES_VIEW, NOTES_EDITOR)  # Edit/create the note


if __name__ == '__main__':
    main()
