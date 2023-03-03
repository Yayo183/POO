class Usuario():
    
    numUsuarios = 0
    
    def __init__(self,Correo,Pass):
        self.Correo = Correo
        self.Pass = Pass
        
        self.conectado = False
        self.intentos = 3
        
        Usuario.numUsuarios += 1
    
    def conectar(self,password=None):
        if password == None:
            myPass = input("Ingrese su Password:")
        else:
            myPass=password
        if myPass == self.Pass:
            print("Te has conectado con exito, Felicidades")
            self.conectado = True
            return True
        else:
            self.intentos -=1
            if self.intentos > 0:
                print("Password fallo con exito, porfavor vuelva a intentarlo")
                if password != None:
                    return False
                print("Intentos restantes:",self.intentos)
                self.conectar()
            else:
                print ("Error, La regaste con exito vuelve a intentarlo")
                print ("no te aguites, bye")
                    
    def Disconnect(self):
        if self.conectado:
            print("Cerraste la sesion con exito")
            self.conectado = False
        else:
            print("Error no robes informacion, o vuelva a intentarlo")
    
    def __str__(self):
        if self.conectado:
            conect = "Conectado"
        else:
            conect = "Desconectado"
        return f"Mi correo de usuario es {self.Correo} y estoy {conect}"
    
#usuario1 = Usuario(input("Ingrese un Correo: "),input("Ingrese un Password: "))
#print(usuario1)

#usuario1.conectar()
#print(usuario1)

#usuario1.Disconnect()
#print(usuario1)

