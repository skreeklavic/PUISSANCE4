################### alexandre
from json import *

historique =[]

def enregistré_un_coup(ligne,colone):  ###pile
    coup = (ligne,colone)
    historique.append(coup)


def annulation_coup(plateau):  
    plateau
    if len(historique)==0:
        print("IMPOSSIBLE AUCUN COUPS N'A ETE JOUé")
        return False
    if len(historique) >0:
        ligne_avant, colone_avant = historique.pop()
    plateau[ligne_avant][colone_avant]=0
    print("coup annulé en ligne = ",ligne_avant,"et colone = ",colone_avant)
    return True


parametres = { "manches_gagnantes": 1, "lignes": 6, "colonnes": 7 }

def nombreDeMANcheGAgnante(nombreShouaite): ###choisi et verifier le nombre de manche gagnante
    if type(nombreShouaite) == int and nombreShouaite > 0:
        parametres["manches_gagnantes"]= nombreShouaite
        print("dorénavant il faut ",nombreShouaite," manches pour gagné")
    else:
        print("Erreur : Le nombre de manches doit être un entier positif")

####


 
def sauvegarder_partie(plateau, joueur_actuel, nom_fichier="sauvegarde.json"):
    donnees = {}
    donnees["plateau"] = plateau
    donnees["joueur_actuel"] = joueur_actuel
    donnees["historique"] = historique
    donnees["manches_gagnantes"] = parametres["manches_gagnantes"]
 
    fichier = open(nom_fichier, "w")
    dump(donnees, fichier, indent=4)
    fichier.close()
    print("Partie sauvegardée dans", nom_fichier)
 
def charger_partie(nom_fichier="sauvegarde.json"):
    fichier = open(nom_fichier, "r")
    strn = fichier.read()
    fichier.close()
 
    donnees = loads(strn)
 
    historique.clear()
    i = 0
    while i < len(donnees["historique"]):
        historique.append(tuple(donnees["historique"][i]))
        i += 1
 
    parametres["manches_gagnantes"] = donnees["manches_gagnantes"]
    print("Partie chargée depuis", nom_fichier)
    return donnees


####################
