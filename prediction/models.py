from django.db import models


class Prediction(models.Model):
    img = models.ImageField(upload_to="images/")
