from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import BienImmobilier  # Importez le modèle BienImmobilier

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