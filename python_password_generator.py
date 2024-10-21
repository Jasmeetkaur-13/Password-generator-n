import random
from tkinter import messagebox
from tkinter import *

def generate_password():
    try:
        length = int(length_entry.get())
        repeat = int(repeat_entry.get())
        
        if length <= 0:
            messagebox.showerror("Input Error", "Password length must be greater than 0.")
            return
        if repeat not in [1, 2]:
            messagebox.showerror("Input Error", "Repetition must be 1 (no repetition) or 2 (repetition allowed).")
            return

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for length and repetition.")
        return

    if repeat == 1:
        password = ''.join(random.sample(character_string, length))
    else:
        password = ''.join(random.choices(character_string, k=length))

    password_v.set("Created password: " + password)

# Character set for password generation
character_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

# Setting up the GUI
password_gen = Tk()
password_gen.geometry("400x250")
password_gen.title("Password Generator")

title_label = Label(password_gen, text="PASSWORD GENERATOR", font=('Ubuntu Mono', 17, 'bold'))
title_label.pack(pady=10)

length_label = Label(password_gen, text="Enter password length:")
length_label.place(x=30, y=60)
length_entry = Entry(password_gen, width=7)
length_entry.place(x=250, y=50)

repeat_label = Label(password_gen, text="Repetition? /n 1: Yes, 2: No:")
repeat_label.place(x=20, y=90)
repeat_entry = Entry(password_gen, width=5)
repeat_entry.place(x=250, y=90)

password_button = Button(password_gen, text="Generate Password", command=generate_password)
password_button.place(x=140, y=130)

password_v = StringVar()
password_label = Entry(password_gen, bd=0, bg="gray85", textvariable=password_v, state="readonly", font=('Ubuntu Mono', 12))
password_label.place(x=20, y=170, height=70, width=400)

password_gen.mainloop()
