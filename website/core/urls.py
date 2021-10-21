from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='About'),
    path('contacts/', views.contacts, name='Contacts'),
    path('category/<str:category_name>/', views.category, name='Category'),
]
