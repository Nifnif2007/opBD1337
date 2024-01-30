import tkinter as tk
def add_to_shopping_list():
    selected_items = products_listbox.curselection()
    for index in selected_items:
        item = products_listbox.get(index)
        shopping_listbox.insert(tk.END, item)
def remove_from_shopping_list():
    selected_items = shopping_listbox.curselection()
    for index in selected_items:
        shopping_listbox.delete(index)
root = tk.Tk()
root.title("Listbox")
products = ["Яблоко", "Банан", "Груша", "Апельсин", "Мандарин", "Ананас"]
products_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
for product in products:
    products_listbox.insert(tk.END, product)
products_listbox.pack(side=tk.LEFT)
shopping_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
shopping_listbox.pack(side=tk.RIGHT)
add_button = tk.Button(root, text=">>>", command=add_to_shopping_list)
add_button.pack()
remove_button = tk.Button(root, text="<<<", command=remove_from_shopping_list)
remove_button.pack()
root.mainloop()