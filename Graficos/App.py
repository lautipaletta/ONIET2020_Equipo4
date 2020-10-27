from tkinter import *
from tkinter import messagebox
import os

root = Tk()
root.config(bg = "lightblue")
root.resizable(0,0)

frame = Frame(root)
frame.config(bg = "lightblue")
frame.pack()

# MENU

barraMenu = Menu(root)
root.config(menu = barraMenu)

EditarUsuario = Menu(barraMenu, tearoff = 0)
EditarUsuario.add_command(label = "Editar información de Usuario", command = lambda:abrirEditor())

barraMenu.add_cascade(label = "Editar", menu = EditarUsuario)

AboutUs = Menu(barraMenu, tearoff = 0)
AboutUs.add_command(label = "Información", command = lambda:aboutUs())

barraMenu.add_cascade(label = "About Us", menu = AboutUs)

# FUNCIONES PROGRAMA
def aboutUs():
    messagebox.showinfo("Información","Somos tres estudiantes de la EEST N°7 Quilmes 'IMPA'\n-Casareski Juan\n-Paletta Lautaro\n-Torres Santiago")

def abrirEditor():
    os.system("python Graficos/Update.py")

def limpiar():
    nombreUsuario.set("")
    apellidoUsuario.set("")
    paisUsuario.set("")
    nuevosContagios.set("")
    nuevosDecesos.set("")
    contagiados.set("")
    activos.set("")
    recuperados.set("")
    decesos.set("")

# VARIABLES

nombreUsuario = StringVar()
apellidoUsuario = StringVar()
paisUsuario = StringVar()
ultAct = StringVar()
    
titulo = Label(frame, text = "API COVID19", font = ("Impact", 24))
titulo.config(bg = "lightblue")
titulo.grid(row=0, column=0, padx=10, pady=20, columnspan = 2)

# NOMBRE
lbl_nombre = Label(frame, text="Nombre: ")
lbl_nombre.grid(row=1, column=0, padx=10, pady=5, sticky = "e")
lbl_nombre.config(bg = "lightblue")

txt_nombre = Entry(frame, textvariable = nombreUsuario)
txt_nombre.grid(row=1, column=1, padx=10, pady=5)

# APELLIDO
lbl_apellido = Label(frame, text="Apellido: ")
lbl_apellido.grid(row=2, column=0, padx=10, pady=5, sticky = "e")
lbl_apellido.config(bg = "lightblue")

txt_apellido = Entry(frame, textvariable = apellidoUsuario)
txt_apellido.grid(row=2, column=1, padx=10, pady=5)

# PAIS
lbl_pais = Label(frame, text="País: ")
lbl_pais.grid(row=3, column=0, padx=10, pady=5, sticky = "e")
lbl_pais.config(bg = "lightblue")

txt_pais = Entry(frame, textvariable = paisUsuario)
txt_pais.grid(row=3, column=1, padx=10, pady=5)

# ULT ACT
lbl_ult = Label(frame, text="Ult. Actualización del país: ")
lbl_ult.grid(row=4, column=0, padx=10, pady=5, sticky = "e")
lbl_ult.config(bg = "lightblue")

txt_ult = Entry(frame, textvariable = ultAct)
txt_ult.grid(row=4, column=1, padx=10, pady=5)

# DATOS PAIS

# VARIABLES
nuevosContagios = StringVar()
nuevosDecesos = StringVar()
contagiados = StringVar()
activos = StringVar()
recuperados = StringVar()
decesos = IntVar()

frameDatos = Frame(root)
frameDatos.pack()
frameDatos.config(bg = "lightblue", bd = 10, relief = "groove", pady = 10, padx = 10)

# NUEVOS CASOS
lbl_nombre = Label(frameDatos, text="Nuevos casos: ")
lbl_nombre.grid(row=1, column=0, padx=10, pady=5, sticky = "e")
lbl_nombre.config(bg = "lightblue")

txt_nombre = Entry(frameDatos, textvariable = nuevosContagios)
txt_nombre.grid(row=1, column=1, padx=10, pady=5)

# NUEVOS CASOS
lbl_nombre = Label(frameDatos, text="Nuevos decesos: ")
lbl_nombre.grid(row=2, column=0, padx=10, pady=5, sticky = "e")
lbl_nombre.config(bg = "lightblue")

txt_nombre = Entry(frameDatos, textvariable = nuevosDecesos)
txt_nombre.grid(row=2, column=1, padx=10, pady=5)

# TOTAL:
lbl_nombre = Label(frameDatos, text="Total: ")
lbl_nombre.grid(row=3, column=0, padx=10, pady=5, sticky = "e")
lbl_nombre.config(bg = "lightblue")

# CONTAGIADOS
lbl_nombre = Label(frameDatos, text="    CONTAGIADOS: ")
lbl_nombre.grid(row=4, column=0, padx=10, pady=5, sticky = "e")
lbl_nombre.config(bg = "lightblue")

txt_nombre = Entry(frameDatos, textvariable = contagiados)
txt_nombre.grid(row=4, column=1, padx=10, pady=5)

# ACTIVOS
lbl_nombre = Label(frameDatos, text="    ACTIVOS: ")
lbl_nombre.grid(row=5, column=0, padx=10, pady=5, sticky = "e")
lbl_nombre.config(bg = "lightblue")

txt_nombre = Entry(frameDatos, textvariable = activos)
txt_nombre.grid(row=5, column=1, padx=10, pady=5)

# RECUPERADOS
lbl_nombre = Label(frameDatos, text="    RECUPERADOS: ")
lbl_nombre.grid(row=6, column=0, padx=10, pady=5, sticky = "e")
lbl_nombre.config(bg = "lightblue")

txt_nombre = Entry(frameDatos, textvariable = recuperados)
txt_nombre.grid(row=6, column=1, padx=10, pady=5)

# DECESOS
lbl_nombre = Label(frameDatos, text="    DECESOS: ")
lbl_nombre.grid(row=7, column=0, padx=10, pady=5, sticky = "e")
lbl_nombre.config(bg = "lightblue")

txt_nombre = Entry(frameDatos, textvariable = decesos)
txt_nombre.grid(row=7, column=1, padx=10, pady=5)


limpiar()
root.mainloop()
