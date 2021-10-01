from .parse_module import cli, cli_config
from .SlipBox import SlipBox, Zettel # Import objects
from .func_module import index_notes, retrieve_path  # Import functions


def main():
    configs = cli_config()  # Parse the user configurations, or use defaults

    NOTES_DIRECTORY = configs.get('settings', 'notes_directory')

    NOTES_EDITOR = configs.get('settings', 'notes_editor')

    NOTES_VIEW = configs.get('settings', 'notes_view')

    args = cli()  # The arguments come from argparse

    checks_slip_box = SlipBox(NOTES_DIRECTORY)  # Creates object in the define directory
    checks_slip_box.initialize_box()  # Checking if all the directories inside it exists

    index_notes(NOTES_DIRECTORY, NOTES_EDITOR, args.index)

    actual_path_note = retrieve_path(args.destination)

    edit_zettel = Zettel(actual_path_note, args.view)
    edit_zettel.create_zettel(NOTES_VIEW, NOTES_EDITOR)  # Edit/create the note


if __name__ == '__main__':
    main()

# TODO
# Implement pathlib correctly and not use a combination of Path and strings which is wrong
