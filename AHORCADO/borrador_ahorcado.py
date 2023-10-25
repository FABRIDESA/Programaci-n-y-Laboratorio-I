diccionario_de_temas = {
    "Programacion":  
    ["Algoritmo","Variable","Ciclo","Funcion","Clase"], 
    "Historia":  
    ["Antiguedad","Renacimiento","Colonizacion","Imperio","Revolucion"],
    "Matematica": 
    ["Algebra","Geometria","Calculo","Estadistica","Trigonometria"],
    "Futbol": 
    ["Balon","Gol","Arquero","Delantero","Centrocampista"]
    }

#list(temas.keys())

###Llamo a las claves de un diccionario###

# claves = diccionario_de_temas.keys()
# print(claves)

###Creo una lista con las claves del diccionario###

# claves = list(diccionario_de_temas.keys())
# print(claves)

###Uso del random.choise para seleccionar un elemento de la lista aleatoriamente###
##En este caso quiero una clave aleatoria del diccionario

import random
# claves = list(diccionario_de_temas.keys())
# tema_aleatorio = random.choice(claves)
# print(tema_aleatorio)

###FUNCIÓN TEMA ALEATORIO###
def obtener_tema(temas: dict):
    claves = list(temas.keys())
    tema_aleatorio = random.choice(claves)
    return tema_aleatorio

##captura e impresion de la función##
# tema_aleatorio = obtener_tema(diccionario_de_temas)
# print(tema_aleatorio)

##como llamar a las listas que representan los valores de las claves del diccionario
# lista_de_palabras = diccionario_de_temas["Historia"]
# print(lista_de_palabras)

##hacemos una selección aleatoria de alguna palabra dentro de la lista de palabras
##convertimos la palabra a mayúscula a fines del juego
# palabra_aleatoria = random.choice(lista_de_palabras)
# palabra_aleatoria = palabra_aleatoria.upper()
# print(palabra_aleatoria)

###FUNCIÓN OBTENER PALABRA###
def obtener_palabra(temas:dict,clave:str):
    lista_de_palabras = temas[clave]
    palabra_aleatoria = random.choice(lista_de_palabras)
    palabra_aleatoria = palabra_aleatoria.upper()
    return palabra_aleatoria

##captura e impresion de la función obtener tema y obtener palabra##
#primero obtengo un tema aleatorio, que corresponde a una clave del diccionario
#luego obtengo una palabra aleatoria, que corresponde a un elemento del valor de la clave aleatoria anterior
# tema_aleatorio = obtener_tema(diccionario_de_temas)
# print(tema_aleatorio)
# palabra_aleatoria = obtener_palabra(diccionario_de_temas,tema_aleatorio)
# print(palabra_aleatoria)

#probando validación
# lista_letras = ["A","B","C"]
# letra = input('Ingresar letra: ')
# while not letra.isalpha() or len(letra) != 1 or letra.upper() in lista_letras:  
#     letra = input('El caracter ingresado ya fue ingresado o no es valido: ')

# letra = letra.upper()

################################################
from datos import diccionario_de_temas
import random
import re

def obtener_tema(diccionario: dict):
    claves = list(diccionario.keys())
    tema_aleatorio = random.choice(claves)
    return tema_aleatorio

def obtener_palabra(diccionario: dict, clave: str):
    lista_de_palabras = diccionario[clave]
    palabra = random.choice(lista_de_palabras)
    palabra = palabra.upper()
    return palabra

def validar_letras(lista_letras:list):

    letra = input('Ingresar letra: ')
    while not letra.isalpha() or len(letra) != 1 or letra.upper() in lista_letras:  
        letra = input('El caracter ingresado ya fue ingresado o no es valido: ')

    letra = letra.upper()
    return letra


def reemplazar_letras(palabra:str, lista_letras:list):
    abecedario = "abcdefghijklmnopqrstuvwxyz".upper()
    palabra_oculta = palabra
    for letra in abecedario:
        if letra not in lista_letras:
                palabra_oculta = re.sub(letra, "_", palabra_oculta)
        else:
            pass
    return palabra_oculta

def ahorcado (diccionario:dict):
    jugando = True
    puntaje = 0
    vidas = 6

    while jugando:
        tema = obtener_tema(diccionario)
        palabra = obtener_palabra(diccionario,tema)
        lista_letras = []
        palabra_oculta = reemplazar_letras(palabra,lista_letras)
        print(f"La categoria es:{tema} \n {palabra_oculta}")
        print(f"Tu puntaje es: {puntaje}")


        while palabra != palabra_oculta:
            previa_palabra_oculta = palabra_oculta
            letra_ingresada = validar_letras(lista_letras)
            lista_letras.append(letra_ingresada)
            palabra_oculta = reemplazar_letras(palabra,lista_letras)
            if palabra_oculta == previa_palabra_oculta:
                vidas -= 1
                puntaje -= 5
                print(f"Te quedan {vidas} vidas")
            else:
                puntaje += 10

            if vidas == 0:
                jugando = False
                break
            
            print(palabra_oculta)
        

        puntaje += 100

    print(f"Tu puntaje final es: {puntaje}")
    print("PERDISTE")
            


ahorcado(diccionario_de_temas)