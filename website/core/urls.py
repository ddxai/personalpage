from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('category/<str:category_name>/', views.category, name='category'),
]
