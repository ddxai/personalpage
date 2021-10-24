from django.contrib import admin

from .models import Category, Picture, About, Social

admin.site.register(Category)
admin.site.register(Picture)
admin.site.register(About)
admin.site.register(Social)
