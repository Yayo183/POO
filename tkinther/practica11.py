from tkinter import Tk,Button,Frame,messagebox

#5declaramos las funciones
def mostrarMensajes():
    messagebox.showinfo("Aviso","Presionaste el boton azul")
    messagebox.showinfo("Error","Todo fallo con exito")
    print(messagebox.askretrycancel("¿Pregunta", "Ella jugo con tu corazon?"))
    
#6.Funcion para agregar botones
def agregarBoton():
    bottonVerde.config(text="+",bg="green",fg="white")
    botonNuevo = Button(seccion3,text="Nuevo")
    botonNuevo.pack()    
    
#1.Instanciamos el objeto ventana
ventana = Tk()
ventana.title("Ejemplo de 3 Frames ")
ventana.geometry("600x400")#metodo que nos ayuda el tamano de la ventana

#2.Secciones o los frames se agregan
seccion1 = Frame(ventana,bg="red")
seccion1.pack(expand=True,fill='both')

seccion2 = Frame(ventana,bg="white")
seccion2.pack(expand=True,fill='both')

seccion3 = Frame(ventana,bg="dark green")
seccion3.pack(expand=True,fill='both')

#3.agregar botones
bottonAzul= Button(seccion1,text="boton Negro",fg="black",bg="#2A8DC6",command=mostrarMensajes)
bottonAzul.place(x=60,y=60)

bottonNegro= Button(seccion2,text="boton Negro",fg="white",bg='#000000',command=mostrarMensajes) 
bottonNegro.grid(row= 0,column= 0)

bottonAmarillo= Button(seccion2,text="boton Negro",fg="black",bg='#E6F40C',command=mostrarMensajes)
bottonAmarillo.grid(row=1,column=1)

bottonVerde= Button(seccion3,text="boton Negro",fg="black",bg='#10D938',command=agregarBoton)
bottonVerde.configure(height=2, width=10)
bottonVerde.pack()

#diferenciar los Posicionamientos de elementos 



#llamamos el main
ventana.mainloop()
