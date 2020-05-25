#!/bin/bash
echo "Make sure you have pyenv installed."
echo "Current Directory: "
pwd
echo "Installing python 3.6.8: "
pyenv install 3.6.8
echo "Setting up virtualenv with python 3.6.8 with name venvSSA: "
pyenv virtualenv 3.6.8 venvSSA
echo "Using the virtualenv venvSSA: "
pyenv local venvSSA
echo "Location of python using: "
which python
python --version
which pip
pip --version
echo "Installing requirements: "
pip install -r "${PWD}/requirements.txt"
echo "Setup complete"
