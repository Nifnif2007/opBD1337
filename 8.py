import tkinter as tk

def change_text_size(event=None):
    try:
        width = int(width_entry.get())
        height = int(height_entry.get())
        text.configure(width=width, height=height)
    except ValueError:
        pass

def on_focus_in(event):
    text.configure(bg="white")

def on_focus_out(event):
    text.configure(bg="lightgrey")

root = tk.Tk()
root.title("Многострочное текстовое поле")

width_label = tk.Label(root, text="Ширина:")
width_label.pack()

width_entry = tk.Entry(root)
width_entry.pack()
width_entry.bind("<Return>", change_text_size)

height_label = tk.Label(root, text="Высота:")
height_label.pack()

height_entry = tk.Entry(root)
height_entry.pack()
height_entry.bind("<Return>", change_text_size)

change_size_button = tk.Button(root, text="Изменить размер", command=change_text_size)
change_size_button.pack()

text = tk.Text(root, bg="lightgrey")
text.pack()
text.bind("<FocusIn>", on_focus_in)
text.bind("<FocusOut>", on_focus_out)

root.mainloop()