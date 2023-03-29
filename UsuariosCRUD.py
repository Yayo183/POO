from tkinter import *
from tkinter import ttk
import tkinter as tk
from ControladorBD import * #Te presentamos la clase a la ventana
from tkinter import messagebox

#Crear una objeto de tipo controlador
controlador = controladorBD()

#Proceder a guardar usando el metodo del objeto controlador
def ejecutaInsert():
    controlador.guardarUsuario(varNom.get(),varCor.get(),varCon.get())


#Funcion para buscar un usuario
def ejecutaSelectU():
    rsUsuario = controlador.consultaUsuario(varBus.get())
    
    for usu in rsUsuario:
        cadena = str(usu[0]) + " " + usu[1] + " " + usu[2] + str(usu[3])
    
    if(rsUsuario):
        print(cadena)
    else:
        messagebox.showinfo("No se encontro","Ningun usuario con este registro en BD")


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

btnGuardar = Button(pestana1,text="Guardar Usuario", command=ejecutaInsert).pack()



#Pestaña 2: buscar usuario
titulo2 = Label(pestana1,text="Buscar Usuario", fg="green",font=("Modetn",18)).pack()

varBus = tk.StringVar()
lblid = Label(pestana2, text="identificador de usuario: ").pack()
txtid = Entry(pestana2, textvariable=varBus).pack()

btnBuscar = Button (pestana2,text="Buscar",command=ejecutaSelectU).pack() 

subBus = Label(pestana2, text="Registrado: ",fg="blue",font=("Modern",15)).pack()
textBus = tk.Text(pestana2,height=5,width=52).pack()

 

panel.add(pestana1,text="Formulario de Usuarios")
panel.add(pestana2,text="Buscar Usuario")
panel.add(pestana3,text="Consultar Usuarios")
panel.add(pestana4,text="Actualizar Usuario")

Ventana.mainloop()
