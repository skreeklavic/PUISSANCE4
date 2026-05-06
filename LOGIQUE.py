#Sara

##choisir aléatoirement qui commence
import random

def choisir_premier_joueur():
    return random.randint(1, 2)


##détection de la victoire
def verifier_victoire(grille, joueur):
    for r in range(6):
        for c in range(4):
            if grille[r][c] == joueur and grille[r][c+1] == joueur and \
               grille[r][c+2] == joueur and grille[r][c+3] == joueur:
                return True

    for c in range(7):
        for r in range(3):
            if grille[r][c] == joueur and grille[r+1][c] == joueur and \
               grille[r+2][c] == joueur and grille[r+3][c] == joueur:
                return True

    for c in range(4):
        for r in range(3):
            if grille[r][c] == joueur and grille[r+1][c+1] == joueur and \
               grille[r+2][c+2] == joueur and grille[r+3][c+3] == joueur:
                return True

    for c in range(4):
        for r in range(3, 6):
            if grille[r][c] == joueur and grille[r-1][c+1] == joueur and \
               grille[r-2][c+2] == joueur and grille[r-3][c+3] == joueur:
                return True

    return False


##détection du match nul
def verifier_match_nul(grille):
    for c in range(7):
        if grille[0][c] == 0: 
            return False
    return True
      
      
##affichage du message de fin      
def afficher_resultat(vainqueur):
    if vainqueur == 0:
        print("Match nul ! La grille est pleine.") 
    elif vainqueur == 1:
        print("Félicitations ! Le joueur 1 a gagné la manche.") 
        
    elif vainqueur == 2:
        print("Félicitations ! Le joueur 2 a gagné la manche.") 
