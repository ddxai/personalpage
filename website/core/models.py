from ckeditor.fields import RichTextField
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Picture(models.Model):
    title = models.CharField(max_length=70)
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Social(models.Model):
    name = models.CharField(max_length=20)
    link = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class About(models.Model):
    text = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.text
