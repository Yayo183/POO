from tkinter import messagebox
import sqlite3 
#import bcrypt

class controladorBD:
    
    def __init__(self):
        pass
    
    #1 Preparamos la conexion para usarla cuando sea necesario
    def conexionBD(self):
        try:
            conexion = sqlite3.connect("C:/Users/yahir/OneDrive/Documents/Escuela/P.O.O/POO/TkinterPy/RESPOUN.db")
            print ("Conectado BD")
            return conexion
        
        except sqlite3.OperationalError:
            print("No se pudo conectar")
            
    #.Metodo para Insertar
    def guardarUsuario(self, nom, cor, con):
        
        #1. Llamar la conexion 
        conx = self.conexionBD()
        
        #2. Revisar que los parametros no esten vacios
        if(nom == "" or cor == "" or con == ""):
            messagebox.showwarning("Aguas!!", "Revisa tu formulario")
            conx.close()
        else:
        #3. Prepara datos y el querySQL
            cursor = conx.cursor()
            conH = self.encriptarContr(con)
            datos = (nom, cor, conH)
            qrInsert = "insert into TablaBD(Nombre, Correo, Contra) values(?,?,?)"
            
        #4. Proceder a insertar y cerrar la conexion
        cursor.execute(qrInsert,datos)
        conx.commit()
        conx.close()
        messagebox.showinfo("Exito, Ya quedo patron tus datos que nos pediste")
        
    
    #def encriptarContr(self, con):
        #conPlana = con
        #conPlana = conPlana.encode() #convierte la contraseña a bytes
        #sal = bcrypt.gensalt()
        #conHa = bcrypt.hashpw(conPlana, sal)
        #print(conHa)
        #return conHa
    
    def consultaUsuario(self,id):
        #1. Preparo la conexion
        conx = self.conexionBD()
        
        #2.verificar que el id no este vacio
        if( id == ""):
            messagebox.showwarning("Mi estimado usuario", "Su ID esta vacio porfavor escribe uno")
            conx.close()
        else:
            #3.proceder a buscar
            try:
                #4. Preparar lo necesario para el select
                cursor = conx.cursor()
                sqlSelect = "select * from TablaBD where id="+id 
                
                #5.Ejecucion y guardado de la consulta
                cursor.execute(sqlSelect)
                RSusuario = cursor.fetchall()
                conx.close()
                
                return RSusuario
                
            except sqlite3.OperationalError:
                print("Error se callo la consulta")
            
        
        
        
        
        
        
        
        
            