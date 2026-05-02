import INTERFACE
import LOGIQUE
import GESTION
import tkinter as tk
from tkinter import simpledialog,   messagebox , filedialog
from INTERFACE import COULEUR_VIDE, LIGNES, COLONNES, TAILLE_CASE



##### pop up pour nombre de manche alexandre |aide chat gpt
def demander_nb_manches():
    nbombre = simpledialog.askinteger("Nombre de manches","Combien de manches faut-il gagner pour remporter la partie ?",minvalue=1, maxvalue=10,initialvalue=1)
    if nbombre is None:  ###c'esr que l'utilistauer a fermé la boite
        nbombre = 1
    GESTION.nombreDeMANcheGAgnante(nbombre)
 
demander_nb_manches()
#############



###"#darys
racine = tk.Tk()
racine.title("Puissance 4")
canvas = tk.Canvas(racine, background=COULEUR_VIDE, width=COLONNES * TAILLE_CASE, height=LIGNES * TAILLE_CASE)
canvas.pack()
INTERFACE.dessine_grille(canvas)

######## Darys et alexandre

def click(event):
   colonne = event.x // TAILLE_CASE
   if 0 <= colonne < COLONNES:
     INTERFACE.placer_jeton(canvas, colonne)  ### le joueur humain joue
     if IA.MODE_de_jeu != 1:  ### si on est pas en mode 1v1                         # avec ia
       if INTERFACE.joueur_actuel == 2:  ### si c est maintenant le tour de l ia
         IA.jouer_ia(canvas)  ### l ia joue

#def click(event):
 #  colonne = event.x // TAILLE_CASE
  # if 0 <= colonne < COLONNES:             # sans ia
   #  INTERFACE.placer_jeton(canvas, colonne)

########################

################### alexandre aide de claude ( nouveau module pour la gestion de fichier )
# fonction
def sauvegarder():### sert a selectionner l'endroit et le nom de la sauvergarde
    nom_fichier = filedialog.asksaveasfilename(title="Sauvegarder la partie",defaultextension=".json",filetypes=[("Fichier JSON", "*.json")],initialfile="partie.json")

    GESTION.sauvegarder_partie(INTERFACE.grille, INTERFACE.joueur_actuel, nom_fichier)
    messagebox.showinfo("Sauvegarde", "Partie sauvegardée !")
 
def charger():# permet de chosiisri le fichier que le joueur veux ouvrir puis de redefinir le plateau avec les données sauvergaéd
    nom_fichier = filedialog.askopenfilename(title="Charger une partie",filetypes=[("Fichier JSON", "*.json")])

    donnees = GESTION.charger_partie(nom_fichier)
    ligne = 0
    while ligne < LIGNES: #### parcours le plateau actuelle pour le remplacer par la matreci du json
        colonne = 0
        while colonne < COLONNES:
            INTERFACE.grille[ligne][colonne] = donnees["plateau"][ligne][colonne]
            colonne += 1
        ligne += 1
    INTERFACE.joueur_actuel = donnees["joueur_actuel"]
    INTERFACE.dessine_grille(canvas)
    messagebox.showinfo("Chargement", "Partie chargée !")
# boutons
 
boutons = tk.Frame(racine) #####tout cela sert a definir les boutons sauvergarder et charger
boutons.pack(pady=5)
 
bsauvegarder = tk.Button(boutons, text="Sauvegarder", command=sauvegarder,bg="#2980b9", fg="white", font=("Arial", 11, "bold"), padx=8)
bsauvegarder.pack(side=tk.LEFT, padx=5)
 
bcharger = tk.Button(boutons, text="Charger", command=charger,bg="#27ae60", fg="white", font=("Arial", 11, "bold"), padx=8)## padx = taille
bcharger.pack(side=tk.LEFT, padx=5)
##########"
def annuler():  
    annulation = GESTION.annulation_coup(INTERFACE.grille) 
    if annulation == True:  # 
        INTERFACE.changer_joueur()  # reviens a l'ancien joeur joeur 
        INTERFACE.dessine_grille(canvas)  # on rgrille sans le jeton

bannuler = tk.Button(boutons, text="Annuler", command=annuler, bg="#e74c3c", fg="white", font=("Arial", 11, "bold"), padx=8)
bannuler.pack(side=tk.LEFT, padx=5)


#######




racine.mainloop()
