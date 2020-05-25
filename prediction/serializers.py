from rest_framework import serializers
from .models import Prediction
import os
import subprocess
from shutil import copyfile


def perform_inference(path):
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print("base path----------" + base_path)
    code_path = (
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        + "/predict-with-deeplabv3"
    )
    print("model path---------" + code_path)
    infer_script_path = base_path + "/predict-with-deeplabv3-script.sh"
    print("inference script path------------" + infer_script_path)
    dataset_path = code_path + "/dataset"
    print("dataset path-----------------" + dataset_path)
    destination_path = dataset_path + "/image.png"
    print("destination path-------------" + destination_path)

    print("initial path of image -------------------------------" + path)
    copyfile(path, destination_path)

    inference_script = code_path + "/inference.py"
    inference_data_list = code_path + "/dataset/infer.txt"
    inference_model_dir = code_path + "/model"
    inference_data_dir = code_path + "/dataset"
    inference_output_dir = code_path + "/dataset/inference_output"
    inferrence_command = [
        "python3",
        inference_script,
        "--infer_data_list",
        inference_data_list,
        "--model_dir",
        inference_model_dir,
        "--data_dir",
        inference_data_dir,
        "--output_dir",
        inference_output_dir,
    ]

    # call script to run inference file

    subprocess.run(inferrence_command)

    path_of_result_img = dataset_path + "/inference_output/image_mask.png"
    result_path = "/media/images/image.png"
    destination2_path = base_path + result_path
    copyfile(path_of_result_img, destination2_path)

    return result_path


class InputSerializer(serializers.ModelSerializer):

    input_image_url = serializers.SerializerMethodField("get_input_image_url")
    output_image_url = serializers.SerializerMethodField("get_output_image_url")

    class Meta:
        model = Prediction
        fields = "__all__"

    def get_input_image_url(self, obj):
        """ Returns the path of input image wrt django server."""
        return obj.img.url

    def get_output_image_url(self, obj):
        """ Returns the path of output image wrt django server."""
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print("project location--------------" + BASE_DIR)
        path_of_img = BASE_DIR + obj.img.url
        print("path of image--------------" + path_of_img)
        path_of_result_img = BASE_DIR + perform_inference(path_of_img)
        print("path of result image--------------" + path_of_result_img)
        return path_of_result_img
