import argparse
import subprocess
import os
import datetime
from configparser import ConfigParser
from pathlib import Path  # Manage paths


def cli() -> argparse.Namespace:  # Parse the arguments

    parser = argparse.ArgumentParser(prog='zettelpy',
        description='Personal Knowledge System based on Zettelkasten')

    parser.add_argument('destination', nargs='?', type=Path, default='Fleeting',
        help='Provide path/Title or Luhmann-ID to go to note')

    parser.add_argument('-v', '--view', action='store_true',
        help='Open a note by title, ID, or by lastNoteUsed')

    parser.add_argument('-i', '--index', action='store_true',
        help='Shows the index in your editor of choice')

    return parser.parse_args()


def cli_config():  # Parse the user configurations, or use defaults

    CONFIG_LOCATE = (os.environ['XDG_CONFIG_HOME'] + '/zettelpyrc.ini')

    if not os.path.exists(CONFIG_LOCATE):  # Check if config file exists
        default_config = ConfigParser()
        default_config['settings'] = {
            'NOTES_DIRECTORY': (os.environ['XDG_DATA_HOME'] + '/zettelpy'),
            'NOTES_EDITOR': (os.environ['EDITOR']),
            'NOTES_VIEW': 'okular'
            }
        with open(CONFIG_LOCATE, 'w') as userConfig:
            default_config.write(userConfig)
            print('The config file has been created in', CONFIG_LOCATE,
                    'go there and change it with the settings that you want')
            exit(0)

    config = ConfigParser()
    config.read(CONFIG_LOCATE)

    return config


def index_notes(notes_directory, notes_editor, index=False):
    if index is True:  # Redoes the index and clean empty files
        subprocess.Popen(['.utils/zettelpy-redo-notes', notes_directory])
        subprocess.run([notes_editor, 'index.md'])
        exit(0)


def retrieve_path(dest: Path):
    if str(dest) == 'lastOpenedNote':  # lastOpenedNote
        with open('.utils/lastOpenedNote', 'r') as lastOpenedNote:
            return lastOpenedNote.read().rstrip('\n')

    elif str(dest).startswith('@'):  # Luhmann-ID
        try:
            return str(subprocess.check_output(['rg', '-w', '-l', '## ' + str(dest)]))[2:-3]
        except Exception as t:
            print(t)

    elif str(dest) == 'Fleeting':  # Fleeting notes
        todays_note = ('Fleeting/note-' + datetime.date.today().strftime("%Y-%m-%d") + '.md')
        todays_title = ('# Notes for ' + datetime.date.today().strftime("%b %d, %Y") + '\n')
        hours_title = ('\n# At ' + str(datetime.datetime.now().strftime("%H:%M")))
        if not os.path.exists(todays_note):  # If the note doesn't exists, create it
            with open(todays_note, 'w+') as fleetingNote:
                fleetingNote.write(todays_title + "\n\n")
        with open(todays_note, 'a') as fleetingNote:  # Insert hour each time you enter the note
            fleetingNote.write(hours_title + "\n\n")
        return todays_note
    else:
        return dest
