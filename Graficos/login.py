from tkinter import *
import os

# Funciones

def login():
    #validacion:
        os.system("python Graficos/App.py")
    #else:
        #incorrecto

# TKINTER login

root = Tk()
root.title("LogIn")
root.resizable(0,0)

frame = Frame(root)
frame.pack()

frame.config(bg = "lightblue")
root.config(bg = "lightblue")

# Variables

emailUsuario = StringVar()
passwordUsuario = StringVar()

# LABELS

# ---- Email
lbl_email = Label(frame, text="Email:")
lbl_email.config(bg = "lightblue")
lbl_email.grid(row=0, column=0, padx=10, pady=10)

txt_email = Entry(frame, textvariable = emailUsuario)
txt_email.grid(row=0, column=1, padx=10, pady=10)

# ---- Password

lbl_password = Label(frame, text="Password:")
lbl_password.config(bg = "lightblue")
lbl_password.grid(row=1, column=0, padx=10, pady=10)

txt_password = Entry(frame, textvariable = passwordUsuario)
txt_password.grid(row=1, column=1, padx=10, pady=10)

# BOTONES


botonLogin = Button(frame, text="Iniciar Sesión", command = lambda:login())
botonLogin.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()