import tkinter as tk
import random


def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


CANVAS_WIDTH, CANVAS_HEIGHT = 256, 256

root = tk.Tk()
root.title("Couleurs")

canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")


def draw_pixel(i, j, color):
    if ((0 <= i <= CANVAS_WIDTH) and (0 <= j <= CANVAS_HEIGHT)):
        canvas.create_oval(i, j, i, j, fill=color)
    else:
        print("Error")


def ecran_aleatoire():
    for i in range(0, CANVAS_WIDTH * CANVAS_HEIGHT):
        x = random.randint(0, 256)
        y = random.randint(0, 256)
        color = get_color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        draw_pixel(x, y, color)


def degrade_gris():
    '''for i in range(10, 240):
        if (10 <= i <= 240):
            color = get_color(i, i, i)
            draw_pixel(i, i, color)'''
    for i in range(0, 257, 2):
        for j in range(0, 257):
            color = get_color(i, i, i)
            draw_pixel(i, j, color)
    '''for i in range(0, 256):
        color = get_color(i, i, i)
        liste = []
        liste.append(i)
        print(liste)
        draw_pixel(i, i, color)'''


def degrade_2D():
    for i in range(0, 256, 1):
        for j in range(0, 256):
            color = get_color(i, i, i)
            draw_pixel(j, i, color)


# Début du code

aletatoire = tk.Button(root, text="Aléatoire", command=ecran_aleatoire, bg="white", fg="blue", font="14")
degrade_gris = tk.Button(root, text="Dégradé gris", command=degrade_gris, bg="white", fg="blue", font="14")
degrade_2D = tk.Button(root, text="Dégradé 2D", command=degrade_2D, bg="white", fg="blue", font="14")

aletatoire.grid(row=0, column=0)
degrade_gris.grid(row=1, column=0)
degrade_2D.grid(row=2, column=0)

# Fin du code

canvas.grid(row=0, column=1, rowspan=3)
root.mainloop()
