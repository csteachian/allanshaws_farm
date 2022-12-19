from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('gallery', views.gallery),
    path('contact', views.contact),
    path('links', views.links),
]
