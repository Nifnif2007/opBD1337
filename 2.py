import tkinter as tk


def insert_red():
    text = '#ff0000'
    entr1.delete(0, tk.END)
    entr1.insert(0, text)
    lb.config(text='красный')


def insert_orange():
    text = '#ff7d00'
    entr1.delete(0, tk.END)
    entr1.insert(0, text)
    lb.config(text='оранжевый')


def insert_yellow():
    text = '#ffff00'
    entr1.delete(0, tk.END)
    entr1.insert(0, text)
    lb.config(text='жёлтый')


def insert_green():
    text = '#00ff00'
    entr1.delete(0, tk.END)
    entr1.insert(0, text)
    lb.config(text='зелёный')


def insert_lblue():
    text = '#007dff'
    entr1.delete(0, tk.END)
    entr1.insert(0, text)
    lb.config(text='голубой')


def insert_blue():
    text = '#0000ff'
    entr1.delete(0, tk.END)
    entr1.insert(0, text)
    lb.config(text='синий')


def insert_purple():
    text = '#7d00ff'
    entr1.delete(0, tk.END)
    entr1.insert(0, text)
    lb.config(text='фиолетовый')


root = tk.Tk()
lb = tk.Label(text='Пусто')
entr1 = tk.Entry(width=50, text='Пусто')
but_r = tk.Button(bg='#ff0000', command=insert_red, width=50)
but_o = tk.Button(bg='#ff7d00', command=insert_orange, width=50)
but_y = tk.Button(bg='#ffff00', command=insert_yellow, width=50)
but_g = tk.Button(bg='#00ff00', command=insert_green, width=50)
but_l = tk.Button(bg='#007dff', command=insert_lblue, width=50)
but_b = tk.Button(bg='#0000ff', command=insert_blue, width=50)
but_p = tk.Button(bg='#7d00ff', command=insert_purple, width=50)
lb.pack()
entr1.pack()
but_r.pack()
but_o.pack()
but_y.pack()
but_g.pack()
but_l.pack()
but_b.pack()
but_p.pack()


root.mainloop()