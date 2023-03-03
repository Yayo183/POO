from tkinter import *
from tkinter import ttk as ttk
from Usuario import Usuario
from tkinter import messagebox as Messagebox

root = Tk()

nombreUsuario = StringVar()
ContraUsuario = StringVar()
usuarios = []

def creatGUI():

    #Ventana Principal
    #root = Tk()
    root.title("Login Usuario")

    #mainFrame
    mainFrame = Frame(root)
    mainFrame.pack()
    mainFrame.config(width=480,height=320,bg="lightblue")

    titulo = Label(mainFrame,text="Login de Usuario",font=("Arial",22))
    titulo.grid(column=0,row=0,padx=10,pady=10,columnspan=2)

    nombreLabel = Label(mainFrame,text="Correo: ")
    nombreLabel.grid(column=0,row=1)
    PassLabel = Label(mainFrame,text="Password: ")
    PassLabel.grid(column=0,row=2)

    #Entradas de texto
    
    #nombreUsuario = StringVar()
    nombreUsuario.set("")
    nombreEntry = Entry(mainFrame,textvariable=nombreUsuario)
    nombreEntry.grid(column=1,row=1)

    #PasswordUsuario = StringVar()
    ContraUsuario.set("")
    ContraEntry = Entry(mainFrame,textvariable=ContraUsuario,show="*")
    ContraEntry.grid(column=1,row=2)

    #Botones
    startSeccionButton = ttk.Button(mainFrame,text="sign in",command=SignIn)
    startSeccionButton.grid(column=1,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    checkInButton = ttk.Button(mainFrame,text="Check in",command=CheckIn)
    checkInButton.grid(column=0,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    root.mainloop()

def SignIn():
    for user in usuarios:
        if user.Correo == nombreUsuario.get():
            nombre = user.Correo
            test = user.conectar(ContraUsuario.get())
            if test:
                Messagebox.showinfo(f"Conectado",f"Has iniciado seccion en [{nombre}] con exito")
            else:
                Messagebox.showerror("Error","fallo exitoso intentalo de nuevo")
            break
    else:
        Messagebox.showerror("Error","No existen Usuarios con ese Nombre")

def CheckIn():
    name = nombreUsuario.get()
    passwd = ContraUsuario.get()   
    newUser = Usuario (name,passwd)
    usuarios.append(newUser)
    Messagebox.showinfo("Registro",f"Se ha registrado [{name}] correctamente, bien hecho")
    nombreUsuario.set("")
    ContraUsuario.set("")

if __name__ == "__main__":
    #user1 = Usuario(input("Ingrese un Correo: "),input("Ingrese un Password: "))
    user1 = Usuario("lucas","1234")
    usuarios.append(user1)
    creatGUI()
