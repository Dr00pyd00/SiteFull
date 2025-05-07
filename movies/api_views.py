from django.shortcuts import render
import json
import requests
from django.http import JsonResponse


def api_film(request):
    
    film_name = request.GET.get('movie_title','').strip()   # strip pour enlever les espaces.
    
    # check si y'a rien dans la query
    if not film_name:
        return JsonResponse({'error':'No film match this titls!'},status=400)
    
    response = requests.get(f'https://www.omdbapi.com/?t={film_name}&apikey=824c66f0')
    print('response recu!')
    
    # check si le code d'erreur  different de 200:
    if  response.status_code != 200:
        return JsonResponse({'error':'External error!'}, status=502)
    
    data = response.json()
    
    # check si le titre est trouvé:
    if data.get('Response') == 'False':
        return JsonResponse({'error':'Movie not Found!'}, status=400)
    
    
    return JsonResponse(data)

