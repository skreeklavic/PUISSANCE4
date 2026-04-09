import INTERFACE
import LOGIQUE
import GESTION
import tkinter as tk
from tkinter import simpledialog,   messagebox
from INTERFACE import COULEUR_VIDE, LIGNES, COLONNES, TAILLE_CASE



##### pop up pour nombre de manche
def demander_nb_manches():
    nbombre = simpledialog.askinteger(
        "Nombre de manches",
        "Combien de manches faut-il gagner pour remporter la partie ?",
        minvalue=1, maxvalue=10,
        initialvalue=1)
    if nbombre is None:  ###c'esr que l'utilistauer a fermé la boite
        nbombre = 1
    GESTION.nombreDeMANcheGAgnante(nbombre)
 
demander_nb_manches()
########




racine = tk.Tk()
racine.title("Puissance 4")
canvas = tk.Canvas(racine, background=COULEUR_VIDE, width=COLONNES * TAILLE_CASE, height=LIGNES * TAILLE_CASE)
canvas.pack()
INTERFACE.dessine_grille(canvas)


def on_clic(event):
   colonne = event.x // TAILLE_CASE
   if 0 <= colonne < COLONNES:
     INTERFACE.placer_jeton(canvas, colonne)

canvas.bind("<Button-1>", on_clic)



racine.mainloop()
