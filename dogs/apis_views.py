from django.http import JsonResponse
from .models import Dog
import json




def dog_list(request):
    
    # si on demande a regarder:
    if request.method == 'GET':
        dogs = Dog.objects.all()
        data = [
            {
                'id': dog.id,
                'name': dog.name,
                'description': dog.description,
                'image': dog.image.url if dog.image else None,
            }
            for dog in dogs
        ]
        return JsonResponse(data=data, safe=False)
    
    # si on veut ajouter une data:
    elif request.method == 'POST':       

        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        
        new_dog = Dog.objects.create(
            name=name,
            description=description,
            image=image
        )
        
        return JsonResponse({'id': new_dog.id})