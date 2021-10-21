from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)
    folder_path = models.CharField(max_length=200)


class Picture(models.Model):
    title = models.CharField(max_length=70)
    description = models.CharField(max_length=200, default=None, blank=True, null=True)
    file_path = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
