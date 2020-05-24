from rest_framework import serializers
from .models import Prediction


class InputSerializer(serializers.ModelSerializer):

    input_image_url = serializers.SerializerMethodField("get_input_image_url")
    output_image_url = serializers.SerializerMethodField("get_output_image_url")

    class Meta:
        model = Prediction
        fields = "__all__"

    def get_input_image_url(self, obj):
        return obj.img.url

    def get_output_image_url(self, obj):
        result_path = "/media/images/image.png"
        return result_path
