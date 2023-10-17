def sumar1():
    primer_numero = int(input("Ingrese el primer numero: "))
    segundo_numero = int(input("Ingrese el segundo numero: "))

    suma = primer_numero + segundo_numero

    print(f"La suma es: {suma}")


def sumar2(un_numero, otro_numero):
    suma = un_numero + otro_numero
    print(f"La suma es: {suma}")

def sumar3():
    primer_numero = int(input("Ingrese el primer numero: "))
    segundo_numero = int(input("Ingrese el segundo numero: "))
    suma = primer_numero + segundo_numero
    return suma #devuelve el resultado de la suma


def sumar4(un_numero, otro_numero):
    suma = un_numero + otro_numero
    return suma
#####################################################
def calcular_promedio(lista):
    acumulador = 0
    for video in lista:
        duracion = video["length"]
        acumulador += duracion

    promedio = acumulador / len(lista)

    return promedio
##############
def buscar_temas_mas_vistos(lista:list):
    maximo_vistas = buscar_maximo_key(lista,"views")
    print(f"El maximo de vistas es: {maximo_vistas}")
    mostrar_titulos_maximos(lista,maximo_vistas,"views")

def buscar_temas_mas_largos(lista:list):
    maximo_len = buscar_maximo_key(lista,"length")
    print(f"El tema mas largo dura: {maximo_len}")
    mostrar_titulos_maximos(lista,maximo_len,"length")

def buscar_temas_maximos_key(lista:list, key:str,mensaje:str):
    maximo = buscar_maximo_key(lista,key)
    print(f"{mensaje}: {maximo}")
    mostrar_titulos_maximos(lista,maximo,key)

##############
def buscar_maximo_key(lista:list, key:str):
    bandera_primero = False
    maximo = 0
    for video in lista:
        valor = video[key]
        if bandera_primero == False or valor > maximo:
            maximo = valor
            bandera_primero = True

    return maximo

#############
def mostrar_titulos_maximos(lista:list,maximo_vistas:int,key:str):
    for video in lista:
        valor = video[key]
        titulo = video["title"]
        if valor == maximo_vistas:
            print(f"\t{titulo}")