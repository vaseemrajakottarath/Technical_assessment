from django import views
from django.urls import path
from . import views

urlpatterns=[
     path('login',views.login,name='user_login'),
     path('',views.home,name='home')
    ]