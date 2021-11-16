import os
import argparse
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
            'notes_directory': (os.environ['XDG_DATA_HOME'] + '/zettelpy'),
            'notes_editor': (os.environ['EDITOR']),
            'notes_view': 'okular',
            'use_db': 'no'
            }
        with open(CONFIG_LOCATE, 'w') as userConfig:
            default_config.write(userConfig)
            print('The config file has been created in', CONFIG_LOCATE,
                    'go there and change it with the settings that you want')
            exit(0)

    config = ConfigParser()
    config.read(CONFIG_LOCATE)

    return config
