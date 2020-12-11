import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 500, 500

root = tk.Tk()
root.title("Ma cyble")

canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")

liste_couleur = ["blue", "green", "black", "yellow", "magenta", "red"]

nombre_de_cercle = 30
epaisseur = CANVAS_WIDTH / 2 / nombre_de_cercle
for i in range(0, nombre_de_cercle):
    canvas.create_oval(epaisseur * i, epaisseur * i,
                       CANVAS_WIDTH - (epaisseur * i),
                       CANVAS_HEIGHT - (epaisseur * i),
                       fill=liste_couleur[i % len(liste_couleur)],
                       outline=liste_couleur[i % len(liste_couleur)])

canvas.grid()
root.mainloop()
