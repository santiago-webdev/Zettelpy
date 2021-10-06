import subprocess
import os
from pathlib import Path  # Manage paths
from .func_module import last_opened_note  # To write to lastOpenedNote


class SlipBox:  # Create or check the directories
    def __init__(self, directory):
        self.directory = directory

    def initialize_box(self):
        try:  # Check and create base directories
            NOTES_PATH = Path(self.directory + '/Notes/Fleeting')
            if not NOTES_PATH.is_dir():
                NOTES_PATH.mkdir(parents=True, exist_ok=True)
            os.chdir(self.directory)  # Change to the directory of the notes
        except Exception as d:
            print(d)
            exit(1)


class Zettel:  # Create a defined type of note based on the type of argument given
    def __init__(self, dest, view=False):
        self.dest = dest
        self.view = view

    def create_zettel(self, NOTES_VIEW, NOTES_EDITOR):
        zettel_dest = Path(self.dest)  # I use this variable as a mind helper, to know what I'm working with

        if self.view:
            if zettel_dest.is_file():
                subprocess.Popen([NOTES_VIEW, zettel_dest])
                exit(0)
            else:
                print('The note that you are trying to view doesn\'t exists')
                exit(1)

        try:
            if not zettel_dest.exists():
                os.makedirs(zettel_dest.parent, exist_ok=True)
        except Exception as f:
            print(f)
            exit(1)
        finally:
            if not zettel_dest.exists():
                with open(zettel_dest, 'w') as destNote:
                    title_note = ('# ' +
                            os.path.splitext(os.path.basename(str(zettel_dest)))[0]+'' +
                            '\n## @\n\n\n')  # Generate the template
                    destNote.write(title_note)  # And insert it
            subprocess.run([NOTES_EDITOR, zettel_dest])  # Open the note
            last_opened_note(zettel_dest)
