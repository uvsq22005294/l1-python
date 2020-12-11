import tkinter as tk
import random as rd

WIDTH = 700
HEIGHT = 600
rayon = 20
balle = []
dx = []
dy = []
id_after = None


def touche_haut_bas(balle):
    """Retourner True si la balle touche le haut ou le bas du canvas et False sinon """
    coord = canvas.coords(balle)
    # coord est une liste de la forme (x1, y1, x2, y2)
    y_haut = coord[1]
    y_bas = coord[3]
    if (y_haut <= 0 or y_bas >= HEIGHT):
        return True
    return False


def touche_gauche_droite(balle):
    """Retourner True si la balle touche à gauche ou à droite du canvas et False sinon """
    coord = canvas.coords(balle)
    # coord est une liste de la forme (x1, y1, x2, y2)
    x_gauche = coord[0]
    x_droite = coord[2]
    if (x_gauche <= 0 or x_droite >= WIDTH):
        return True
    return False


def start():
    """ Démarre le mouvement des balles """
    global dx, dy
    global id_after
    if (balle == []):
        return
    for i in range(len(balle)):
        if touche_haut_bas(balle[i]):
            dy[i] = -dy[i]
        if touche_gauche_droite(balle[i]):
            dx[i] = -dx[i]
        canvas.move(balle[i], dx[i], dy[i])
    id_after = canvas.after(20, start)


def stop():
    """ Arrête le mouvement des balles """
    if (id_after is None):
        return
    canvas.after_cancel(id_after)


def ajout_balle(event):
    """ Dessine un cercle à l'endroit où l'on a cliqué """
    global balle, dx, dy
    x = event.x
    y = event.y
    col = "blue"
    new_balle = canvas.create_oval((x - rayon, y - rayon), (x + rayon, y + rayon), fill=col, outline=col)
    balle.append(new_balle)
    dep_x = rd.randint(-5, 5)
    dep_y = rd.randint(-5, 5)
    dx.append(dep_x)
    dy.append(dep_y)


racine = tk.Tk()
racine.title("Jeu de balle")
canvas = tk.Canvas(racine, width=WIDTH, height=HEIGHT, bg="black")
bouton_start = tk.Button(racine, text="Start", command=start)
bouton_stop = tk.Button(racine, text="Stop", command=stop)

canvas.grid(column=0, row=0, columnspan=2)
bouton_start.grid(column=0, row=1)
bouton_stop.grid(column=1, row=1)
canvas.bind("<Button-1>", ajout_balle)


racine.mainloop()
