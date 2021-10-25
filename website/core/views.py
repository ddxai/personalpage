from django.shortcuts import render, get_object_or_404

from .models import Category, Social, About


def index(request):
    category_list = Category.objects.order_by('id')
    pic_list = []
    for cat in category_list:
        pic_queryset = cat.picture_set.order_by('-id')
        if pic_queryset.exists():
            pic_list.append(pic_queryset[0])
    if pic_list:
        pic_list = sorted(pic_list, key=lambda p: p.image.height)
        height_sum = 0
        for pic in pic_list:
            height_sum += pic.image.height

        sum_col1 = sum_col2 = height_sum / 2
        pic_list_col1, pic_list_col2 = [], []
        for pic in pic_list:
            if sum_col1 >= sum_col2:
                pic_list_col1.append(pic)
                sum_col1 -= pic.image.height
            else:
                pic_list_col2.append(pic)
                sum_col2 -= pic.image.height
    else:
        pic_list_col1 = pic_list_col2 = None
    context = {'category_list': category_list, 'pic_list_col1': pic_list_col1, 'pic_list_col2': pic_list_col2}
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
