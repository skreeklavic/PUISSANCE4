# PUISSANCE4
PUISSANCE4 projet in200

teste

Il reste encore plusieurs éléments à ajouter pour le projet de Puissance 4 :

8. la possibilité de modifier le nombre de lignes et de colonnes


## Répartition du travail

###  Sarah — Logique de jeu (`LOGIQUE.py`)
- [ ] Compléter `verifier_victoire(grille, joueur)` — ligne, colonne, diagonale
- [ ] Brancher la victoire dans `MAIN.py` après chaque coup
- [ ] Brancher `verifier_match_nul()` dans `MAIN.py`
- [ ] Brancher `choisir_premier_joueur()` dans `MAIN.py` (actuellement jamais appelée) choisi au harsard
- [ ] Appeler `afficher_resultat()` via une popup tkinter

###  Darys — Interface visuelle (`INTERFACE.py`)
- [x] Grille + jetons + gravité
- [ ] Animation des jetons (tomber visuellement case par case)
- [ ] Label graphique "Joueur X à toi" + numéro de manche ( 5. un petit message graphique indiquant la manche actuelle et le joueur en cours)
- [ ] Réinitialiser la grille pour une nouvelle manche

###  Adshaya — Interface graphique (`INTERFACE.py` + `MAIN.py`)
- [x] Vérifier si la colonne est pleine + bloquer le dépôt
- [x] Alternance des joueurs
- [ ] Bouton "Rejouer" (nouvelle manche / reset grille)
- [ ] Boutons Sauvegarder / Charger dans l'interface 
- [ ] Bloquer les clics quand la partie est terminée

###  Alexandre — Gestion & données (`GESTION.py` + `MAIN.py`)
- [x] Popup nombre de manches au lancement
- [x] Structure historique + annulation logique
- [ ] Brancher bouton "Annuler" + Ctrl+Z dans `MAIN.py`
- [ ] Fonctions `sauvegarder_partie()` et `charger_partie()` en JSON
- [ ] Boutons Sauvegarder / Charger dans `MAIN.py`
- [ ] IA ( séléction et développement)







‎ 
‎ 
‎ 
‎ 
‎ 
‎ 
‎ 
‎ 
‎ 
‎ 
‎ 
‎ ‎ 

‎ 
 1. la détection de victoire
2. l’affichage d’un message de victoire
9. la sauvegarde de la partie
10. les boutons pour sauvegarder et charger une partuie
8. la possibilité de modifier le nombre de lignes et de colonnes
7. une intelligence artificielle (IA)
6. la sélection du type d’IA
5. un petit message graphique indiquant la manche actuelle et le joueur en cours
4. implemantation annuler le coups
3. Gestion du match nul
1. Le joueur qui d´ebute la partie est choisi au hasard.
2. ajouter la fonction rejoué
3. annimation des jetons



