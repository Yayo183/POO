
from Personaje import * 

#1. Solicitar datos
print("")
print("###### Datos Heroe ####")
especieH = input("Escribe el especie del heroe: ")
nombreH = input("Escribe el nombre del heroe: ")
AlturaH = float(input("Escribe la altura del heroe: "))
recargaH= int(input("Cuantas Balas recargas al heroe: "))

print("")
print("###### Datos Villano ####")
especieV = input("Escribe el especie del villano: ")
nombreV = input("Escribe el nombre del villano: ")
AlturaV = float(input("Escribe la altura del villano: "))
recargaV= int(input("Cuantas Balas recargas al villano: "))

#2.Crear los objetos

heroe = Personaje(especieH,nombreH,AlturaH)
villano = Personaje(especieV,nombreV,AlturaV)

#3. Usar atributos

#ejemplo de set para 1 atributo
heroe.set_Nombre("Pepe pecas")


print("")
print("###### Objeto Heroe ####")
print("El personaje se llama: " + heroe.get_Nombre())
print("El pertenece a la especie: " + heroe.get_Especie())
print("Tiene una altura de: " + str(heroe.get_Alturas()))
heroe.correr(True)
heroe.LanzarGranadas()
heroe.RecargarArma(recargaH)

#ejemplo de un metodo privado
#heroe.__pensar()

print("")
print("###### Objeto villano ####")
print("El personaje se llama: " + villano.get_Nombre())
print("El pertenece a la especie: " + villano.get_Especie())
print("Tiene una altura de: " + str(villano.get_Alturas()))
villano.correr(True)
villano.LanzarGranadas()
villano.RecargarArma(recargaV)