from rest_framework import serializers
from .models import Prediction

class InputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prediction
        fields = "__all__"