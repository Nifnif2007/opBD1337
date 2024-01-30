import tkinter as tk

def show_selected():
    selected_value = var.get()
    if selected_value == 1:
        label.config(text="Вы выбрали 'a'")
    elif selected_value == 2:
        label.config(text="Вы выбрали 'b'")
    elif selected_value == 3:
        label.config(text="Вы выбрали 'c' ")

root = tk.Tk()
root.title("Прога")

var = tk.IntVar()
var.set(1)

label = tk.Label(root, text="")
label.pack(side='right')

radio_button1 = tk.Radiobutton(root, text="Вариант 1", variable=var, value=1, indicatoron=0, command=show_selected)
radio_button1.pack()

radio_button2 = tk.Radiobutton(root, text="Вариант 2", variable=var, value=2, indicatoron=0, command=show_selected)
radio_button2.pack()

radio_button3 = tk.Radiobutton(root, text="Вариант 3", variable=var, value=3, indicatoron=0, command=show_selected)
radio_button3.pack()



root.mainloop()