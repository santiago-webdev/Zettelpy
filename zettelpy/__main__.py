import argparse, sys, os, subprocess
from pathlib import Path

class NoteError(Exception):
    pass

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

def what_is_this(dest: Path):
    if str(dest) == 'lastOpenedNote':
        print('Open the lastOpenedNote')
        with open('utils/lastOpenedNote', 'r') as readLastNote:
            temp = readLastNote.read().rstrip('\n')
            readLastNote.close()
            return temp
    else:
        return dest
    # destChar = str(dest)[:1]
    # print(destChar)
    # if (destChar == '@'):
    #     print('This is a tag')
    #     # and now it should search for a Luhmann-ID inside a note, to open it
    # else:
    #     print('This is not a tag')


def zettel_edit(dest: Path, view=False):
    if view:
        # If -v flag present do:
        subprocess.Popen(['okular', dest])
        exit(0)
    try: # Open or create the note and path
        if not os.path.exists(dest):
            os.makedirs(os.path.split(dest)[0], exist_ok=True)
    except NoteError as f:
        print('Error: Could not open the note', f, file=stderr)
        exit(1)
    finally:
        with open('utils/lastOpenedNote', 'w') as writeLastNote:
            writeLastNote.write(str(dest))
            writeLastNote.close()
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

    slip_box(notes_directory) # Checks environment

    zettel_edit(what_is_this(args.destination), args.view)

if __name__ == '__main__':
    main()
