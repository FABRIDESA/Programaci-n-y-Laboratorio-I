import math

'''
NOMBRE: FABRICIO
APELLIDO: DE SA TORRES
DIVISION: B
EJERCICIO: Ejercicio 04 (Funciones)
ESTADO: Ejercicio entregado
'''

'''
Ejercicio 01: Escribe una función que calcule el área de un círculo. 
La función debe recibir el radio como parámetro y devolver el área.
'''
def calculo_area_circulo(radio:float):
    """_summary_

    Args:
        radio (float): Recibe el radio de un circulo

    Returns:
        float: Retorna el area del círculo
    """
    area = math.pi * radio ** 2
    return area

# area = calculo_area_circulo(4)
# print(area)

'''
Ejercicio 02: Crea una función que verifique si un número dado es par o impar. 
La función debe imprimir un mensaje indicando si el número es par o impar.
'''
def validar_numero_par(numero:float):
    """_summary_

    Args:
        numero (float): Recibe un numero

    Returns:
        bool: True si el numero es par. False si el numero es impar 
    """
    if numero % 2 == 0:
        return True
    else:
        return False
    
# par_o_impar = validar_numero_par(8)
# print(par_o_impar)

'''
Ejercicio 03: Diseña una función que tome una lista de números y devuelva la suma de todos los elementos.
'''
lista_numeros = [7,6,5,36,38,19,3,4,7,18]

def suma_elementos_lista(lista:list):
    """_summary_

    Args:
        lista (list): Recibe una lista de numeros

    Returns:
        int: Suma de los numeros de la lista
    """
    acumulador = 0
    for numeros in lista:
        acumulador += numeros
    return acumulador

# suma = suma_elementos_lista(lista_numeros) #deberia dar 63
# print(suma)

'''
Ejercicio 04: Define una función que encuentre el máximo de tres números. 
La función debe aceptar tres argumentos y devolver el número más grande.
'''
def maximo(primer_numero,segundo_numero,tercer_numero):
    """_summary_

    Args:
        primer_numero (int): Recibe un primer numero
        segundo_numero (int): Recibe un segundo numero
        tercer_numero (int): Recibe un tercer numero

    Returns:
        list: Lista con el/los máximo/s
    """
    lista_numeros2 = []
    lista_maximos = []
    flag_a = False
    max_numero = 0
    lista_numeros2.append(primer_numero)
    lista_numeros2.append(segundo_numero)
    lista_numeros2.append(tercer_numero)
    
    for elementos in lista_numeros2:
        if flag_a == False or elementos > max_numero:
            max_numero = elementos
            flag_a = True

    for elementos in lista_numeros2:
        if elementos == max_numero:
            lista_maximos.append(elementos)
            maximos = lista_maximos
    return lista_maximos

# max = maximo(2,20,20)
# print(max)

'''
Ejercicio 05: Escribe una función que tome una cadena como entrada y devuelva la cadena invertida.
'''
def invertir_cadena(cadena:str):
    """_summary_

    Args:
        cadena (str): Recibe un string

    Returns:
        str: Cadena invertida
    """
    cadena_invertida = ""
    for letra in cadena:
        cadena_invertida = letra + cadena_invertida
    return cadena_invertida

# cadena_invertida = invertir_cadena("Virginia")
# print(cadena_invertida)

'''
Ejercicio 06: Crea una función que reciba una lista de palabras y devuelva una nueva lista con las 
palabras ordenadas alfabéticamente.
'''
lista_palabras = ["Ana","Fernando","Ezequiel","Alejandro","Fabricio","Bianca","Roberto"]
def ordenar_alfabeticamente(lista:list):
    """_summary_

    Args:
        lista (list): Recibe una lista de nombres

    Returns:
        list: Lista nueva con los nombres ordenados alfabeticamente
    """
    lista_ordenada = lista
    lista_ordenada.sort()
    return lista_ordenada

# lista_ordenada = ordenar_alfabeticamente(lista_palabras)
# print(lista_ordenada)

'''
Ejercicio 07: Diseña una función que calcule la potencia de un número. La función debe recibir la base 
y el exponente como argumentos y devolver el resultado.
'''
def potencia_de_un_numero(base,exponente):
    """_summary_

    Args:
        base (int): Recibe la base a ser elevada a un exponente
        exponente (int): Recibe el exponente al que será elevada la base

    Returns:
        int: Potencia de la base sobre el exponente
    """
    resultado = base ** exponente
    return resultado

