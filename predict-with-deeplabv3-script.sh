#!/bin/bash
pwd
# source "${PWD}/predict-with-deeplabv3/venv/bin/activate"
pyenv local venvSSA
echo 'path of python: ---------------------------------------------------------------'
which python
ls "${PWD}/predict-with-deeplabv3/dataset"
python ./predict-with-deeplabv3/inference.py --infer_data_list "${PWD}/predict-with-deeplabv3/dataset/infer.txt" --model_dir "${PWD}/predict-with-deeplabv3/model" --data_dir "${PWD}/predict-with-deeplabv3/dataset/" --output_dir "${PWD}/predict-with-deeplabv3/dataset/inference_output"
