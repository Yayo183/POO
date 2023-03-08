from tkinter import *
from Password import *
import tkinter as tk
from tkinter import messagebox

axc = Password()

def Presionar():
    text = Password.generadorPassword()
    messagebox.showinfo("Mostrar", F"password gen: {text}")

ventana = Tk()
ventana.title("Generador de password")
ventana.geometry("300x150")

seccion1 = Frame(ventana)
seccion1.pack(expand=True, fill='both')

titulo = Label(seccion1,text="Password",bg="black",fg="white",font=("Arial", 18))
titulo.pack()

var1 = tk.StringVar()
Pasw = Label(seccion1,text="Passwords: ")
Pasw.pack()
txtPasw = Entry(seccion1, textvariable=var1, takefocus=True)
txtPasw.pack()

BotonPresionar = Button(seccion1,text="Generador", bg="darkgreen", command=Presionar)
BotonPresionar.pack()

#Main
ventana.mainloop()