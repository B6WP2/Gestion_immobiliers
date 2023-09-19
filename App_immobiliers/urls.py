from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='accueil'),  # URL de la page d'accueil
    
    path('home/', views.home, name='home'),  # URL de la page d'accueil

    # URL pour la section "À propos"
    path('a-propos/', views.apropos, name='apropos'),

    # URL pour la liste (les détails) des biens immobiliers
    path('biens-immobiliers/', views.liste_biens_immobiliers, name='liste_biens_immobiliers'),
 
    # URL pour la gestion de l'utilisateur (connexion, inscription, etc.)
    path('utilisateur/', views.gestion_utilisateur, name='gestion_utilisateur'),
    # path('login/', CustomLoginView.as_view(), name='login'),
    # path('logout/', CustomLogoutView.as_view(), name='logout'),
]