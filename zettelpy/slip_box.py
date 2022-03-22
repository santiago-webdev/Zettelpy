import os
import sqlite3
from pathlib import Path
from zettelpy import utils_module as utils  # Import helper functions


# SlipBox
class SlipBox:
    """Instantiate an object that can create the directory hierarchy"""

    def __init__(self, directory: str) -> None:
        self.dir: Path = Path(directory)  # We put all our files in here
        self.dir_fleeting = Path(self.dir, "fleeting")  # Temp notes go here
        self.dir_permanent = Path(self.dir, "permanent")  # Permanent notes go here
        self.dir_last_note = Path(self.dir, "last_note")  # Temp notes go here

    def slipbox_init(self):
        """If the dir or the DB under the given path doesn't exist create it"""

        try:
            # Create the main directory
            if not self.dir.is_dir():
                self.dir.mkdir(parents=True, exist_ok=True)

            # Create the fleeting notes directory
            if not self.dir_fleeting.is_dir():
                self.dir_fleeting.mkdir(parents=True, exist_ok=True)

            # Create the permanent notes directory
            if not self.dir_permanent.is_dir():
                self.dir_permanent.mkdir(parents=True, exist_ok=True)

            # Create the file were we store the path to the last accessed note
            if not self.dir_last_note.is_file():
                self.dir_last_note.touch()
        except Exception as OSError:
            print(OSError)
            exit(1)
        else:
            os.chdir(self.dir)  # Change to the directory that will contain the notes
            return self.dir


# DatabaseManage
class DatabaseManage(SlipBox):
    """Manage the SQLite3 database, which will store the paths to each note"""

    def __init__(self, directory: Path) -> None:
        super().__init__(directory)  # Inherit from SlipBox
        self.db_path = Path(directory, "slip_box.db")  # This is the database

    def database_init(self):
        """Check if the database exists, if not create it and the table"""
        if self.db_path.is_file():
            return
        conn = sqlite3.connect(self.db_path)
        with conn:
            conn.cursor().execute(
                """ CREATE TABLE notes (
                    note_id INTEGER PRIMARY KEY NOT NULL,
                    title   TEXT NOT NULL,
                    path    TEXT NOT NULL,
                    date    TEXT NULL,
                    UNIQUE(title)
                    )"""
            )

    def insert_note(self, TITLE: str, REAL_PATH: Path) -> Path:
        """
        There's no duplicates, the database will hold only one row for note, meaning
        that this entry will be created just once, and every other requests to INSERT
        will be ignored
        """
        connection = sqlite3.connect(self.db_path)  # Connect to the database
        with connection:
            connection.cursor().execute(
                """INSERT OR IGNORE INTO notes (title, path, date) VALUES ('{}', '{}',
                DATETIME('now'))""".format(
                    TITLE, REAL_PATH
                )
            )

    def return_path(self, TITLE: str) -> Path:
        """
        This function returns either a None or a tuple with just one element when it
        finds something on the database
        """
        connection = sqlite3.connect(self.db_path)  # Connect to the database
        with connection:
            cur = connection.cursor()
            cur.execute(
                "SELECT path FROM notes WHERE title='{}'".format(Path(TITLE).stem)
            )
            connection.commit()
            return cur.fetchone()

    def delete_row_and_file(self, TITLE: Path):
        """
        (Query is by title of the note) This function not only deletes the note from the
        table, but also deletes the file from the filesystem
        """
        connection = sqlite3.connect(self.db_path)  # Connect to the database
        with connection:
            try:
                connection.cursor().execute(
                    "DELETE FROM notes WHERE title='{}'".format(Path(TITLE).stem)
                )
                connection.commit()
                os.remove(TITLE)  # Remove the file
                print("Successfully deleted the note")
            except Exception as OSError:
                print(OSError)
                print("The note doesn't exists or was already deleted")
                exit(1)


# Zettel
class Zettel(SlipBox):
    """
    Create notes, either permanent ones(modf_zettel), or temporary ones(modf_temp_note)
    """

    def __init__(self, directory: Path) -> None:
        super().__init__(directory)

    def modf_temp_note(self) -> Path:
        # Get path as date with the root being self.dir_fleeting
        NOTE_PATH = utils.get_date_as_path(self.dir_fleeting)

        if not NOTE_PATH.is_file():  # If the file doesn't exists
            NOTE_PATH.touch()  # Create the file
            utils.template_do("title fleeting", NOTE_PATH)  # And insert title
        else:
            utils.template_do("new insertion", NOTE_PATH)  # Insert subheader

        utils.receive_from_stdin(NOTE_PATH)  # Write anything coming from stdin
        return NOTE_PATH

    def modf_zettel(self, TITLE_ZETTEL: Path) -> Path:
        if not TITLE_ZETTEL.is_file():  # If the file doesn't exists
            TITLE_ZETTEL.touch()  # Create the file
            utils.template_do("title zettel", TITLE_ZETTEL)  # And insert title
        utils.receive_from_stdin(TITLE_ZETTEL)
        return TITLE_ZETTEL
