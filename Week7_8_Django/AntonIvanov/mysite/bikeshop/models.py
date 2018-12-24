from django.db import models


class Bike(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    brand = models.CharField(max_length=50, null=True, blank=True)
    bike_type = models.CharField(max_length=20, null=True, blank=True)
    wheel_size = models.CharField(max_length=10, null=True, blank=True)
