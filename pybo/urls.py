from django.urls import URLPattern, path
from . import views

URLPatterns=[
    path('', views.index),
    path('hello/', views.index),
    path('hello/3/', views.index),
]