import subprocess
import os


# Create or check the directories
class SlipBox:
    def __init__(self, directory):
        self.directory = directory

    def initializeBox(self):
        try:
            # Check if the zettelpy directory exists
            if not os.path.exists(self.directory):
                os.mkdir(self.directory)

            # Check if the Fleeting directory exists
            if not os.path.exists(self.directory + '/' + 'Fleeting'):
                os.mkdir(self.directory + '/' + 'Fleeting')

            # Check if the .utils directory exists
            if not os.path.exists(self.directory + '/' + '.utils'):
                os.mkdir(self.directory + '/' + '.utils')

            # Check if the shell script exists
            if not os.path.exists(self.directory + '/' + '.utils/zettelpy-redo-notes'):
                print('You didn\'t executed the install.sh did you?')
                exit(1)

            # Change to the directory of the notes
            os.chdir(self.directory)
        except Exception as d: print (d) & exit(1)


# Create a defined type of note based on the type of argument given
class Zettel:
    def __init__(self, dest, view=False):
        self.dest = dest
        self.view = view

    def createZettel(self):
        # If the -v is present open the file and ignore everything else
        if self.view:
            subprocess.Popen(['okular', self.dest])
            exit(0)
        try:
            if not os.path.exists(self.dest):
                os.makedirs(os.path.split(self.dest)[0], exist_ok=True)
        except Exception as f: print(f) & exit(1)
        finally:
            with open('.utils/lastOpenedNote', 'w+') as lastOpenedNote:
                lastOpenedNote.write(str(self.dest))  # Rewrites to the lastNote
            # If the note doesn't exists create it and put template on it
            if not os.path.exists(self.dest):
                with open(self.dest, 'w') as destNote:
                    titleNote = ('# ' + os.path.basename(str(self.dest)) + '\n## @\n\n\n')
                    destNote.write(titleNote)
            # And open with the default EDITOR
            subprocess.run([os.environ['EDITOR'], self.dest])
