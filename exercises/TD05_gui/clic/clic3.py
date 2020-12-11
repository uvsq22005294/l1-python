import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 500, 500

root = tk.Tk()
root.title("Clic")

canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="black")

nombre_clic = 0
point = (0, 0)


def draw_line(event):
    global nombre_clic, point
    if (nombre_clic == 0):
        nombre_clic == 1
        point = (event.x, event.y)
    else:
        nombre_clic = 0
        if (CANVAS_WIDTH / 2 - event.x)


canvas.create_line(CANVAS_WIDTH / 2, 0, CANVAS_WIDTH / 2, CANVAS_HEIGHT, fill="white")
canvas.bind("<Button-1>", draw_line)
canvas.grid()
root.mainloop()
