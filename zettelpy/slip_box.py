import os
import subprocess
from pathlib import Path
from zettelpy import helper_module


class SlipBox:
    """Instantiate an object that can create the directory"""

    def __init__(self, directory):
        self.directory = directory

    def slipbox_init(self):
        """In this method if the directory or the database under the given path does not exist then create it"""

        NOTES_PATH: Path = Path(self.directory)
        NOTES_PATH_FLEETING: Path = Path(self.directory, 'fleeting')
        try:
            if not NOTES_PATH.is_dir():
                NOTES_PATH.mkdir(parents=True, exist_ok=True)
            if not NOTES_PATH_FLEETING.is_dir():
                NOTES_PATH_FLEETING.mkdir(parents=True, exist_ok=True)
        except Exception as OSError:
            print(OSError)
            exit(1)
        else:
            os.chdir(NOTES_PATH)  # Change to the directory that will contain the notes
            return NOTES_PATH


class DatabaseManage(SlipBox):
    """This class is a child of SlipBox, and it will create and manage the SQLite3 database"""

    def database_init(self):
        """Check if the database exists, if not then create it"""

        DB_PATH = Path(self.directory + '/slip_box.db')
        try:
            if not DB_PATH.is_file():
                DB_PATH.touch()
        except Exception as OSError:
            print(OSError)
            exit(1)


class FleetingZettel:
    """
    This class will be in charge of creating and managing the
    temporary(fleeting) notes:
        The title for each note will be based on this format: YYYYMMDDhhmm, for
        example 202212312359.md, this title will be generated from a function on
        the helpers_module and all of this notes will be saved under fleeting/
        under the default directory set by the environment variable
        ZETTELPY_DIR, this notes will not be stored on the database, and "title"
        will be the path to the note that is created each day.
    """

    def create_temp_note():
        TEMP_NOTE_PATH: Path = helper_module.get_date_as_path()
        if not TEMP_NOTE_PATH.exists():
            with open(TEMP_NOTE_PATH, 'w') as tempNote:
                tempNote.write(helper_module.temp_note_template(0))
        with open(TEMP_NOTE_PATH, 'a') as tempNote:
            tempNote.write(helper_module.temp_note_template(1))  # Insert time
            tempNote.write(helper_module.receive_from_stdin())  # Insert contents given through stdin
        subprocess.call(['nvim', '-c norm Go', TEMP_NOTE_PATH])
