from django import forms
from django.contrib.auth.forms import UserCreationForm

class ConnexionForm(UserCreationForm):
    username = forms.CharField(label="Nom d'utilisateur")
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

class InscriptionForm(UserCreationForm):
    username = forms.CharField(label="Nom d'utilisateur")
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    email = forms.EmailField(label="Adresse e-mail")
    nom = forms.CharField(label="Nom")
    prenom = forms.CharField(label="Prénom")
    telephone = forms.CharField(label="Téléphone")
    # Ajoutez d'autres champs d'inscription si nécessaire
