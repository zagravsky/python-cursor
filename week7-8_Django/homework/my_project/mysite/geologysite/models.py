from django.db import models
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField


class MineralModel(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    formula = models.CharField(max_length=50, null=True, blank=True)
    colour = models.CharField(max_length=100, null=True, blank=True)
    luster = models.CharField(max_length=100, null=True, blank=True)
    streak = models.CharField(max_length=100, null=True, blank=True)
    hardness = models.FloatField(null=True, blank=True)
    density = models.FloatField(null=True, blank=True)
    avatar = models.ImageField(upload_to='image/')
    description = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name


class RockModel(models.Model):
    name = models.CharField(max_length=50)
    min_composition = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    avatar = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100)
    body = RichTextUploadingField(blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.title
