import argparse, sys, os, subprocess
from pathlib import Path

class NoteError(Exception):
    pass

def slip_box(directory):
    try:
        if not os.path.isdir(directory):
            os.mkdir(directory)
            os.mkdir(directory + '/' + 'utils')
        os.chdir(directory)
    except NoteError as d:
        print('Error: Could not create directory', d, file=stderr)
        exit(1)

def zettel_edit(dest: Path, view=False):
    try: # Open or create the note
        # if not dest.is_file():
        #     open(dest, 'w+')
        if not os.path.exists(dest):
            os.mkdir(os.path.split(dest)[0])
            open(dest, 'w+')
    except NoteError as f:
        print('Error: Could not open the note', f, file=stderr)
        exit(1)
    finally:
        subprocess.run([os.environ['EDITOR'], dest])

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

def main():
    args = cli()
    notes_directory = (os.environ['HOME'] + '/.zettelpy')

    slip_box(notes_directory)
    zettel_edit(args.destination, args.view)

if __name__ == '__main__':
    main()
