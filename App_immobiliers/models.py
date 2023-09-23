from django.db import models

class BienImmobilier(models.Model):
    nom = models.CharField(max_length=255)
    types = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=0)
    disponibilite = models.BooleanField(default=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    images = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.nom
    
    
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Ajoutez ici des champs supplémentaires si nécessaire
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return self.username