class Personaje:
    
    #Atributos del personaje
    especie = "Humano"
    Nombre = "Master Chief"
    Alturas = "2.70"
    
    #Metodo
    def correr(self,status):
        if(status):
            print("El personaje " + self.Nombre + "esta corriendo")
        else:
            print("El personaje " + self.Nombre + "Se detuvo")
    
    def LanzarGranadas(self):
        print("El personaje " + self.Nombre + "lanzo granada a un covenant")
        
    def RecargarArma(self,municiones):
        cargador = 10
        cargador = cargador + municiones
        print("El arma tiene " + str(cargador) + " balas")

        