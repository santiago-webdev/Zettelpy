#!/usr/bin/env bash

echo -e "Creating python virtual environment"
python -m venv .zetenv

echo -e "Entering the virtual environment"
source ./.zetenv/bin/activate

echo -e "Installing dependencies"
pip install -r requirements.txt

echo -e "Installing Zettelpy"
pip install -e .

echo -e "Leaving the virtual environment"
deactivate

echo -e "Modifying the launcher"
path_to_repo=$(realpath .)
path_to_venv=$path_to_repo/.zetenv/bin/activate
cp needed/zet needed/zet_user
sed -i "s|path_virt_env=|path_virt_env=$path_to_venv|" needed/zet_user

echo -e "Copying launcher"
cp needed/zet_user ~/.local/bin/zet
