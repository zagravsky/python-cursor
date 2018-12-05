from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from ckeditor_uploader.fields import RichTextUploadingField


class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = RichTextUploadingField(null=True, blank=True)
    create_at = models.DateTimeField(default=datetime.now, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.title
