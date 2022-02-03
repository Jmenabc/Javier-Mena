# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from io import open
from colorama import init, Back
import random
init()
""" Aqui iniciamos el documento 5letras, que contiene todas las palabras del
proyecto, ademas de que ponemos todas las variables que vamos a usar"""

palabras=""
FraseF=""
palabra=""
FraseDeljuego=""
intentos=""
x=0
tries=0
i=0
"""REGLAS"""
print("Las reglas son sencillas:")
print("Tienes seis intentos")
print("ROJO: la letra esta en la palabra pero no en esa posicion")
print("VERDE: la letra esta en la palabra y en la posicion adecuada")
print("NADA: la letra no esta en la frase")
print("--------------------------------------------------------------------")
"""empezamos a poner funciones"""
palabras = open('C:/Users/menaj/Downloads/5letras.txt','r')

"""A continuación leemos la lista y dividimos las frases por comas con el método split"""

FraseF = palabras.read().split(" ")

"""Ahora vamos a seleccionar una palabra aleatoria de la lista y la metemos en 
una lista"""

palabra = FraseF[random.randint(0,len(FraseF))]
FraseDeljuego = list(palabra)
FraseDeljuego = [i for i in FraseDeljuego]
print(FraseDeljuego)

"""Ahora creamos tres bucles, 
1. Si se acaban los intentos mientras no se averigue la palabra siga funcionando la aplicacion , 
2. Los bucles for son para ir leyendo las listas e ir comparando conforme  al rango que le señalemos """
#Llamamos a la funcion anterior
def proceso():
    intentos=0
    tries=0
    while  tries<6 and intentos!=FraseDeljuego:
        intentos = input()
        listIntentos = list(intentos)
        #para que nos sea mas cómodo hemos transformado del tiron la frase que introducimos en la lista
        #de esta forma es mas conmodo trabajar
        for i in range(0,5):
            x = listIntentos[i]
            temporal = [0,0,0,0,0] #Este temporal es para que si se imprime la  posición 
            #O en la segunda posicion se guarde si esta bien y no vuelva a imprimirla con un color distinto
            for j in range(0,5):
                if x not in FraseDeljuego and temporal[j]==0 :
                    print(Back.RESET,x,Back.RESET,end=" ")
                    temporal[j]==1
                    break
                else:
                    if i==j and x==FraseDeljuego[j] and temporal[j]==0:
                        print(Back.GREEN,x,Back.RESET,end=" ")
                        temporal[j]==1
                        break
                    elif x in FraseDeljuego and j>=4: #Esta condicion de aqui  una de las opciones que intentamos trabajar fue que
                    #interpretaba que todas las letras que formaban la palabra continuasen despues de entrar en la condicion mostrándose rojas, 
                    #por tanto probamos varias opciones hasta dar con esta la usada actualmente.
                        print(Back.YELLOW,x,Back.RESET,end=" ")
                        temporal[j]==1
                        break
                j=+1    
            i=+1
        tries+=1
        if intentos==palabra:
            print()
            print("enhorabuena")
        else:
            print()
        
proceso()      #funcion  
if intentos==palabra:
    print()
    print("enhorabuena")
else:
    print()
    print("Vuelve a intentarlo en otra ocasión",FraseDeljuego)
    
"""Realizamos la condición para imprimir si el usuario ha completado el desafío 
    o no ha sido capaz de realizarlo, el bucle de arriba recoge la condición de que si la palabra esta bien acabe y sino continue
    realmente es un seguro para que nunca falle"""
        
print(Fore.RESET)
