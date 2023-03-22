from tkinter import *
#from Password import *
import tkinter as tk
from tkinter import messagebox

#axc = Password()

#def Presionar():
    #text = Password.generadorPassword()
    #messagebox.showinfo("Mostrar", f"password gen: {text}")

def Pregunta():
    longitud = messagebox.
    Caracter = messagebox.askyesno("Que opcion te gustaria elegir", "Caracter Especial")
    Letras = messagebox.askyesno("Que opcion te gustaria elegir", "Letras")
    Numeros = messagebox.askyesno("Que opcion te gustaria elegir", "Numeros")
    print (Caracter,Letras,Numeros)
    
    

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

BotonPresionar = Button(seccion1,text="Generador", bg="darkgreen", command=Pregunta)
BotonPresionar.pack()

#Main
ventana.mainloop()