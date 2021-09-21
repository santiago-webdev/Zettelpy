#!/usr/bin/env bash

# Default path for storing the notes
notesDirectory="${XDG_DATA_HOME}/zettelpy"

# Checks if you are executing the script inside the repo
if [[ ! -d 'needed' && 'zettelpy' ]]; then
    echo 'You need to execute this script from inside the Zettelpy repo'
    exit
fi

# Creates the basic file structure
mkdir -p "$notesDirectory"/{.utils,Fleeting} || echo "Problems creating the directories"

# Copies one shell script that I use to clean the directory, refresh the tags and
# reload the index.md file
echo $notesDirectory
cp needed/zettelpy-redo-notes "$notesDirectory"/.utils/zettelpy-redo-notes
cp -r needed/.ctags.d "$notesDirectory"/
cp needed/.rgignore "$notesDirectory"/
