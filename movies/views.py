from django.shortcuts import render
from django.views.generic import View

# Create your views here.


class searchMovie(View):
    def get(self, request):
        return render(request, 'movies/movie_search.html')
        