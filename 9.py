import tkinter as tk

def draw_scene(canvas):
    canvas.delete('all')

    canvas.create_rectangle(50, 150, 150, 250, fill='darkred')
    canvas.create_polygon(50, 150, 150, 150, 100, 100, fill='lightpink')

    canvas.create_oval(200, 50, 250, 100, fill='yellow')

    for i in range(0, 400, 10):
        canvas.create_arc(i, 250, i+10, 270, start=0, extent=180, fill='lime')

root = tk.Tk()

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

draw_scene(canvas)

root.mainloop()