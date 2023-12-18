from django.urls import path
from django.contrib.auth import views as auth_views

from authapp.views import index, register

app_name = 'authapp'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register')
]