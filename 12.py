import tkinter as tk

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(self.master, width=400, height=400)
        self.canvas.pack()
        self.button = tk.Button(self.master, text="Добавить фигуру", command=self.open_figure_window)
        self.button.pack()

    def open_figure_window(self):
        self.figure_window = tk.Toplevel(self.master)
        FigureWindow(self.figure_window, self)

    def draw_figure(self, x1, y1, x2, y2, figure_type):
        if figure_type == "rectangle":
            self.canvas.create_rectangle(x1, y1, x2, y2)
        elif figure_type == "oval":
            self.canvas.create_oval(x1, y1, x2, y2)

class FigureWindow:
    def __init__(self, master, main_window):
        self.master = master
        self.main_window = main_window
        self.figure_type = tk.StringVar()
        self.x1_label = tk.Label(self.master, text="x1")
        self.y1_label = tk.Label(self.master, text="y1")
        self.x2_label = tk.Label(self.master, text="x2")
        self.y2_label = tk.Label(self.master, text="y2")
        self.x1_entry = tk.Entry(self.master)
        self.y1_entry = tk.Entry(self.master)
        self.x2_entry = tk.Entry(self.master)
        self.y2_entry = tk.Entry(self.master)
        self.rectangle_radio = tk.Radiobutton(self.master, text="Прямоугольник", variable=self.figure_type, value="rectangle")
        self.oval_radio = tk.Radiobutton(self.master, text="Овал", variable=self.figure_type, value="oval")
        self.draw_button = tk.Button(self.master, text="Нарисовать", command=self.draw)
        self.x1_entry.grid(row=0, column=1)
        self.y1_entry.grid(row=1, column=1)
        self.x2_entry.grid(row=2, column=1)
        self.y2_entry.grid(row=3, column=1)
        self.x1_label.grid(row=0, column=0)
        self.y1_label.grid(row=1, column=0)
        self.x2_label.grid(row=2, column=0)
        self.y2_label.grid(row=3, column=0)
        self.rectangle_radio.grid(row=4, column=0)
        self.oval_radio.grid(row=4, column=1)
        self.draw_button.grid(row=5, column=0, columnspan=2)
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_rowconfigure(2, weight=1)
        self.master.grid_rowconfigure(3, weight=1)
        self.master.grid_rowconfigure(4, weight=1)
        self.master.grid_rowconfigure(5, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)

    def draw(self):
        x1 = int(self.x1_entry.get())
        y1 = int(self.y1_entry.get())
        x2 = int(self.x2_entry.get())
        y2 = int(self.y2_entry.get())
        figure_type = self.figure_type.get()
        self.main_window.draw_figure(x1, y1, x2, y2, figure_type)
        self.master.destroy()

root = tk.Tk()
app = MainWindow(root)
root.mainloop()