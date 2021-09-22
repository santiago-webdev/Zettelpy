import argparse
import subprocess
import os
import datetime
from pathlib import Path  # Manage paths


# Parse the arguments
def cli() -> argparse.Namespace:

    parser = argparse.ArgumentParser(prog='zettelpy',
        description='Personal Knowledge System based on Zettelkasten')

    parser.add_argument('destination',
        nargs='?', type=Path,
        default='Fleeting',
        help='Provide path/Title or Luhmann-ID to go to note')

    parser.add_argument('-v', '--view',
        action='store_true',
        help='Open a note by title, ID, or by lastNoteUsed')

    parser.add_argument('-i', '--index',
        action='store_true',
        help='Shows the index in your editor of choice')

    return parser.parse_args()


# Redoes the index and clean empty directories and files
def index_notes(notesDirectory, index=False):
    if index is True:
        subprocess.Popen(['.utils/zettelpy-redo-notes', notesDirectory])
        subprocess.run([os.environ['EDITOR'], 'index.md'])
        exit(0)


def retrieve_path(dest: Path):
    # lastOpenedNote
    if str(dest) == 'lastOpenedNote':
        with open('.utils/lastOpenedNote', 'r') as lastOpenedNote:
            return lastOpenedNote.read().rstrip('\n')

    # Luhmann-ID
    elif str(dest).startswith('@'):
        try:
            return str(subprocess.check_output(['rg', '-w', '-l', '## ' + str(dest)]))[2:-3]
        except Exception as t:
            print(t)

    # Fleeting notes
    elif str(dest) == 'Fleeting':
        # Now I need to add the logic for creating a note each day and add the date and hour
        todays_note = ('Fleeting/note-' + datetime.date.today().strftime("%Y-%m-%d") + '.md')
        todays_title = ('# Notes for ' + datetime.date.today().strftime("%b %d, %Y") + '\n')
        hours_title = ('\n# At ' + str(datetime.datetime.now().strftime("%H:%M")))
        # If the note doesn't exists, create it
        if not os.path.exists(todays_note):
            with open(todays_note, 'w+') as fleetingNote:
                fleetingNote.write(todays_title + "\n\n")
        # Each time I enter to the Fleeting note of the day it will insert hour and minutes
        with open(todays_note, 'a') as fleetingNote:
            fleetingNote.write(hours_title + "\n\n")
        return todays_note
    else:
        return dest
