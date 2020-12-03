import tkinter as tk


def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


CANVAS_WIDTH, CANVAS_HEIGHT = 256, 256

root = tk.Tk()
root.title("tk")

canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")


def draw_pixel(i, j, color):
    if((0 <= i <= CANVAS_WIDTH) and (0 <= j <= CANVAS_HEIGHT)):
        canvas.create_oval(i, j, i, j, fill=color)
    else:
        print("Error")


def ecran_aleatoire():
    for a in range(0, CANVAS_WIDTH + 1):
        for b in range(0, CANVAS_HEIGHT + 1):
            draw_pixel(a, b, "yellow")


# Début du code

aleatoire = tk.Button(root, text="Aléatoire", command=ecran_aleatoire,
                      fg="blue", font=("14"))
degrade_gris = tk.Button(root, text="Dégradé gris", fg="blue", font=("14"))
degrade_2d = tk.Button(root, text="Dégradé 2D", fg="blue", font=("14"))

aleatoire.grid(column=0, row=0)
degrade_gris.grid(column=0, row=1)
degrade_2d.grid(column=0, row=2)

# Fin du code

canvas.grid(column=1, row=0, rowspan=3)
root.mainloop()
