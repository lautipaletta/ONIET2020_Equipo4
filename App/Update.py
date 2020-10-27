from tkinter import *

root = Tk()
root.config(bg = "lightblue")
root.resizable(0,0)

frame = Frame(root)
frame.pack()

frame.config(bg = "lightblue")

# VARIABLES

nombreUsuario = StringVar()
apellidoUsuario = StringVar()
passwordUsuario = StringVar()
direccionUsuario = StringVar()
paisUsuario = StringVar()
emailUsuario = StringVar()

# TITULO
titulo = Label(frame, text="EDITAR USUARIO", font = ("Impact", 24))
titulo.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
titulo.config(bg = "lightblue")


# EMAIL
lbl_email = Label(frame, text="Email (No modificable): ")
lbl_email.grid(row=1, column=0, padx=10, pady=10, sticky = "e")
lbl_email.config(bg = "lightblue")

txt_email = Entry(frame, textvariable = emailUsuario)
txt_email.grid(row=1, column=1, padx=10, pady=10)

# NOMBRE
lbl_nombre = Label(frame, text="Nombre: ")
lbl_nombre.grid(row=2, column=0, padx=10, pady=10, sticky = "e")
lbl_nombre.config(bg = "lightblue")

txt_nombre = Entry(frame, textvariable = nombreUsuario)
txt_nombre.grid(row=2, column=1, padx=10, pady=10)

# APELLIDO
lbl_apellido = Label(frame, text="Apellido: ")
lbl_apellido.grid(row=3, column=0, padx=10, pady=10, sticky = "e")
lbl_apellido.config(bg = "lightblue")

txt_apellido = Entry(frame, textvariable = apellidoUsuario)
txt_apellido.grid(row=3, column=1, padx=10, pady=10)

# PASSWORD
lbl_password = Label(frame, text="Password: ")
lbl_password.grid(row=4, column=0, padx=10, pady=10, sticky = "e")
lbl_password.config(bg = "lightblue")

txt_password = Entry(frame, textvariable = passwordUsuario)
txt_password.grid(row=4, column=1, padx=10, pady=10)
txt_password.config(show="*")

# DIRECCION
lbl_direccion = Label(frame, text="Dirección: ")
lbl_direccion.grid(row=5, column=0, padx=10, pady=10, sticky = "e")
lbl_direccion.config(bg = "lightblue")

txt_direccion = Entry(frame, textvariable = direccionUsuario)
txt_direccion.grid(row=5, column=1, padx=10, pady=10)

# PAIS
lbl_pais = Label(frame, text="País: ")
lbl_pais.grid(row=6, column=0, padx=10, pady=10, sticky = "e")
lbl_pais.config(bg = "lightblue")

txt_pais = Entry(frame, textvariable = paisUsuario)
txt_pais.grid(row=6, column=1, padx=10, pady=10)

# BOTONES

frameBotones = Frame(root)
frameBotones.pack()
frameBotones.config(bg = "lightblue")

botonUpdate = Button(frameBotones, text="Update", command = lambda:())
botonUpdate.grid(row=0, column=1, padx=10, pady=10)

root.mainloop()