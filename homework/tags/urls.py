
from django.urls import path
from . import views

app_name = 'tags'

urlpatterns = [
    path('', views.main, name = "root"),
    path("<tag>", views.main, name = "main"),
    path('toptentags/', views.toptentags, name='toptentags'),
]