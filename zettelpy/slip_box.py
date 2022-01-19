import os
import sqlite3
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
    def __init__(self, directory: Path) -> None:
        super().__init__(directory)
        self.db_path: Path = Path(directory, 'slip_box.db')  # This is the database

    def database_init(self):
        """Check if the database exists, if not create it and the table"""

        try:
            if self.db_path.is_file():
                return

            self.db_path.touch()  # Create it
            conn = sqlite3.connect(self.db_path)  # Connect to the database
            # cursor_db.execute("DROP TABLE IF EXISTS notes")
            conn.cursor().execute(
                """
                CREATE TABLE notes (
                    note_id         INTEGER PRIMARY KEY AUTOINCREMENT,
                    luhmann_id      TEXT,
                    path            TEXT
                )"""
            )
            conn.commit()
            conn.close()
        except Exception as OSError:
            print(OSError)
            exit(1)
        else:
            os.chdir(self.dir)  # Change to the directory that will contain the notes
            return True


class Zettel(SlipBox):
    def __init__(self, directory: Path) -> None:
        super().__init__(directory)

    def modf_temp_note(self) -> Path:
        NOTE_PATH: Path = helper_module.get_date_as_path(self.dir_fleeting)  # Get path
        if not NOTE_PATH.is_file():  # If the file doesn't exists
            NOTE_PATH.touch()  # Create the file
            helper_module.template_do('title fleeting', NOTE_PATH)  # Insert a title
        else:
            helper_module.template_do('new insertion', NOTE_PATH)  # Insert subheader
        return NOTE_PATH

    # def modf_zettel(self) -> Path:
    #     DatabaseManage(self.dir).table_creation()
