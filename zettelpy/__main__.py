import os
import sys
from .SlipBox import SlipBox, Zettel  # Import Zettel(notes) and Slip Box objects
from .func_module import cli, index_notes, retrieve_path


def main():
    # The arguments come from argparse, from the imported cli function
    args = cli()

    # Define default place
    notes_directory = (os.environ['HOME'] + '/.local/share/zettelpy')

    # Checking if the directories exists
    checkSlipBox = SlipBox(str(notes_directory))
    checkSlipBox.initializeBox()

    # If you parse -i it will clean empty files, regenarate ctags and index to
    # view it, if you don't it will just skip this part.
    index_notes(notes_directory, args.index)

    # Parse a keyword or title and return the real path of the note that we are
    # looking for
    actual_path_note = retrieve_path(args.destination)

    # Edit/create the note
    editZettel = Zettel(actual_path_note, args.view)
    editZettel.createZettel()


if __name__ == '__main__':
    main()
