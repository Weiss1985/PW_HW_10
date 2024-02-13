
from django.urls import path
from . import views

app_name = 'authors'

urlpatterns = [
    path('', views.main, name = "root"),
    path("<author>", views.main, name = "main"),
]