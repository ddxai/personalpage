from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Picture(models.Model):
    title = models.CharField(max_length=70)
    description = models.CharField(max_length=200, default=None, blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