# resultado = potencia_de_un_numero(4,4)
# print(resultado)

'''
Ejercicio 08: Define una función que reciba una lista de números y devuelva una nueva lista con solo 
los números pares.
'''
lista_numeros_nueva = [2,4,6,7,8,9,11,13,15,14,20,16]

def lista_pares(lista:list):
    """_summary_

    Args:
        lista (list): Recibe una lista de numeros

    Returns:
        list: Devuelve una lista con los numeros pares unicamente
    """
    lista_pares = []
    for numero in lista:
        if numero % 2 == 0:
            lista_pares.append(numero)
    return lista_pares

# pares = lista_pares(lista_numeros_nueva)
# print(pares)

'''
Ejercicio 09: Escribe una función que tome una lista de números y calcule el producto de todos los 
elementos.
'''
def calculo_producto_elementos(lista:list):
    """_summary_

    Args:
        lista (list): Recibe una lista de numeros

    Returns:
        int: Producto de todos los elementos
    """
    multiplicador = 1
    for numero in lista:
        multiplicador *= numero
    return multiplicador

# producto = calculo_producto_elementos(lista_numeros)
# print(producto)

'''
Ejercicio 10: Crea una función que determine si una cadena dada es un palíndromo (se lee igual de 
izquierda a derecha que de derecha a izquierda).
'''
#reconocer es un palíndromo
def es_palindromo(cadena:str):
    """_summary_

    Args:
        cadena (str): Recibe un string

    Returns:
        bool: True si la cadena original y su version inversa son iguales,
        o sea, si son palíndromos. False si no son palíndromos.
    """
    cadena_inversa = ""
    for letra in cadena:
        cadena_inversa = letra + cadena_inversa
    if cadena_inversa == cadena:
        return True
    else:
        return False
    
# booleano = es_palindromo("reconocer")
# print(booleano)

'''
Nota: Todas las funciones deben estar probadas y se podrá acceder a cada una de ellas mediante un menú de opciones.
'''
while 1:
    a = "Calculo area de un circulo"
    b = "¿Numero par o impar?"
    c = "Suma de numeros"
    d = "Máximo"
    e = "Invertir cadena"
    f = "Orden alfabetico"
    g = "Potencia de un numero"
    h = "Devolver numeros pares"
    i = "Producto de numeros"
    j = "¿Es un palíndromo?"
    opcion = int(input(f"1.{a}\n2.{b}\n3.{c}\n4.{d}\n5.{e}\n6.{f}\n7.{g}\n8.{h}\n9.{i}\n10.{j}\n11.Salir\nSeleccione una opción: "))
    match opcion:
        case 1:
            print("-----------------------------------")
            area = calculo_area_circulo(4)
            print(area)
            print("-----------------------------------")
        case 2:
            print("-----------------------------------")
            par_o_impar = validar_numero_par(8)
            print(par_o_impar)
            print("-----------------------------------")
        case 3:
            print("-----------------------------------")
            suma = suma_elementos_lista(lista_numeros)
            print(suma)
            print("-----------------------------------")
        case 4:
            print("-----------------------------------")
            max = maximo(2,20,20)
            print(max)
            print("-----------------------------------")
        case 5:
            print("-----------------------------------")
            cadena_invertida = invertir_cadena("Virginia")
            print(cadena_invertida)
            print("-----------------------------------")
        case 6:
            print("-----------------------------------")
            lista_ordenada = ordenar_alfabeticamente(lista_palabras)
            print(lista_ordenada)
            print("-----------------------------------")
        case 7:
            print("-----------------------------------")
            resultado = potencia_de_un_numero(4,4)
            print(resultado)
            print("-----------------------------------")
        case 8:
            print("-----------------------------------")
            pares = lista_pares(lista_numeros_nueva)
            print(pares)
            print("-----------------------------------")
        case 9:
            print("-----------------------------------")
            producto = calculo_producto_elementos(lista_numeros)
            print(producto)
            print("-----------------------------------")
        case 10:
            print("-----------------------------------")
            booleano = es_palindromo("reconocer")
            print(booleano)
            print("-----------------------------------")
        case 11:
            break