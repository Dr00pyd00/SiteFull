from django.shortcuts import render
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic import ListView, DetailView, View
from .models import Cat, Breed
from django.urls import reverse_lazy

# gestion d'accesibilité
# il faut creer et gerer : Settings.LOGIN_URL = 'path_de_log'
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


# j'utilise des classes Views only!



# page general:
class MainView(LoginRequiredMixin, View):
    def get(self, request):
        cat_list = Cat.objects.all()
        number_of_breed = Breed.objects.count()
        ctx = {'nb_breed': number_of_breed, 'cat_list':cat_list}
        return render(request, 'cats/cat_list.html', ctx)




### Gestion des chats ###
#########################

# creation d'un chat:
class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:cat_list')

# update d'un chat:
class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:cat_list')

# delete d'un chat:
class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    success_url = reverse_lazy('cats:cat_list')

# detail d'un chat :
class CatDetail(LoginRequiredMixin, DetailView):
    model = Cat
    context_object_name = 'cat'


### Gestion des Races###
########################

# list des races:
class BreedList(LoginRequiredMixin, ListView):
    model = Breed

# detail d'une race: ( ne sert PAS)
class BreedDetail(LoginRequiredMixin, DetailView):
    model = Breed
    context_object_name = 'breed'

# creation d'une race:
class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:breed_list')

# suppression d'une race:
class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    success_url = reverse_lazy('cats:breed_list')

# update d'une race:
class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:breed_list')



