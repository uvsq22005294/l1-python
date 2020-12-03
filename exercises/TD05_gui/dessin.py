import tkinter as tk
import random

CANVAS_WIDTH, CANVAS_HEIGHT = 500, 500

root = tk.Tk()
root.title("Mon Dessin")

canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")


def dessine_cercle():
    x = random.randint(50, CANVAS_WIDTH - 50)
    y = random.randint(50, CANVAS_HEIGHT - 50)
    canvas.create_oval(x - 50, y - 50, x + 50, y + 50)

# Début du code

couleur = tk.Button(root, text="Choisir une couleur", bg="yellow", fg="blue",
                    font=("hervetica", "8"), pady=6, bd="6")
cercle = tk.Button(root, text="Cercle", command=dessine_cercle, bg="blue",
                   fg="white", font=("hervetica", "8"), padx=10, bd="4")
carre = tk.Button(root, text="Carré", bg="blue", fg="white",
                  font=("hervetica", "8"), padx=10, bd="4")
croix = tk.Button(root, text="Croix", bg="blue", fg="white",
                  font=("hervetica", "8"), padx=10, bd="4")

couleur.grid(column=1, row=0)
cercle.grid(column=0, row=1)
carre.grid(column=0, row=2)
croix.grid(column=0, row=3)

# Fin du code

canvas.grid(column=1, row=1, rowspan=3)
root.mainloop()

# Correction
'''import tkinter as tk
import random

couleur="red"

def choix_couleur():
    global couleur
    couleur=input()

def dessine_cercle():
    x = random.randint(0, CANVAS_WIDTH)
    y = random.randint(0, CANVAS_HEIGHT)
    canvas.create_oval(x - 50, y - 50, x + 50, y + 50, fill=couleur)

def dessine_carre():
    x = random.randint(0, CANVAS_WIDTH)
    y = random.randint(0, CANVAS_HEIGHT)
    canvas.create_rectangle(x - 50, y - 50, x + 50, y + 50, fill=couleur)

def dessine_croix():
    x = random.randint(0, CANVAS_WIDTH)
    y = random.randint(0, CANVAS_HEIGHT)
    canvas.create_line(x - 50, y - 50, x + 50, y + 50, fill=couleur)
    canvas.create_line(x - 50, y + 50, x + 50, y - 50, fill=couleur)


CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400
root = tk.Tk()
root.title("DESSIN")
canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = "black", relief=tk.GROOVE, bd=1)

def create_button(text, fonction, i, j):
    bouton = tk.Button(text=text, command = fonction, font = ("Helvetica", "30"), activeforeground="red", activebackground="black", padx=100)
    bouton.grid(column=i, row=j)
    return bouton

# Début de votre code
cercle = create_button("cercle", dessine_cercle, 0, 1)
carre = create_button("carre",   dessine_carre, 0, 2)
croix = create_button("croix",   dessine_croix, 0, 3)
choix = create_button("choisir une couleur",  choix_couleur, 1, 0)
# Fin de votre code

canvas.grid(column=1, row = 1, rowspan=3)
canvas.create_oval(150, 150, 250, 250)
root.mainloop()
'''