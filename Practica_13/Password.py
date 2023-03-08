from tkinter import *
import random

class Password:
    
    def __init__(self):
        self._Letras = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        self._Simbolos = "#@=.>,-}{][?"
        self._Numeros= "0123456789"
        
    def generadorPassword(self):
        Juntar = f'{self._Letras}{self._Numeros}{self._Simbolos}'
        longitud = 8
        Password = random.sample(Juntar, longitud)
        Contra = "".join(Password)
        return Contra

    #print(self.generadorPassword())