document.addEventListener("DOMContentLoaded", function() {
    var boutonConnexion = document.getElementById('ouvrirModalConnexion');
    var boutonInscription = document.getElementById('ouvrirModalInscription');
    var fenetreModaleConnexion = document.getElementById('fenetreModaleConnexion');
    var fenetreModaleInscription = document.getElementById('fenetreModaleInscription');

    boutonConnexion.addEventListener('click', function() {
        // Ouvrir la fenêtre modale de connexion
        fenetreModaleConnexion.style.display = 'block';
    });

    boutonInscription.addEventListener('click', function() {
        // Ouvrir la fenêtre modale d'inscription
        fenetreModaleInscription.style.display = 'block';
    });
});
