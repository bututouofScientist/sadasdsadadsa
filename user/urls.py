from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('detailview/<int:pk>', views.UserDetailView.as_view(), name='detailview'),
    path('listview', views.UserListView.as_view(), name='listview'),
    path('gotobd', views.UserRedirectView.as_view(url='https://www.baidu.com'), name='gotobd'),
    path('home', views.HomeView.as_view(), name='home'),
    path('', views.UserView.as_view(), name=''),
    path('logout', views.logout, name='logout'),
    path('index', views.index, name='index'),
    path('login', views.login, name='login')
]