import random

def choisir_premier_joueur():
    return random.randint(1, 2)



def verifier_victoire():

      








def verifier_match_nul(grille):
    for c in range(7):
        if grille[0][c] == 0: 
            return False
    return True
      
      
      
def afficher_resultat(vainqueur):
    if vainqueur == 0:
        print("Match nul ! La grille est pleine.") 
    elif vainqueur == 1:
        print("Félicitations ! Le joueur 1 a gagné la manche.") 
        
    elif vainqueur == 2:
        print("Félicitations ! Le joueur 2 a gagné la manche.") 
