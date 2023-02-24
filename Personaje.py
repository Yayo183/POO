class Personaje:
    
    #Definimos el contructor de personaje y los encapsulamos 
    def __init__(self,esp,nom,alt):  
        self.__especie = esp #eso se llama inicializacion de atributos 
        self.__Nombre = nom
        self.__Alturas = alt
    
    #Metodo
    def correr(self,status):
        if(status):
            print("El personaje " + self.__Nombre + "esta corriendo")
        else:
            print("El personaje " + self.__Nombre + "Se detuvo")
    
    def LanzarGranadas(self):
        print("El personaje " + self.__Nombre + "lanzo granada a ")
        
    def RecargarArma(self,municiones):
        cargador = 10
        cargador = cargador + municiones
        print("El arma tiene " + str(cargador) + " balas")
        
    def __pensar(self):
        print("Toy pensando......")

    #declarar getters y setters de atributos
    def get_Nombre(self):
        return self.__Nombre
    
    def set_Nombre(self,Nom):
        self.__Nombre = Nom
        
    def get_Especie(self):
        return self.__especie
    
    def set_Especie(self,Esp):
        self.__Nombre = Esp
        
    def get_Alturas(self):
        return self.__Alturas
    
    def set_Alturas(self,Alt):
        self.__Alturas = Alt