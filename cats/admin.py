from django.contrib import admin
from .models import Breed, Cat

# Register your models here.

admin.site.register(Cat)
admin.site.register(Breed)