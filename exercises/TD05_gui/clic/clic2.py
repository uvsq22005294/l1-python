import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 500, 500

root = tk.Tk()
root.title("Clic")

canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="black")


def draw_cercle(event):
    if (event.x > CANVAS_WIDTH / 2):
        canvas.create_oval((event.x - 50, event.y - 50), (event.x + 50, event.y + 50), fill="red")
    elif (event.x < CANVAS_WIDTH / 2):
        canvas.create_oval((event.x - 50, event.y - 50), (event.x + 50, event.y + 50), fill="blue")


canvas.create_line(CANVAS_WIDTH / 2, 0, CANVAS_WIDTH / 2, CANVAS_HEIGHT, fill="white")
canvas.bind("<Button-1>", draw_cercle)
canvas.grid()
root.mainloop()
