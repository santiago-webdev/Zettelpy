# Zettelpy
A personal knowledge management system based on Zettelkasten

*Some notes:*

- This is a personal project that I started to learn a little bit of Python, meaning that it has a lot of bugs and
  missing features.
- I'm open to suggestions.
- I think this CLI only works in Unix like OSes.
- Make sure to be _inside_ the directory when running the installer
- Don't move or delete the repo because the launcher will not be able to find the virtual environment
- You need to add .local/bin to your \$PATH in order to launch this program
- To update you can `git pull`
- I don't know how this program behaves with GUI text editors, I only use terminal based text editors like Neovim.

## How to install
You can run the installer, and if you want to change the default directory in which the notes are stored you can export
an environment variable, the default directory is at ~/zettelpy

```bash
./install.sh

export ZETTELPY_DIR="${XDG_DATA_HOME}/zettelpy"
```

## How to uninstall
There is no uninstaller, you just need to delete some directories, so to uninstall you need to delete the repo, the
launcher, and the directory for storing the notes.

```bash
rm ~/path/to/this/repo/Zettelpy
rm ~/zettelpy # This is the default location of the notes
rm ~/.local/bin/zet # This is the launcher
```

## Dependencies
- Python 3.10
- To install this program and its dependencies you'll need pip
- A shell like bash or zsh
- To update the program you will need git

## Usage:
### Fleeting notes
You can use this mode which is the default mode to take quick notes.

```bash
zet
```

### Create notes with a title or ID
Use quotes for names with spaces. You also need to be aware that if you specify an extension different from .md it will
cause some problems because this project is intended to be used with markdown files, since it's just for notes.

```bash
zet "The Aleph"
```

*You don't need to specify the extension but using "The Aleph.md" would also work*

### Delete notes
If you have decided that you want to delete the note that you are editing, just empty the file that you are in, the file
and the row in the database will be deleted after you quit the file

### How do you link the notes?
By the name of this repo you can tell that this program was made with the intention of being used for the zettelkasten
method, the first one or two attempts of making this a usable tools I used ctags to link each file together, but now I
decided to use [this language server](https://github.com/artempyanykh/zeta-note).

## Flags

### Access to the last edited/viewed note
You can use the --last or -l flag, which will search your last accessed note, this doesn't include quick notes, only
permanent notes.

```bash
zet -l # Or --last
```

### Print the path
Use --path or -p, this flag prints the path to the note, so you can pipe it or use it on command substitution for other
programs to use, I use okular to view big markdown files, this will give you an idea of how to use it with other
commands:

```bash
okular "$(zet 'The Aleph' -p)" & # Don't forget the double quotes
disown
```

## TODO
1. Make the program work with IDs and even when the notes are in subdirectories
2. Find a fast way of searching through the notes
3. Create tools to fix errors introduced into the database
4. Being able to delete notes with a flag -d
5. Replace info automatically from the templates
