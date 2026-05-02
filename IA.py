import random
import INTERFACE

# #################################### alexandre énorme aide de claude surtout pour l'ia 2 et 3 
# 1 = joueur vs joueur 2 (Normal)
# 2 = joueur vs IA (Random)
# 3 = joueur vs IA (Heuristique - scorification)
# 4 = joueur vs IA (Minimax - arbre de décison)
#######################################
MODE_de_jeu = 1 ################################## selection ici ##################

def ia_random():
    colonne = random.randint(0, INTERFACE.COLONNES - 1) #### choisi une colone aléaroirement 
    while INTERFACE.colonne_pleine(colonne) == True:  ###
        colonne = random.randint(0, INTERFACE.COLONNES - 1)
    return colonne  ### renvoir  la colonne choisie
    
################
def ia_heuristique():
    a =a

###############

def ia_minimax():
    b=b

###############""""



def jouer_ia(canvas): ########### appelle la bonne ia selon le mode choisi

    if MODE_de_jeu == 2:
        colonne = ia_random()
        INTERFACE.placer_jeton(canvas, colonne)
    elif MODE_de_jeu == 3:
        colonne = ia_heuristique()
        INTERFACE.placer_jeton(canvas, colonne)
    elif MODE_de_jeu == 4:
        colonne = ia_minimax()
        INTERFACE.placer_jeton(canvas, colonne)
 
