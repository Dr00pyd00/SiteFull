
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', include('home.urls')), 

    path('auth/', include('authenticate.urls')),

    path('cats/', include('cats.urls')),

    path('js_first/', include('js_first.urls')),

    
]
