from django.contrib import admin
from django.urls import path
from . import views

app_name = 'authenticate'



urlpatterns = [
    path('login_page/', views.login_page, name='login_page'),
    path('logout_page/', views.logout_page, name='logout_page'),
    
    path('registration/', views.user_registration, name='registration')

]