#!/usr/bin/env bash

echo -e "Creating python virtual environment"
python -m venv .zetenv

echo -e "Entering the virtual environment"
source ./.zetenv/bin/activate

echo -e "Updating pip"
pip install --upgrade pip

echo -e "Installing dependencies"
pip install -r requirements.txt >/dev/null

echo -e "Installing Zettelpy"
pip install -e . >/dev/null

echo -e "Leaving the virtual environment"
deactivate

echo -e "Modifying the launcher"
path_to_repo=$(realpath .)
path_to_venv=$path_to_repo/.zetenv/bin/activate
cp zettelpy/templates/zet zettelpy/templates/zet_user
sed -i "s|path_virt_env=|path_virt_env=$path_to_venv|" zettelpy/templates/zet_user >/dev/null

echo -e "Copying launcher"
cp zettelpy/templates/zet_user ~/.local/bin/zet
