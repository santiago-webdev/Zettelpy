import datetime
import subprocess
from pathlib import Path
from typing import Optional


def index_notes(NOTES_DIRECTORY, NOTES_EDITOR, index=False):
    index_path = (NOTES_DIRECTORY + '/Notes/index.md')
    if index is True:  # Redoes the index and clean empty files
        subprocess.call(['find', '.', '-empty', '-type', 'f', '-delete'])  # Deletes the empty files
        with open(index_path, 'w') as f:
            subprocess.call(['find', '.', '-name', '*.md'], stdout=f)  # Creates an index of notes
            subprocess.call(['ctags', '-R', '.'])
        subprocess.run([NOTES_EDITOR, index_path])  # View index with editor selected in your config
        exit(0)


def last_opened_note(mode: Optional[Path]):
    if mode == None:
        with open('lastOpenedNote', 'r') as l:  # Read mode
            return l.read().rstrip('\n')
    else:
        if mode.is_file():  # Check if note exists, and then writes
            with open('lastOpenedNote', 'w') as l:  # Write mode
                l.write(str(mode))
        else:
            raise Exception('Can\'t write to file')


def check_extension(to_check: Path):
    if to_check.stem == to_check.name:
        return to_check.with_suffix('.md')
    else:
        return to_check


def retrieve_path(dest: Path):
    dest_path = str(dest)  # I'm casting a Path to a string

    if dest_path == 'lastOpenedNote':  # lastOpenedNote
        return last_opened_note(None)

    elif dest_path.startswith('@'):  # Luhmann-ID
        try:
            return str(subprocess.check_output(['rg', '-w', '-l', '## ' + str(dest)]))[2:-3]
        except Exception as t:
            print(t)
            exit(1)

    elif dest_path == 'Fleeting':  # Fleeting notes
        todays_note = Path('Notes/Fleeting/note-' +
            datetime.date.today().strftime("%Y-%m-%d") + '.md')
        todays_title = ('# Notes for ' +
            datetime.date.today().strftime("%b %d, %Y") + '\n')
        hours_title = ('\n# At ' +
            str(datetime.datetime.now().strftime("%H:%M")))

        if not todays_note.is_file():  # If the note doesn't exists, create it
            with open(todays_note, 'w+') as f:
                f.write(todays_title + "\n\n")

        with open(todays_note, 'a') as f:  # Insert hour each time you enter the note
            f.write(hours_title + "\n\n")
        return todays_note

    else:
        # Check if the dest has a file extension
        dest_fix = Path('Notes', check_extension(dest))
        return dest_fix
