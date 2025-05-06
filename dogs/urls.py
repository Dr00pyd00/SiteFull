from django.urls import path
from . import views
from .import apis_views

app_name = 'dogs'

urlpatterns = [
    
        path('', views.index, name='index'),
        
        # gestion django
        
        path('list/', views.DogList.as_view(), name='dog_list'),
        
        path('create/', views.DogCreate.as_view(), name='dog_create'),
        
        path('delete/<int:pk>', views.DogDelete.as_view(), name='dog_delete'),
        
        path('update/<int:pk>/', views.DogUpdate.as_view(), name='dog_update'),
        
        path('detail/<int:pk>/', views.DogDetail.as_view(), name='dog_detail'),
    
    
        # gestion api js:
        
        path('with_api/list/', views.dog_list_by_api, name='dog_list_by_api'),
    
        # APIS :
        
        path('api_dog_list/', apis_views.dog_list, name='dog_api_list' ),
]




