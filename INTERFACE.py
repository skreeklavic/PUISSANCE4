#Darys
LIGNES = 6
COLONNES = 7
TAILLE_CASE = 80
COULEUR_VIDE = "white"
COULEUR_JOUEUR1 = "red"
COULEUR_JOUEUR2 = "yellow"


grille = []

for i in range(LIGNES):
    ligne = [0] * COLONNES
    grille.append(ligne)


def dessiner_jeton(canvas,ligne,colonne):
    #Dessine un jeton
    centre_x = colonne * TAILLE_CASE + TAILLE_CASE // 2
    centre_y = ligne * TAILLE_CASE + TAILLE_CASE // 2
    if grille[ligne][colonne] == 1:
        couleurs = COULEUR_JOUEUR1
    else:
        couleurs = COULEUR_JOUEUR2
    
    canvas.create_oval(centre_x - 50,centre_y + 50, centre_x + 50, centre_y - 50, fill = couleurs)
def dessine_grille():

    #Dessine une grille de puissance 4,Darys

    canvas.delete("all")

    for ligne in range(LIGNES):
        for colonne in range(COLONNES):
            x1 = colonne * TAILLE_CASE
            y1 = ligne * TAILLE_CASE
            x2 = x1 + TAILLE_CASE
            y2 = y1 + TAILLE_CASE

            canvas.create_rectangle(x1, y1, x2, y2,fill="white", outline="black", width=2)
# Redessine les jetons déjà posés, Alexandre 
       for ligne in range(LIGNES):
        for colonne in range(COLONNES):
            if grille[ligne][colonne] != 0:
                dessiner_jeton(canvas, ligne, colonne)
#A
joueur_actuel = 1

def colonne_pleine(colonne):
    return grille[0][colonne] != 0

partie_finie = False

def placer_jeton(canvas, colonne):
    global partie_finie
    if partie_finie:
        return
    if colonne_pleine(colonne):
        print("Colonne pleine, impossible de déposer ici")
        return
    for ligne in range(LIGNES -1, -1, -1):
        if grille[ligne][colonne] == 0:
            grille[ligne][colonne] = joueur_actuel
            dessiner_jeton(canvas, ligne, colonne)
            break
    changer_joueur()

def changer_joueur():
    global joueur_actuel
    if joueur_actuel == 1:
        joueur_actuel = 2
    else:
        joueur_actuel = 1

#bouton rejouer appuyer
def reset_grille():
    global grille, joueur_actuel, partie_finie
    for i in range(LIGNES):
        for j in range(COLONNES):
            grille[i][j] = 0
    partie_finie = False
    joueur_actuel = 1
    dessiner_grille()




