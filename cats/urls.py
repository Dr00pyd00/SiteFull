from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'cats'



urlpatterns = [
        path('', views.MainView.as_view(), name='cat_list'),

        ### gestion de chat:
        # creation d'un chat
        path('create/', views.CatCreate.as_view(), name='cat_create'),
        # update d'un chat:
        path('update/<int:pk>/', views.CatUpdate.as_view(), name='cat_update'),
        # delete d'un chat:
        path('delete/<int:pk>/', views.CatDelete.as_view(), name='cat_delete'),
        # detail d'un chat:
        path('detail/<int:pk>/', views.CatDetail.as_view(), name='cat_detail'),

        ### gestion des races
        # list des races dispos:
        path('breeds/list/', views.BreedList.as_view(), name='breed_list'),
        # creation race:
        path('breeds/creation/', views.BreedCreate.as_view(), name='breed_create'),
        # update d'une race:
        path('breeds/update/<int:pk>/', views.BreedUpdate.as_view(), name='breed_update'),
        # delete d'une race:
        path('breeds/delete/<int:pk>/', views.BreedDelete.as_view(), name='breed_delete'),



]