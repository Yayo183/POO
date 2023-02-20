
from Personaje import * 

#1. Crear un objeto de la clase personaje

heroe = Personaje()

#2. Usar atributos

print("El personaje se llama: " + heroe.Nombre)
print("El pertenece a la especie: " + heroe.especie)
print("Tiene una altura de: " + heroe.Alturas)

#3. Metodos

heroe.correr(True)
heroe.LanzarGranadas()
heroe.RecargarArma(87)