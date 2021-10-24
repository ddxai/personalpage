from django.shortcuts import render, get_object_or_404

from .models import Category, Social, About


def index(request):
    category_list = Category.objects.order_by('id')
    context = {'category_list': category_list}
    return render(request, 'core/index.html', context)


def about(request):
    category_list = Category.objects.order_by('id')
    social_list = Social.objects.order_by('id')
    try:
        about_obj = About.objects.order_by('id')[0]
        text_about = about_obj.text
        photo = about_obj.photo
    except About.DoesNotExist:
        text_about = ' '
        photo = None
    context = {'category_list': category_list, 'social_list': social_list, 'text_about': text_about, 'photo': photo}
    return render(request, 'core/about.html', context)


def category(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    picture_list = category.picture_set.order_by('-id')
    category_list = Category.objects.order_by('id')
    context = {'category': category, 'picture_list': picture_list, 'category_list': category_list}
    return render(request, 'core/category.html', context)
