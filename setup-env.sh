#!/bin/bash
echo "Current Directory: "
pwd
echo "Installing python 3.6.8: "
pyenv install 3.6.8
echo "Setting up virtualenv with python 3.6.8: "
pyenv virtualenv 3.6.8 venvSSA
echo "Using the virtualenv: "
pyenv local venvSSA
echo "Location of python using: "
which python
python --version
which pip
pip --version
pip install -r "${PWD}/requirements.txt"
echo "Setup complete"

# pyenv virtualenv 3.6.8 "${PWD}/predict-with-deeplabv3/venv"
# source "${PWD}/predict-with-deeplabv3/venv/bin/activate"