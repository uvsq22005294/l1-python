import tkinter as tk

HEIGHT = 800
WIDTH = 800

racine = tk.Tk()

canvas = tk.Canvas(racine, bg="red", height=HEIGHT, width=WIDTH)
canvas.grid(column=0, row=0)

largeur = 100

colors = ["black", "white"]
cpt = 0
for j in range(8):
    for i in range(9):
        cpt = 1 - cpt
        print(cpt, end=" ")
        canvas.create_rectangle((i * largeur, j * largeur), ((i + 1) * largeur, (j + 1) * largeur), fill = colors[cpt])
    print()


racine.mainloop()