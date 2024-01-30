import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename()
    with open(file_path, 'r') as file:
        text_field.delete('1.0', tk.END)
        text_field.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename()
    with open(file_path, 'w') as file:
        file.write(text_field.get('1.0', tk.END))

root = tk.Tk()

entry_field = tk.Entry(root)
entry_field.pack()

text_field = tk.Text(root)
text_field.pack()

open_button = tk.Button(root, text='Открыть', command=open_file)
open_button.pack()

save_button = tk.Button(root, text='Сохранить', command=save_file)
save_button.pack()

root.mainloop()