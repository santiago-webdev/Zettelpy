import argparse
from os import getenv
from .slip_box import DatabaseManage


def cli() -> argparse.Namespace:
    """Parses the user arguments"""
    parser = argparse.ArgumentParser(prog='zettelpy', description='Personal Knowledge System based on Zettelkasten')
    parser.add_argument('luhmann-id', nargs='?', type=str, default='', help='Provide path or id of the note')
    parser.add_argument('-p', '--path', action='store_true', help='Shows real path of the note')
    return parser.parse_args()


def main():
    NOTES_DIR: str = getenv('ZETTELPY_DIR')  # Directory used to the notes
    user_args = cli()  # Arguments given by the user

    checks_slip_box = DatabaseManage(NOTES_DIR)
    checks_slip_box.slipbox_init()
    checks_slip_box.database_init()

    # # Receive input from standard input
    # if not sys.stdin.isatty():
    #     data = sys.stdin.read()
    #     print(data.strip())


if __name__ == '__main__':
    main()
