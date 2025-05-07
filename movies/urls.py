from django.urls import path
from . import views, api_views
from django.views.generic import TemplateView


app_name = 'movies'

urlpatterns = [
        
        path('index', TemplateView.as_view(template_name='movies/index.html'), name='index'),

        path('search/', views.searchMovie.as_view(), name='movie_search'),
        
        path('search_back/', views.searchMovieApi.as_view(), name='movie_search_api'),
        
        # API:
        path('api_request/', api_views.api_film, name='movie_api'),
    
]