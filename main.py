import INTERFACE
import LOGIQUE
import GESTION







racine = tk.Tk()
racine.title("Puissance 4")
canvas = tk.Canvas(racine,background=COULEUR_VIDE, width = LIGNES * 100, height=COLONNES * 100 )
canvas.pack()
dessiner_grille()
racine.mainloop()
