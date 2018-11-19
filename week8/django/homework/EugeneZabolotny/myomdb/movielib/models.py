from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=6000, null=False, blank=False)
    poster = models.BinaryField(blank=True)
