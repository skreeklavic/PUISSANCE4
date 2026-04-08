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


def dessiner_jeton(ligne,colonne):
    #Dessine un jeton
    centre_x = colonne * TAILLE_CASE + TAILLE_CASE // 2
    centre_y = ligne * TAILLE_CASE + TAILLE_CASE // 2
    if grille[ligne][colonne] == 1:
        couleurs = COULEUR_JOUEUR1
    else:
        couleurs = COULEUR_JOUEUR2
    
    canvas.create_oval(centre_x - 50,centre_y + 50, centre_x + 50, centre_y - 50, fill = couleurs)
def dessiner_grille():
    #Dessine la grille de jeu 

    for ligne in range(LIGNES):
        for colonne in range(COLONNES):
            x1 = colonne * TAILLE_CASE
            y1 = ligne * TAILLE_CASE
            x2 = x1 + TAILLE_CASE
            y2 = y1 + TAILLE_CASE
            canvas.create_rectangle(x1, y1, x2, y2, fill="blue")



