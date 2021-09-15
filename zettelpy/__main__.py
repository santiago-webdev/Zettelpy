import argparse, sys, os, subprocess, re
from os.path import exists
from pathlib import Path

class NoteError(Exception):
    pass # For managing exceptions

def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog='zettelpy',
        description='Personal Knowledge System based on Zettelkasten')
    parser.add_argument('destination',
        type=Path,
        help='Provide path/Title or Luhmann-ID to go to note')
    parser.add_argument('-v', '--view',
        action='store_true',
        help='Open a note by title, ID, or by lastNoteUsed')
    return parser.parse_args()

def slip_box(directory):
    try:
        if not os.path.isdir(directory):
            os.mkdir(directory)
            os.mkdir(directory + '/' + 'utils')
            with open(directory + '/' + 'utils/lastOpenedNote', 'w') as lastOpenedNote:
                pass
        os.chdir(directory)
    except NoteError as d:
        print('Error: Could not create directory', d, file=stderr)
        exit(1)

def define_path(dest: Path):
    if str(dest) == 'lastOpenedNote':
        with open('utils/lastOpenedNote', 'r') as readLastNote:
            temp = readLastNote.read().rstrip('\n')
            return temp
    else:
        if (str(dest)[:1] == '@'):
            auxVar = subprocess.check_output(['rg', '-w', '-l', dest])
            auxiliar = str(auxVar)
            return auxiliar[2:-3]
        else:
            return dest

def zettel_edit(dest: Path, view=False):
    # If the -v is present open the file and ignore everything else
    if view:
        subprocess.Popen(['okular', dest])
        exit(0)
    # Try open or create the path to the note before creating the note itself.
    try:
        if not os.path.exists(dest):
            os.makedirs(os.path.split(dest)[0], exist_ok=True)
    except NoteError as f:
        print('Error: Could not open the note', f, file=stderr)
        exit(1)
    finally:
        with open('utils/lastOpenedNote', 'w') as lastNote:
            lastNote.write(str(dest)) # Rewrites to the lastNote
        # If the note doesn't exists create it and put template on it
        if not exists(dest):
            with open(dest, 'w') as destNote:
                destNote.write('# Title\n## @\n\n\n')
        # And open with the default EDITOR
        subprocess.run([os.environ['EDITOR'], dest])

def main():
    # The arguments come from argparse
    args = cli()
    # Define default place
    notes_directory = (os.environ['HOME'] + '/.zettelpy')
    # Checks environment
    slip_box(notes_directory)
    # Edit the dest and note
    zettel_edit(define_path(args.destination), args.view)

if __name__ == '__main__':
    main()
