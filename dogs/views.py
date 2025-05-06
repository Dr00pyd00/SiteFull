from django.shortcuts import render
from django.views.generic import DeleteView, DetailView, UpdateView, CreateView, ListView
from .models import Dog
from django.urls import reverse_lazy

# Create your views here.






#==================================================#
#========   Gestion par full django  ==============#

def index(request):
    return render(request, 'dogs/index.html')

class DogList(ListView):
    model = Dog
    context_object_name = 'dogs'
    
    
class DogCreate(CreateView):
    model = Dog
    fields = '__all__'
    success_url = reverse_lazy('dogs:dog_list')
    
class DogDelete(DeleteView):
    model = Dog
    success_url = reverse_lazy('dogs:dog_list')
    
class DogUpdate(UpdateView):
    model = Dog
    fields = '__all__'
    success_url = reverse_lazy('dogs:dog_list')
    
class DogDetail(DetailView):
    model = Dog
    context_object_name = 'dog'
    
    
    


#================================================#
#============== Gestion par JS et API ===========#

def dog_list_by_api(request):
    return render(request, 'dogs/api_dog_list.html')
    
    
    