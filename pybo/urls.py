from django.urls import URLPattern, path
from . import views

urlpatterns=[
    path('', views.index),
    path('hello/', views.index),
    path('hello/3/', views.index),
]