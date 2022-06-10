from django import views
from django.urls import path
from . import views

urlpatterns=[
    path('login',views.login,name='admin_login'),
    path('',views.home,name='admin_home'),
    path('logout',views.logout,name='admin_logout'),
    path('createuser',views.create_user,name='createuser'),
    path('department',views.department,name='department'),
    path('add_department',views.add_department,name='add_department'),
    path('update_department/<int:pk>',views.update_department,name='update_department'),
    path('delete_department/<int:pk>',views.delete_department,name='delete_department'),
    path('ticket',views.ticket,name='ticket'),
    path('create_ticket',views.create_ticket,name='admin_ticket'),
]   