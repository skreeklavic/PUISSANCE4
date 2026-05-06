import IA
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
label_joueur = tk.Label(racine, text = "Tour du Joueur 1", fg = INTERFACE.COULEUR_JOUEUR1, font = ("Arial",16,"bold"))
label_joueur.pack(pady = 10)
#####
#Darys
def actualiser_affichage_joueur():
    """Met à jour le texte et la couleur du label en fonction du joueur actuel"""
    if INTERFACE.joueur_actuel == 1:
        label_joueur.config(text="Tour du Joueur 1", fg=INTERFACE.COULEUR_JOUEUR1)
    else:
        label_joueur.config(text="Tour du Joueur 2", fg=INTERFACE.COULEUR_JOUEUR2)
        
######## Darys et alexandre

# BUG 3 FIX : nouvelle_manche définie AVANT click qui l'appelle
score_joueur1 = 0
score_joueur2 = 0
def nouvelle_manche():
    INTERFACE.reset_grille(canvas)
    actualiser_affichage_joueur()
    GESTION.historique.clear()  ### vide l'historique pour la nouvelle manche
    if IA.MODE_de_jeu != 1 and INTERFACE.joueur_actuel == 2:
        IA.jouer_ia(canvas)
        actualiser_affichage_joueur()
 
# BUG 2 FIX : une seule fonction click qui fait tout (IA + victoire)
def click(event):
    global score_joueur1, score_joueur2 # On appelle les scores pour pouvoir les modifier
    
    colonne = event.x // TAILLE_CASE
    if 0 <= colonne < COLONNES:
        joueur_qui_vient_de_jouer = INTERFACE.joueur_actuel
        INTERFACE.placer_jeton(canvas, colonne)
        actualiser_affichage_joueur()
 
        ### VERIFICATION VICTOIRE JOUEUR HUMAIN
        if LOGIQUE.verifier_victoire(INTERFACE.grille, joueur_qui_vient_de_jouer):
            INTERFACE.partie_finie = True
            
            # 1. On ajoute 1 point au gagnant
            if joueur_qui_vient_de_jouer == 1:
                score_joueur1 += 1
            else:
                score_joueur2 += 1
                
            # 2. On récupère le nombre de manches nécessaires pour gagner le match
            manches_pour_gagner = GESTION.parametres["manches_gagnantes"]
            
            # 3. On vérifie si c'est la victoire finale
            if score_joueur1 >= manches_pour_gagner or score_joueur2 >= manches_pour_gagner:
                messagebox.showinfo("VICTOIRE FINALE !", "Le joueur " + str(joueur_qui_vient_de_jouer) + " remporte le match !\nScores finaux : J1 [" + str(score_joueur1) + "] - J2/IA [" + str(score_joueur2) + "]")
                # On remet les scores à 0 pour le prochain grand match
                score_joueur1 = 0
                score_joueur2 = 0
            else:
                messagebox.showinfo("Manche gagnée", "Le joueur " + str(joueur_qui_vient_de_jouer) + " gagne cette manche !\nScores : J1 [" + str(score_joueur1) + "] - J2/IA [" + str(score_joueur2) + "]")
            
            nouvelle_manche()
            return
 
        ### VERIFICATION MATCH NUL
        if LOGIQUE.verifier_match_nul(INTERFACE.grille):
            INTERFACE.partie_finie = True
            messagebox.showinfo("Match Nul", "La grille est pleine !\nScores : J1 [" + str(score_joueur1) + "] - J2/IA [" + str(score_joueur2) + "]")
            nouvelle_manche()
            return
 
        ### TOUR DE L'IA
        if IA.MODE_de_jeu != 1:
            if INTERFACE.joueur_actuel == 2:
                IA.jouer_ia(canvas)
                actualiser_affichage_joueur()
                
                ### VERIFICATION VICTOIRE IA
                if LOGIQUE.verifier_victoire(INTERFACE.grille, 2):
                    INTERFACE.partie_finie = True
                    score_joueur2 += 1
                    manches_pour_gagner = GESTION.parametres["manches_gagnantes"]
                    
                    if score_joueur2 >= manches_pour_gagner:
                        messagebox.showinfo("VICTOIRE FINALE !", "L'IA remporte le match !\nScores finaux : J1 [" + str(score_joueur1) + "] - IA [" + str(score_joueur2) + "]")
                        score_joueur1 = 0
                        score_joueur2 = 0
                    else:
                        messagebox.showinfo("Manche gagnée", "L'IA a gagné cette manche !\nScores : J1 [" + str(score_joueur1) + "] - IA [" + str(score_joueur2) + "]")
                        
                    nouvelle_manche()

canvas.bind("<Button-1>", click)

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
b_nouvelle_manche = tk.Button(boutons, text="Nouvelle Manche", command=nouvelle_manche, bg="#f39c12", fg="white", font=("Arial", 11, "bold"), padx=8)
b_nouvelle_manche.pack(side=tk.LEFT, padx=5)

def changer_taille():
    # 1. Demander les nouvelles dimensions (entre 4 et 15 pour éviter de casser l'écran)
    nv_lignes = simpledialog.askinteger("Taille", "Nombre de lignes :", minvalue=4, maxvalue=15, initialvalue=INTERFACE.LIGNES)
    nv_colonnes = simpledialog.askinteger("Taille", "Nombre de colonnes :", minvalue=4, maxvalue=15, initialvalue=INTERFACE.COLONNES)
    
    # Si l'utilisateur n'a pas fermé la fenêtre (annulation)
    if nv_lignes is not None and nv_colonnes is not None:
        # 2. Mettre à jour les variables dans INTERFACE.py
        INTERFACE.modifier_taille(nv_lignes, nv_colonnes)
        
        # 3. Mettre à jour le dictionnaire dans GESTION.py pour garder une trace
        GESTION.parametres["lignes"] = nv_lignes
        GESTION.parametres["colonnes"] = nv_colonnes
        
        # 4. Redimensionner le canvas (l'écran de dessin) dans main.py
        canvas.config(width=INTERFACE.COLONNES * INTERFACE.TAILLE_CASE * 1.14, height=INTERFACE.LIGNES * INTERFACE.TAILLE_CASE * 1.14)
        
        # 5. Relancer une manche propre pour dessiner la nouvelle grille
        nouvelle_manche()

b_taille = tk.Button(boutons, text="Taille Grille", command=changer_taille, bg="#8e44ad", fg="white", font=("Arial", 11, "bold"), padx=8)
b_taille.pack(side=tk.LEFT, padx=5)


racine.mainloop()
