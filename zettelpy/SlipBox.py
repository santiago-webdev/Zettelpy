import subprocess
import os


class SlipBox:  # Create or check the directories
    def __init__(self, directory):
        self.directory = directory

    def initialize_box(self):
        try:  # Check if each directories and files exists
            if not os.path.exists(self.directory):
                os.mkdir(self.directory)

            if not os.path.exists(self.directory + '/' + 'Fleeting'):
                os.mkdir(self.directory + '/' + 'Fleeting')

            if not os.path.exists(self.directory + '/' + '.utils'):
                os.mkdir(self.directory + '/' + '.utils')
                print('There\'s some missing files, check the README')

            os.chdir(self.directory)  # Change to the directory of the notes
        except Exception as d: print (d) & exit(1)


class Zettel:  # Create a defined type of note based on the type of argument given
    def __init__(self, dest, view=False):
        self.dest = dest
        self.view = view

    def create_zettel(self, NOTES_VIEW, NOTES_EDITOR):
        if self.view:  # If -v you view the note that you parsed
            subprocess.Popen([NOTES_VIEW, self.dest])
            exit(0)
        try:
            if not os.path.exists(self.dest):  # Create note if it doesn't exists
                os.makedirs(os.path.split(self.dest)[0], exist_ok=True)
        except Exception as f: print(f) & exit(1)
        finally:
            with open('.utils/lastOpenedNote', 'w+') as lastOpenedNote:
                lastOpenedNote.write(str(self.dest))  # Rewrites to lastOpenedNote
            if not os.path.exists(self.dest):
                with open(self.dest, 'w') as destNote:
                    title_note = ('# ' +
                            os.path.splitext(os.path.basename(str(self.dest)))[0]+'' +
                            '\n## @\n\n\n')  # Generate the template
                    destNote.write(title_note)  # And insert it
            subprocess.run([NOTES_EDITOR, self.dest])  # Open the note
