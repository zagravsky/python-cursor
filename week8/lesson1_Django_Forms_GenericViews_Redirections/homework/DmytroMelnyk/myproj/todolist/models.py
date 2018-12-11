# coding=utf-8
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from ckeditor_uploader.fields import RichTextUploadingField


class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = RichTextUploadingField(null=True, blank=True, verbose_name="Text")
    create_at = models.DateTimeField(default=datetime.now, verbose_name="Date")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, verbose_name="Created by")

    def __str__(self):
        return self.title


GENDER_CHOICES = [
    ['male', u"Мужской"],
    ['female', u"Женский"],
]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="User")
    avatar = models.FileField(verbose_name="Avatar", null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True, null=True, verbose_name="About you")
    city = models.CharField(max_length=30, blank=True, null=True, verbose_name="City")
    gender = models.CharField(max_length=10, verbose_name=u"Пол", choices=GENDER_CHOICES, default="male")
