import random
import INTERFACE

# ####################################
# 1 = joueur vs joueur 2 (Normal)
# 2 = joueur vs IA (Random)
# 3 = joueur vs IA (Heuristique - scorification)
# 4 = joueur vs IA (Minimax - arbre de décison)
#######################################
MODE_de_jeu = 1 ################################## selection ici ##################

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
 
