from django.shortcuts import render
from django.views.generic import View

# Create your views here.


# le fectch non securisé en front:
class searchMovie(View):
    def get(self, request):
        return render(request, 'movies/movie_search.html')
        
# gestion api en back JsonResponse:
class searchMovieApi(View):
    def get(self, request):
        return render(request, 'movies/movie_search_python.html')
