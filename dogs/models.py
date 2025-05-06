from django.db import models

# Create your models here.

class Dog(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    image = models.ImageField(upload_to='dogs_images/')
    
    def __str__(self):
        return self.name