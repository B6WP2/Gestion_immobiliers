from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
# Importez le modèle BienImmobilier et Utilisateur
from .models import BienImmobilier, CustomUser

def index(request):
    context = {"message": "Hello World !"}
    template = loader.get_template("App_immobiliers/index.html")
    return HttpResponse(template.render(context, request))
    
def home(request):
    return HttpResponse("Bienvenue sur la création d'une application de gestion de biens immobiliers")

# Vue pour la section "À propos"
def apropos(request):
    return HttpResponse("À propos de notre application de gestion de biens immobiliers")

# Vue pour la liste des biens immobiliers
def liste_biens_immobiliers(request):
    biens = BienImmobilier.objects.all()  # Récupérez tous les biens immobiliers depuis la base de données
    context = {'biens': biens}
    return render(request, 'App_immobiliers/liste_biens_immobiliers.html', context)

# Vue pour les détails d'un bien immobilier
def detail_bien_immobilier(request, bien_id):
    # Récupérez le bien immobilier spécifié par bien_id
    bien = BienImmobilier.objects.get(pk=bien_id)
    # Récupérez une liste d'autres biens immobiliers: les 5 premiers biens autres que celui en cours
    autres_biens = BienImmobilier.objects.exclude(pk=bien_id)[:5] 
    context = {'bien': bien, 'autres_biens': autres_biens}
    return render(request, 'App_immobiliers/detail_bien_immobilier.html', context)

# Vue pour gestion des utilisateurs
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import ConnexionForm, InscriptionForm

def connexion(request):
    if request.method == 'POST':
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Connexion réussie.')
                return redirect('home')  # Redirigez vers la page d'accueil après la connexion réussie
            else:
                # Gestion des erreurs de connexion
                messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
                pass
    else:
        form = ConnexionForm()
    return render(request, 'utilisateur/connexion.html', {'form': form})

def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            # Récupérez les données du formulaire
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            nom = form.cleaned_data['nom']
            prenom = form.cleaned_data['prenom']
            telephone = form.cleaned_data['telephone']
            
            # Créez un nouvel utilisateur avec les données
            user = User.objects.create_user(username=username, password=password, email=email)
            
            # Enregistrez les autres informations de l'utilisateur dans un modèle personnalisé si nécessaire
            utilisateur = CustomUser(nom=nom, prenom=prenom, telephone=telephone, user=user)
            utilisateur.save()
            
            # Connectez l'utilisateur après l'inscription
            login(request, user)
            messages.success(request, 'Inscription réussie.')
            
            return redirect('home')  # Redirigez vers la page d'accueil après l'inscription réussie
    else:
        form = InscriptionForm()
    return render(request, 'utilisateur/inscription.html', {'form': form})

def deconnexion(request):
    logout(request)
    messages.success(request, 'Déconnexion réussie.')
    return redirect('home')
