from PIL import Image
from ckeditor.fields import RichTextField
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


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


@receiver(post_save, sender=Picture)
def create_slug(sender, instance, *args, **kwargs):
    max_size = (1920, 1920)
    img = Image.open(instance.image)
    img.thumbnail(max_size, Image.LANCZOS)
    img.save(instance.image.path)


class Social(models.Model):
    name = models.CharField(max_length=20)
    link = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class About(models.Model):
    text = RichTextField(blank=True, null=True)
    photo = models.ImageField(upload_to='images/about/', blank=True, null=True)

    def __str__(self):
        return self.text
