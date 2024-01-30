import tkinter as tk
from tkinter import messagebox
import threading

def start_timer():
    global remaining_time, timer_label
    minutes = int(minutes_entry.get())
    seconds = int(seconds_entry.get())
    total_seconds = minutes * 60 + seconds
    remaining_time = total_seconds

    def countdown():
        global remaining_time
        if remaining_time > 0:
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            timer_label.configure(text=f'{minutes:02d}:{seconds:02d}')
            remaining_time -= 1
            timer_label.after(1000, countdown)
        else:
            messagebox.showinfo('Timer', 'Timer finished!')

    countdown()

def stop_timer():
    global remaining_time, timer_label
    remaining_time = 0
    timer_label.configure(text='00:00')

root = tk.Tk()
root.title('Timer')

minutes_label = tk.Label(root, text='Минуты:')
minutes_label.pack()

minutes_entry = tk.Entry(root)
minutes_entry.pack()

seconds_label = tk.Label(root, text='Секунды:')
seconds_label.pack()

seconds_entry = tk.Entry(root)
seconds_entry.pack()

start_button = tk.Button(root, text='Старт', command=start_timer)
start_button.pack()

stop_button = tk.Button(root, text='Стоп', command=stop_timer)
stop_button.pack()

timer_label = tk.Label(root, text='00:00', font=('Arial', 24), pady=20)
timer_label.pack()

root.mainloop()