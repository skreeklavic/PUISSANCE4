import INTERFACE
import LOGIQUE
import GESTION







racine = tk.Tk()
racine.title("Puissance 4")
canvas = tk.Canvas(racine,background=COULEUR_VIDE, width = LIGNES * TAILLE_CASE, height=COLONNES * TAILLE_CASE )
canvas.pack()
dessine_grille()
racine.mainloop()
