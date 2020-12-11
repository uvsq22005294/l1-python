import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 500, 500

root = tk.Tk()
root.title("Clic")

canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="black")


def draw_pixel(event):
    canvas.create_oval((event.x, event.y), (event.x + 1, event.y), fill="red")


canvas.bind("<Button-1>", draw_pixel)
canvas.grid()
root.mainloop()
