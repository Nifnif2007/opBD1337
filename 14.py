from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox


def insert_text():
    try:
        file_name = fd.askopenfilename()
        f = open(file_name)
        s = f.read()
        text.insert(1.0, s)
        f.close()
    except:
        messagebox.showinfo("Ошибка", "Файл не загружен")


def extract_text():
    try:
        file_name = fd.asksaveasfilename(
            filetypes=(("TXT files", "*.txt"),
                       ("HTML files", "*.html;*.htm"),
                       ("All files", "*.*")))
        f = open(file_name, 'w')
        s = text.get(1.0, END)
        f.write(s)
        f.close()
    except:
        messagebox.showinfo("Ошибка", "Файл не сохранен")


def clear_text():
    if messagebox.askokcancel("Подтверждение", "Вы уверены, что хотите очиститься перед богом?"):
        text.delete(1.0, END)


root = Tk()
text = Text(width=50, height=25)
text.grid(columnspan=2)

menu = Menu(root)
root.config(menu=menu)

file_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Открыть", command=insert_text)
file_menu.add_command(label="Сохранить", command=extract_text)

context_menu = Menu(text, tearoff=0)
context_menu.add_command(label="Очистить", command=clear_text)

text.bind("<Button-3>", lambda event: context_menu.post(event.x_root, event.y_root))

root.mainloop()