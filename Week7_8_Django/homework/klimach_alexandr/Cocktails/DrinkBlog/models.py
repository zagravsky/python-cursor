from django.db import models


class Cocktail(models.Model):
    name = models.CharField(max_length=50)
    recipe = models.TextField(max_length=1000)
    info = models.TextField()
    author = models.CharField(max_length=50)
    create_date = models.DateField(auto_now=False, auto_now_add=False)
