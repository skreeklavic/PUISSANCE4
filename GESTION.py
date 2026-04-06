
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
