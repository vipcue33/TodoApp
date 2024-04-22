from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
##start
urlpatterns = [
    path('', views.home),
    path('add', views.add_task, name='addtask'),
    path('get', views.get_tasks, name='gettasks'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='home.html'), name='logout'),
]