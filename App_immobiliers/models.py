from django.db import models

class BienImmobilier(models.Model):
    nom = models.CharField(max_length=255)
    types = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    disponibilite = models.BooleanField(default=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    images = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.nom

# Modèle de données utilisateur personnalisé en étendant le modèle de base User de Django
#from django.contrib.auth.models import AbstractUser

#class CustomUser(AbstractUser):
    # Ajoutez des champs personnalisés ici, par exemple, un champ de numéro de téléphone.
    #phone_number = models.CharField(max_length=15, blank=True, null=True)
