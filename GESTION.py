
historique =[]

def enregistré_un_coup(ligne,colone):  ###pile
    coup = (ligne,colone)
    historique.append(coup)


def annulation_coup(plateau):  #trouver le bon nom
    plateau
    if len(historique)==0:
        print("IMPOSSIBLE AUCUN COUPS N'A ETE JOUé")
        return
    if len(historique) >0:
        ligne_avant, colone_avant = historique.pop()


    plateau[ligne_avant][colone_avant]=0

    print("coup annulé en ligne = ",ligne_avant,"et colone = ",colone_avant)


parametres = { "manches_gagnantes": 1, "lignes": 6, "colonnes": 7 }

def nombreDeMANcheGAgnante(nombreShouaite): ###choisi et verifier le nombre de manche gagnante
    if type(nombreShouaite) == int and nombreShouaite > 0:
        parametres["manches_gagnantes"]= nombreShouaite
        print("dorénavant il faut ",nombreShouaite," manches pour gagné")
    else:
        print("Erreur : Le nombre de manches doit être un entier positif")
