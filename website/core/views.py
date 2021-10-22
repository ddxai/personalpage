from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import Category


def index(request):
    category_list = Category.objects.order_by('id')
    context = {'category_list': category_list}
    return render(request, 'core/index.html', context)


def about(request):
    return HttpResponse('About')


def contacts(request):
    return HttpResponse('Contacts')


def category(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    picture_list = category.picture_set.order_by('-id')
    context = {'category': category, 'picture_list': picture_list}
    return render(request, 'core/category.html', context)
