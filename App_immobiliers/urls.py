from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='accueil'),  # URL de la page d'accueil
    
    path('home/', views.home, name='home'),  # URL de la page d'accueil

    # URL pour la section "À propos"
    path('a-propos/', views.apropos, name='apropos'),

    # URL pour la liste (les détails) des biens immobiliers
    path('biens-immobiliers/', views.liste_biens_immobiliers, name='gestion_immobiliers'),
    path('biens-immobiliers/<int:bien_id>/', views.detail_bien_immobilier, name='detail_bien_immobilier'),
    
    # Ajouter un bien immobilier
    path('ajouter-bien-immobilier/', views.ajouter_bien_immobilier, name='ajouter_bien_immobilier'),
    
    # Modifier un bien immobilier (utilisez un identifiant dynamique, par exemple, l'ID du bien immobilier)
    path('modifier-bien-immobilier/<int:bien_immobilier_id>/', views.modifier_bien_immobilier, name='modifier_bien_immobilier'),
    
    # Supprimer un bien immobilier (utilisez un identifiant dynamique, par exemple, l'ID du bien immobilier)
    path('supprimer-bien-immobilier/<int:bien_immobilier_id>/', views.supprimer_bien_immobilier, name='supprimer_bien_immobilier'),
 
    # URL pour la gestion de l'utilisateur (connexion, inscription, etc.)
    path('profil/', views.profil, name='profil'),
    path('connexion/', views.connexion, name='connexion'),
    path('inscription/', views.inscription, name='inscription'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('modifier_profil/', views.modifier_profil, name='modifier_profil'),
    path('suppression_compte/', views.suppression_compte, name='suppression_compte'),
]