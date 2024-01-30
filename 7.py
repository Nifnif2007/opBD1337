import tkinter as tk
def add_to_list(event):
    text = entry.get()
    if text:
        listbox.insert(tk.END, text)
        entry.delete(0, tk.END)
def copy_from_list(event):
    selected_item = listbox.get(listbox.curselection())
    entry.delete(0, tk.END)
    entry.insert(tk.END, selected_item)
root = tk.Tk()
root.title("Текстовое поле и список")
entry = tk.Entry(root)
entry.pack()
entry.bind("<Return>", add_to_list)
listbox = tk.Listbox(root)
listbox.pack()
listbox.bind("<Double-Button-1>", copy_from_list)
root.mainloop()
