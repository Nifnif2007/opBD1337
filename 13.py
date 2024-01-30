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
    if messagebox.askokcancel("Подтверждение", "Вы уверены, что хотите очистить текст?"):
        text.delete(1.0, END)


root = Tk()
text = Text(width=50, height=25)
text.grid(columnspan=2)
b1 = Button(text="Открыть", command=insert_text)
b1.grid(row=1, sticky=E)
b2 = Button(text="Сохранить", command=extract_text)
b2.grid(row=1, column=1, sticky=W)
b3 = Button(text="Очистить", command=clear_text)
b3.grid(row=2, column=0, columnspan=2, sticky="we")

root.mainloop()