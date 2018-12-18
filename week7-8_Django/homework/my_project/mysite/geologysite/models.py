from django.db import models
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse


class MineralModel(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    formula = models.CharField(max_length=50, null=True, blank=True)
    colour = models.CharField(max_length=100, null=True, blank=True)
    luster = models.CharField(max_length=100, null=True, blank=True)
    streak = models.CharField(max_length=100, null=True, blank=True)
    hardness = models.FloatField(null=True, blank=True)
    density = models.FloatField(null=True, blank=True)
    avatar = models.ImageField(upload_to='image/')
    description = models.TextField(max_length=5000, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail_mineral', args=[str(self.id)])


class RockModel(models.Model):
    name = models.CharField(max_length=50)
    min_composition = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)
    avatar = models.ImageField(upload_to='image/')
    field_task3 = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail_rock', args=[str(self.id)])


class Article(models.Model):
    title = models.CharField(max_length=100)
    body = RichTextUploadingField(blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, null=True)
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article', args=[str(self.id)])
