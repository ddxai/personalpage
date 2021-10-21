from django.http import HttpResponse


def index(request):
    return HttpResponse("Homepage")


def about(request):
    return HttpResponse("About")


def contacts(request):
    return HttpResponse("Contacts")


def category(request, category_name):
    return HttpResponse("Category: %s" % category_name)
