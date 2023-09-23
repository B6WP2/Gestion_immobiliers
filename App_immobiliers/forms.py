from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, BienImmobilier  # Assurez-vous d'importer le modèle CustomUser depuis votre application

class ConnexionForm(forms.Form):  # Utilisez `forms.Form` au lieu de `UserCreationForm` pour le formulaire de connexion
    username = forms.CharField(label="Nom d'utilisateur")
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

class InscriptionForm(UserCreationForm):
    email = forms.EmailField(label="Adresse e-mail")
    nom = forms.CharField(label="Nom")
    prenom = forms.CharField(label="Prénom")
    telephone = forms.CharField(label="Téléphone")
    # Ajoutez d'autres champs d'inscription si nécessaire

    class Meta:
        model = CustomUser  # Spécifiez le modèle CustomUser
        fields = UserCreationForm.Meta.fields  # Utilisez les champs du modèle par défaut

        
class BienImmobilierForm(forms.ModelForm):
    class Meta:
        model = BienImmobilier
        fields = ['nom', 'types', 'prix', 'disponibilite', 'images']
        labels = {
            'nom': 'Nom du bien',
            'types': 'Types',
            'prix': 'Prix',
            'disponibilite': 'Disponibilité',
            'images': 'Images',
        }
        
         