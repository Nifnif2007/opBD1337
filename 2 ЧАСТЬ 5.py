from tkinter import *

root = Tk()
root.title("Менеджер контактов")
def add_contact():
    name = name_entry.get()
    surname = surname_entry.get()
    phone = phone_entry.get()
    contact = f"Имя: {name}, Фамилия: {surname}, Телефон: {phone}"
    contacts_list.insert(END, contact)

def edit_contact():
    selected_index = contacts_list.curselection()
    if selected_index:
        selected_contact = contacts_list.get(selected_index)
        contact_info = selected_contact.split(",")
        name = contact_info[0].split(":")[1].strip()
        surname = contact_info[1].split(":")[1].strip()
        phone = contact_info[2].split(":")[1].strip()
        
        name_entry.delete(0, END)
        name_entry.insert(0, name)
        surname_entry.delete(0, END)
        surname_entry.insert(0, surname)
        phone_entry.delete(0, END)
        phone_entry.insert(0, phone)

        contacts_list.delete(selected_index)

def delete_contact():
    selected_index = contacts_list.curselection()
    if selected_index:
        contacts_list.delete(selected_index)

name_label = Label(root, text="Имя:")
name_label.grid(row=0, column=0)
name_entry = Entry(root)
name_entry.grid(row=0, column=1)

surname_label = Label(root, text="Фамилия:")
surname_label.grid(row=1, column=0)
surname_entry = Entry(root)
surname_entry.grid(row=1, column=1)

phone_label = Label(root, text="Телефон:")
phone_label.grid(row=2, column=0)
phone_entry = Entry(root)
phone_entry.grid(row=2, column=1)

add_button = Button(root, text="Добавить", command=add_contact)
add_button.grid(row=3, column=0)

edit_button = Button(root, text="Редактировать", command=edit_contact)
edit_button.grid(row=3, column=1)

delete_button = Button(root, text="Удалить", command=delete_contact)
delete_button.grid(row=3, column=2)

contacts_list = Listbox(root)
contacts_list.grid(row=4, columnspan=3)

root.mainloop()