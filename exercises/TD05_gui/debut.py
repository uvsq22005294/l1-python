import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400

root = tk.Tk()

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

# Début de votre code
x0 = 100
x1 = CANVAS_WIDTH - 100
y = CANVAS_HEIGHT / 2
canvas.create_line(x0, y, x1, y)
canvas.create_oval(x0 - 50, y + 50, x0 + 50, y - 50)
canvas.create_oval(x1 - 50, y + 50, x1 + 50, y - 50)
canvas.create_oval((x0 + x1) / 2 - 50, y + 50, (x0 + x1) / 2 + 50, y - 50)

# Fin de votre code

canvas.grid(column=0, row=0)
root.mainloop()



import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 400, 600

root = tk.Tk()

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

# Début de votre code
x = CANVAS_WIDTH / 2
y0 = 100
y1 = CANVAS_HEIGHT - 100
canvas.create_line(x, y0, x, y1)
canvas.create_oval(x + 50, y0 - 50, x - 50, y0 + 50)
canvas.create_oval(x - 50, y1 + 50, x + 50, y1 - 50)
canvas.create_oval(x + 50, (y0 + y1) / 2 - 50, x - 50, (y0 + y1) / 2 + 50)

# Fin de votre code

canvas.grid(column=0, row=0)
root.mainloop()



import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400

root = tk.Tk()

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

# Début de votre code
x0 = 100
x1 = CANVAS_WIDTH - 100
y = CANVAS_HEIGHT / 2
x = CANVAS_WIDTH/2
y1 = 100
y2 = CANVAS_HEIGHT - 100

canvas.create_line(x, y1, x, y2)
canvas.create_oval(x - 50, y1 + 50, x + 50, y1 - 50)
canvas.create_oval(x - 50, y2 + 50, x + 50, y2 - 50)
canvas.create_oval((x0 + x1) / 2 - 50, y + 50, (x0 + x1) / 2 + 50, y - 50)

# Fin de votre code
canvas.grid(column=0, row=0)
root.mainloop()



#difference entre grid() et pack()
#dans les exemples précédent, on trouve grid(). On trouve pack() dans exemple 3 de gui
import tkinter as tk
CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400
root = tk.Tk()
a = tk.Button(text="a", width=10, height=10)
b = tk.Button(text="b", width=10, height=10)
c = tk.Button(text="c", width=10, height=10)
a.grid(column = 1, row = 0)
b.grid(column = 0, row = 0)
c.grid(column = 2, row = 1)
root.mainloop()


import tkinter as tk
CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400
root = tk.Tk()
a = tk.Button(text="a", width=10, height=10)
b = tk.Button(text="b", width=10, height=10)
c = tk.Button(text="c", width=10, height=10)
a.pack()
b.pack()
c.pack()
root.mainloop()