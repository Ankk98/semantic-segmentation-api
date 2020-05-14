#!/bin/bash
pwd
virtualenv "${PWD}/predict-with-deeplabv3/venv" --python=python3
source "${PWD}/predict-with-deeplabv3/venv/bin/activate"
which python
pip install -r requirements.txt
echo "Setup complete"