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
    