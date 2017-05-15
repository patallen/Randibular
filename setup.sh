#!/bin/zsh
source ~/.zshrc
mkvirtualenv pytesting
echo "Sleeping.... zZzZz"
sleep 1
workon pytesting
$HOME/.virtualenvs/pytesting/bin/pip install -r requirements.txt

