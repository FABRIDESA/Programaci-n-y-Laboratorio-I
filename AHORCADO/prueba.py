import random
import re

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

#tema aleatorio
clave = list(diccionario_de_temas.keys())
tema_aleatorio = random.choice(clave)
print(tema_aleatorio)

#palabra aleatoria
lista_palabras = diccionario_de_temas[tema_aleatorio]
print(lista_palabras)
palabra_aleatoria = random.choice(lista_palabras)
palabra_aleatoria = palabra_aleatoria.upper()
print(palabra_aleatoria)

#creamos una lista de letras
lista_letras = ["A","E","I","O","U"]

#ingresar letra (VALIDAR LETRAS)
# letra = input("Ingrese una letra: ").upper
# while letra.isalpha() == False or len(letra) != 1 or letra in lista_letras:
#     letra = input("La letra ya ha sido ingresada o no es una letra válida: ")
# lista_letras.append(letra)

#ocultar palabra aleatoria (REEMPLAZAR LETRAS)
abecedario = "abcdefghijklmnopqrstuvwxyz".upper()
palabra_oculta = palabra_aleatoria 
for letra in abecedario:
    if letra not in lista_letras:
        palabra_oculta = re.sub(letra,"_",palabra_oculta)
    else:
        pass
print(palabra_oculta)
