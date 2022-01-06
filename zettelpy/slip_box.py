import os
from pathlib import Path  # Manage paths


class SlipBox:
    """This class will instantiate an object that can check or create the directory, and the database for the notes"""

    def __init__(self, directory):
        self.directory = directory

    def slipbox_init(self):
        """In this method if the directory or the database under the given path does not exist then create it"""

        NOTES_PATH = Path(self.directory)
        try:
            # Base directory
            if not NOTES_PATH.is_dir():
                NOTES_PATH.mkdir(parents=True, exist_ok=True)
        except Exception as OSError:
            print(OSError)
            exit(1)
        finally:
            os.chdir(NOTES_PATH)  # Change to the directory that will contain the notes


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
