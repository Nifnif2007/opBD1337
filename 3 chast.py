import tkinter as tk
from tkinter import messagebox
import threading
from tkcustom import CustomTkinter

def login():
    login_window = CustomTkinter(top_level=True)
    login_window.geometry('300x150')
    login_window.title('Login')

    login_label = tk.Label(login_window, text='Username:')
    login_label.pack()

    login_entry = tk.Entry(login_window)
    login_entry.pack()

    password_label = tk.Label(login_window, text='Password:')
    password_label.pack()

    password_entry = tk.Entry(login_window, show='*')
    password_entry.pack()

    def check_credentials():
        username = login_entry.get()
        password = password_entry.get()
        if username == 'admin' and password == 'password':
            login_window.destroy()
            start_timer()
        else:
            messagebox.showwarning('Login', 'Invalid username or password. Please try again.')

    login_button = tk.Button(login_window, text='Login', command=check_credentials)
    login_button.pack()

    login_window.mainloop()

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

root = CustomTkinter()
root.title('Timer')

minutes_label = tk.Label(root, text='Minutes:')
minutes_label.pack()

minutes_entry = tk.Entry(root)
minutes_entry.pack()

seconds_label = tk.Label(root, text='Seconds:')
seconds_label.pack()

seconds_entry = tk.Entry(root)
seconds_entry.pack()

start_button = tk.Button(root, text='Start', command=start_timer)
start_button.pack()

stop_button = tk.Button(root, text='Stop', command=stop_timer)
stop_button.pack()

timer_label = tk.Label(root, text='00:00', font=('Arial', 24), pady=20)
timer_label.pack()

login()

root.mainloop()