from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Importation des methodes et modèles issus des modules locaux
from .models import BienImmobilier, CustomUser
from .forms import ConnexionForm, InscriptionForm, BienImmobilierForm

def index(request):
    context = {"message": "Hello World !"}
    template = loader.get_template("App_immobiliers/index.html")
    return HttpResponse(template.render(context, request))
    
# Vue pour la page d'accueil
def home(request):
    return render(request, 'App_immobiliers/home.html')

# Vue pour la page "À propos"
def apropos(request):
    return render(request, 'App_immobiliers/apropos.html')

# Vue pour la liste des biens immobiliers
def liste_biens_immobiliers(request):
    # Récupérez la liste des biens immobiliers depuis la base de données
    liste_biens_immobiliers = BienImmobilier.objects.all()
    context = {
        'liste_biens_immobiliers': liste_biens_immobiliers,
    }
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
def inscription(request):
    # Check if the request method is POST
    if request.method == 'POST':
        # Create an instance of the form with the POST data
        form = InscriptionForm(request.POST)
        # Check if the form is valid
        if form.is_valid():
            # Get the cleaned data from the form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            nom = form.cleaned_data['nom']
            prenom = form.cleaned_data['prenom']
            telephone = form.cleaned_data['telephone']
            
            # Create a new user with the form data
            user = CustomUser.objects.create_user(username=username, password=password, email=email)
            
            # Save the other user information in the custom user model
            utilisateur = CustomUser(nom=nom, prenom=prenom, telephone=telephone, user=user)
            utilisateur.save()
            
            # Log in the user after successful registration
            login(request, user)
            messages.success(request, 'Inscription réussie.')
            
            # Redirect to the home page after successful registration
            return redirect('gestion_immobiliers')
    else:
        # Create an instance of the form
        form = InscriptionForm()
    
    # Render the template with the form
    return render(request, 'utilisateur/inscription.html', {'form': form})

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
                return redirect('gestion_immobiliers')  # Redirigez vers la page d'accueil après la connexion réussie
            else:
                # Gestion des erreurs de connexion
                messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    else:
        form = ConnexionForm()
    return render(request, 'utilisateur/connexion.html', {'form': form})

def deconnexion(request):
    logout(request)
    messages.success(request, 'Déconnexion réussie.')
    return redirect('index')

# Création de vue pour ajouter un bien immobilier 
@login_required
def ajouter_bien_immobilier(request):
    if request.method == 'POST':
        form = BienImmobilierForm(request.POST, request.FILES)
        if form.is_valid():
            # Sauvegardez le bien immobilier dans la base de données
            bien_immobilier = form.save()
            
            # Récupérez la liste mise à jour des biens immobiliers
            liste_biens_immobiliers = BienImmobilier.objects.all()
            
            # Passez cette liste mise à jour à votre modèle de formulaire ou de contexte
            form.fields['gestion_immobiliers'] = liste_biens_immobiliers
            
            return redirect('gestion_immobiliers')  # Redirigez vers la liste des biens immobiliers après l'ajout
    else:
        form = BienImmobilierForm()
    return render(request, 'App_immobiliers/ajouter_bien_immobilier.html', {'form': form})



# Création d'une vue pour modifier un bien immobilier existant.
@login_required
def modifier_bien_immobilier(request, bien_immobilier_id):
    bien_immobilier = get_object_or_404(BienImmobilier, pk=bien_immobilier_id)

    if request.method == 'POST':
        form = BienImmobilierForm(request.POST, request.FILES, instance=bien_immobilier)
        if form.is_valid():
            form.save()
            
            # Récupérez la liste mise à jour des biens immobiliers
            liste_biens_immobiliers = BienImmobilier.objects.all()
            
            # Passez cette liste mise à jour à votre modèle de formulaire ou de contexte
            form.fields['gestion_immobiliers'] = liste_biens_immobiliers
            
            return redirect('gestion_immobiliers')  # Redirigez vers la liste des biens immobiliers après la modification
    else:
        form = BienImmobilierForm(instance=bien_immobilier)
    return render(request, 'App_immobiliers/modifier_bien_immobilier.html', {'form': form, 'bien_immobilier': bien_immobilier})


# Création d'une vue pour supprimer un bien immobilier.
@login_required
def supprimer_bien_immobilier(request, bien_immobilier_id):
    bien_immobilier = get_object_or_404(BienImmobilier, pk=bien_immobilier_id)
    bien_immobilier.delete()
    return redirect('gestion_immobiliers')  # Redirigez vers la liste des biens immobiliers après la suppression

