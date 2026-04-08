import INTERFACE
import LOGIQUE
import GESTION
import tkinter as tk

from INTERFACE import COULEUR_VIDE, LIGNES, COLONNES, TAILLE_CASE







racine = tk.Tk()
racine.title("Puissance 4")
canvas = tk.Canvas(racine, background=COULEUR_VIDE, width=COLONNES * TAILLE_CASE, height=LIGNES * TAILLE_CASE)
canvas.pack()
INTERFACE.dessine_grille(canvas)
racine.mainloop()
