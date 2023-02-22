class Personaje:
    
    #Definimos el contructor de personaje 
    def __init__(self,esp,nom,alt):  
        self.especie = esp #eso se llama inicializacion de atributos 
        self.Nombre = nom
        self.Alturas = alt
    
    #Metodo
    def correr(self,status):
        if(status):
            print("El personaje " + self.Nombre + "esta corriendo")
        else:
            print("El personaje " + self.Nombre + "Se detuvo")
    
    def LanzarGranadas(self):
        print("El personaje " + self.Nombre + "lanzo granada a ")
        
    def RecargarArma(self,municiones):
        cargador = 10
        cargador = cargador + municiones
        print("El arma tiene " + str(cargador) + " balas")

        