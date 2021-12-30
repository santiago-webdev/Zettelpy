import argparse
from os import getenv
from slip_box import SlipBox


def cli() -> argparse.Namespace:  # Parse the arguments
    parser = argparse.ArgumentParser(prog='zettelpy', description='Personal Knowledge System based on Zettelkasten')
    parser.add_argument('destination', nargs='?', type=str, default='', help='Provide path or id of the note')
    return parser.parse_args()


def main():
    NOTES_DIRECTORY: str = getenv('ZETTELPY_DIR')  # Directory used to the notes
    arguments = cli()  # Flags(arguments) given by the user

    checks_slip_box = SlipBox(NOTES_DIRECTORY)  # Creates object in the defined directory
    checks_slip_box.initialize_box()  # Checking if all the directories inside it exists

    # index_notes(NOTES_DIRECTORY, NOTES_EDITOR, args.index)

    # actual_path_note = retrieve_path(args.destination)

    # edit_zettel = Zettel(actual_path_note, args.view)
    # edit_zettel.create_zettel(NOTES_VIEW, NOTES_EDITOR)  # Edit/create the note


if __name__ == '__main__':
    main()
