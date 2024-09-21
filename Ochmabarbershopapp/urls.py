from django.urls import path
from .import views

path('', views.index, name="index"),
path('starter-page/', views.starter, name="starter"),

