from django.urls import path
from . import views
urlpatterns = [
    path('read_cookie', views.set_cookie, name='read_cookie'),
    # path('set_cookie', views.set_cookie, name='set_cookie')

]
