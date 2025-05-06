from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [

        path('search/', views.searchMovie.as_view(), name='movie_search'),
    
]