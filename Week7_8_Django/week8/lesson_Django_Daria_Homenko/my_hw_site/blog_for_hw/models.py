from django.db import models

# Create models


class Flowers(models.Model):
    flower_name = models.CharField(max_length=50, null=True, blank=True)
    flower_description = models.CharField(max_length=5000, null=True, blank=True)
    flower_image = models.CharField(max_length=200, null=True, blank=True)

