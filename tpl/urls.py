from django.urls import path
from . import views


urlpatterns = [

    path('find', views.find, name='find'),
    path('index', views.index, name='index'),

]
