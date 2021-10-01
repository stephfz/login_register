from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('logout', views.logout),
    path('register', views.register),
    path('home', views.home),
]