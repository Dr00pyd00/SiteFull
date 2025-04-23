from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.


# utilisation de validators :

# race 
class Breed(models.Model):
    name = models.CharField(max_length=300,
                            validators=[MinLengthValidator(2, 'la race doit contenir plus de lettres !')]
                            )
    def __str__(self):
        return self.name 
    

# chat
class Cat(models.Model):
    nickname = models.CharField(max_length=300,
                                validators=[MinLengthValidator(2, "le nickname doit contenir plus d'une lettre!")])
    weight = models.PositiveIntegerField()
    food = models.CharField(max_length=300)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nickname
    
