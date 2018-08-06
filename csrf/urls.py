from django.urls import path
from . import views

app_name = 'csrf'

urlpatterns = [
    path('index1', views.index1, name='index1'),
    path('index2', views.index2, name='index2'),
    path('index', views.index, name='index')
]