from django.db import models
from django.urls import reverse

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
    photo_de_profil = models.ImageField(upload_to='photos_de_profil/', blank=True, null=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return self.username
    
    def get_full_name(self):
        return f"{self.prenom} {self.nom}"

    def get_profile_image(self):
        if self.photo_de_profil:
            return self.photo_de_profil.url
        else:
            # Image par défaut.
            return 'chemin/par/defaut/vers/l/image/de/profil.png' 

    def get_profile_url(self):
        # Assurez-vous que 'profil' est le nom de l'URL de la vue de profil.
        return reverse('profil') 

    def is_logged_in(self):
        return self.is_authenticated

    def is_admin(self):
        return self.is_staff

    def get_logout_url(self):
        # Assurez-vous que 'deconnexion' est le nom de l'URL de la vue de déconnexion.
        return reverse('deconnexion') 