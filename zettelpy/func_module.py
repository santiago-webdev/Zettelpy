import datetime
import subprocess
from pathlib import Path


def index_notes(NOTES_DIRECTORY, NOTES_EDITOR, index=False):
    index_path = (NOTES_DIRECTORY + '/Notes/index.md')
    if index is True:  # Redoes the index and clean empty files
        subprocess.call(['find', '.', '-empty', '-type', 'f', '-delete'])  # Deletes the empty files
        with open(index_path, 'w') as f:
            subprocess.call(['find', '.', '-name', '*.md'], stdout=f)  # Creates an index of notes
            subprocess.call(['ctags', '-R', '.'])
        subprocess.run([NOTES_EDITOR, index_path])  # View index with editor selected in your config
        exit(0)


def retrieve_path(dest: Path):
    if str(dest) == 'lastOpenedNote':  # lastOpenedNote
        with open('lastOpenedNote', 'r') as lastOpenedNote:
            return lastOpenedNote.read().rstrip('\n')

    # TODO
    # Fix using ripgrep instead of python, should use os.walk() I guess
    # fix non existing IDs parsed, how should the program react to that?
    # fix creating note if ID doesn't exists
    elif str(dest).startswith('@'):  # Luhmann-ID
        try:
            return str(subprocess.check_output(['rg', '-w', '-l', '## ' + str(dest)]))[2:-3]
        except Exception as t: print(t)

    elif str(dest) == 'Fleeting':  # Fleeting notes
        todays_note = Path('Notes/Fleeting/note-' +
                datetime.date.today().strftime("%Y-%m-%d") + '.md')
        todays_title = ('# Notes for ' +
                datetime.date.today().strftime("%b %d, %Y") + '\n')
        hours_title = ('\n# At ' +
                str(datetime.datetime.now().strftime("%H:%M")))
        if not todays_note.is_file():  # If the note doesn't exists, create it
            with open(todays_note, 'w+') as fleetingNote:
                fleetingNote.write(todays_title + "\n\n")

        with open(todays_note, 'a') as fleetingNote:  # Insert hour each time you enter the note
            fleetingNote.write(hours_title + "\n\n")
        return todays_note

    else:
        return dest
