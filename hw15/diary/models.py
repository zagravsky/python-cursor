from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150, null=True, blank=False)
    content = models.CharField(max_length=5000, null=True, blank=False)
    author = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return f"{self.title} by {self.author}"
