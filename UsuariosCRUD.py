from tkinter import *
from tkinter import ttk
import tkinter as tk

Ventana = Tk()
Ventana.title("CRUD USUARIOS")
Ventana.geometry("500x300")

panel = ttk.Notebook(Ventana)
panel.pack(fill="both", expand="yes")

pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)

#USUARIOS
titulo = Label(pestana1,text="Registros Usuarios", fg="Blue",font=("Modetn",18)).pack()

varNom = tk.StringVar()
lblNom = Label(pestana1, text="Nombre: ").pack()
txtNom = Entry(pestana1,textvariable=varNom).pack()

varCor = tk.StringVar()
lblCor = Label(pestana1, text="Correo: ").pack()
txtCor = Entry(pestana1,textvariable=varCor).pack()

varCon = tk.StringVar()
lblCon = Label(pestana1, text="Contrasena: ").pack()
txtCon = Entry(pestana1,textvariable=varCon).pack()

btnGuardar = Button(pestana1,text="Guardar Usuario").pack()



panel.add(pestana1,text="Formulario de Usuarios")
panel.add(pestana2,text="Buscar Usuario")
panel.add(pestana3,text="Consultar Usuarios")
panel.add(pestana4,text="Actualizar Usuario")

Ventana.mainloop()
