from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  path('',views.demo,name='demo'),
  path('login/',views.login,name='login'),
  path('register/',views.register,name='register'),
  path('logout/',views.logout,name='logout'),
  path('about',views.about,name='about'),
  path('apply/',views.apply,name='apply')
]