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

