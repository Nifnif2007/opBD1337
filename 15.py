import tkinter as tk
from tkinter import PhotoImage
import random

def move_button():
    window_width = root.winfo_width()
    window_height = root.winfo_height()

    new_x = random.randint(0, window_width - button.winfo_width())
    new_y = random.randint(0, window_height - button.winfo_height())

    button.place(x=new_x, y=new_y)

root = tk.Tk()

img = PhotoImage(file='smile.png')

button = tk.Button(root, image=img, command=move_button)
button.place(x=0, y=0)

root.mainloop()