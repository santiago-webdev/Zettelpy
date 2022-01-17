import os
from pathlib import Path
from zettelpy import helper_module


class SlipBox:
    """Instantiate an object that can create the directory hierarchy"""

    def __init__(self, directory: str) -> None:
        self.dir: Path = Path(directory)  # We put all our files in here
        self.dir_fleeting: Path = Path(self.dir, 'fleeting')  # Temp notes go here
        self.dir_last_note: Path = Path(self.dir, 'last_note')  # Temp notes go here

    def slipbox_init(self):
        """If the dir or the DB under the given path doesn't exist create it"""

        try:
            # Create the main directory
            if not self.dir.is_dir():
                self.dir.mkdir(parents=True, exist_ok=True)

            # Create the fleeting notes directory
            if not self.dir_fleeting.is_dir():
                self.dir_fleeting.mkdir(parents=True, exist_ok=True)

            # Create the file were we store the path to the last accessed note
            if not self.dir_last_note.is_file():
                self.dir_last_note.touch()
        except Exception as OSError:
            print(OSError)
            exit(1)
        else:
            os.chdir(self.dir)  # Change to the directory that will contain the notes
            return self.dir


class DatabaseManage(SlipBox):
    """Returns the path to the database"""

    def __init__(self, directory: Path) -> None:
        super().__init__(directory)
        self.db_path: Path = Path(directory, 'slip_box.db')  # This is the database

    def database_init(self):
        """Check if the database exists, if not then create it"""

        try:
            # Create the database
            if not self.db_path.is_file():
                self.db_path.touch()
        except Exception as OSError:
            print(OSError)
            exit(1)
        else:
            os.chdir(self.dir)
            return self.db_path


class Zettel(SlipBox):
    """Create a fleeting note or edit an existing one"""

    def __init__(self, directory: Path) -> None:
        super().__init__(directory)

    def modf_temp_note(self):
        NOTE_PATH: Path = helper_module.get_date_as_path(self.dir_fleeting)  # Get path
        # TODO: create helper function to call the editor via a function, plus make the
        # next if statement return the path of the file so that on the __main__ we can
        # call the editor at the end of the __main__ file.
        if not NOTE_PATH.is_file():  # If the file doesn't exists
            NOTE_PATH.touch()  # Create the file
            helper_module.template_do('title fleeting', NOTE_PATH)  # Insert a title
        else:
            helper_module.template_do('new insertion', NOTE_PATH)  # Insert subheader
        return NOTE_PATH
