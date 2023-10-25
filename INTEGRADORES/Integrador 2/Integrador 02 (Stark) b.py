from data_stark import *

'''
NOMBRE: FABRICIO
APELLIDO: DE SA TORRES
DIVISIÓN: B
-----------
Ejercicio 01
'''
'''
def stark_normalizar_datos(lista_personajes:list) -> bool:
    #Función: los datos que no sean float o int, se convierten. Se muestra en consola si fueron o no normalizados correctamente.
    #Parámetros: lista de diccionarios (lista_personajes)
    #Retorno: un booleano. True en caso de haberse normalizado correctamente, False si la lista está vacía.
    datos_normalizados = False
    if len(lista_personajes) > 0:
        for heroe in lista_personajes:
            altura = heroe["altura"]
            peso = heroe["peso"]
            fuerza = heroe["fuerza"]

            if type(altura) != float:
                heroe["altura"] = float(altura)
                datos_normalizados = True
            if type(peso) != float:
                heroe["peso"] = float(peso)
                datos_normalizados = True
            if type(fuerza) != int:
                heroe["fuerza"] = int(fuerza)
                datos_normalizados = True
    else:
        datos_normalizados = False

    if datos_normalizados == True:
        print('Datos Normalizados')
    else:
        print('Hubo un Error al normalizar los datos. Verifique que la lista no este Vacía o que los datos ya no se hayan normalizado anteriormente')

    return datos_normalizados
'''
def stark_normalizar_datos(lista):
    for datos in lista:
        nombre = datos["nombre"]
        identidad = datos["identidad"]
        empresa = datos["empresa"]
        altura = datos["altura"]
        peso = datos["peso"]
        genero= datos["genero"]
        color_ojos= datos["color_ojos"]
        color_pelo = datos["color_pelo"]
        fuerza = datos["fuerza"]
        inteligencia = datos["inteligencia"]
        if type(altura) != float or type(peso) != float or type(fuerza) != int:
            altura = float(datos["altura"])
            peso = float(datos["peso"])
            fuerza = int(datos["fuerza"])
            return lista
        
        
# nueva_lista = stark_normalizar_datos(lista_personajes)
# print(nueva_lista)

def obterner_dato(diccionario:dict, key:str):
    if len(diccionario) == 0:
        booleano = False 
    for clave in diccionario:
        if clave.find(key) == 0:
            booleano = True
            break
        else:
            booleano = False
    return booleano

# booleano = obterner_dato(lista_personajes[0],"nombre")
# print(booleano)

def obtener_nombre(diccionario:dict,key):
    if len(diccionario) == 0:
        booleano = False 
    for clave in diccionario:
        if clave.find(key) == 0:
            booleano = True
            diccionario["nombre"] = (f"Nombre: {diccionario['nombre']}")
            break
        else:
            booleano = False
    if booleano == False:
        return booleano

    return diccionario["nombre"]

# nombre = obtener_nombre(lista_personajes[0],"nombre")
# print(nombre)

def obtener_nombre_y_dato(diccionario:dict,key:str):
    #diccionario representa a un héroe
    #key representa el dato que se desea obtener
    #diccionario = lista_personajes[0]
    if len(diccionario) == 0:
        booleano = False
        return booleano
    for claves in diccionario:
        if claves.find("nombre") == 0:
            diccionario["nombre"] = (f"Nombre: {diccionario['nombre']} |")
        elif claves.find(key) == 0:
            diccionario[key] = (f" {key}: {diccionario[key]}")
    
    return diccionario["nombre"] + diccionario[key]

# nombre_y_dato = obtener_nombre_y_dato(lista_personajes[0],"peso")
# print(nombre_y_dato)

def obtener_maximo(lista:list,key:str):
    booleano = True
    flag_a = True
    maximo_dato = 0
    lista_maximos = []
    if len(lista) == 0:
        booleano = False
    for datos in lista:
        if key == "altura" or key == "peso":
            datos[key] = float(datos[key])
        elif key == "fuerza":
            datos[key] = int(datos[key])
        else:
            booleano = False
            break
        if flag_a == True or datos[key] > maximo_dato:
            maximo_dato = datos[key]
            flag_a = False
    if booleano == True:
        for datos in lista:
            if key == "altura" or key == "peso":
                datos[key] = float(datos[key])
            elif key == "fuerza":
                datos[key] = int(datos[key])
            else:
                booleano = False
                break
            if datos[key] == maximo_dato:
                lista_maximos.append(("Nombre",datos["nombre"]))
                lista_maximos.append((key,datos[key]))
                maximo = lista_maximos
        return maximo  
    else: 
        return booleano  
    
# maximo = obtener_maximo(lista_personajes,"fuerza")
# print(maximo)

def obtener_minimo(lista:list,key:str):
    flag_b = False
    cantidad_mínima = 0
    booleano = True
    lista_minimos = []
    if len(lista) == 0:
        booleano = False
    for datos in lista: #datos es cada diccionario en una lista de diccionarios
        if key == "altura" or key == "peso":
            datos[key] = float(datos[key]) #datos[key] ingresa al valor de la clave key
        elif key == "fuerza":
            datos[key] = int(datos[key])
        else:
            booleano = False
            break
        if flag_b == False or datos[key] < cantidad_mínima:
            cantidad_mínima = datos[key]
            flag_b = True
    for datos in lista:
        if key == "altura" or key == "peso":
            datos[key] = float(datos[key]) #datos[key] ingresa al valor de la clave key
        elif key == "fuerza":
            datos[key] = int(datos[key])
        else:
            booleano = False
            break
        if datos[key] == cantidad_mínima:
            lista_minimos.append(("Nombre",datos["nombre"]))
            lista_minimos.append((key,datos[key]))
            minimo = lista_minimos
            #print(f"-> Nombre: {datos['nombre']} | {key}: {datos[key]}")
    if booleano == False:
        return booleano
    else:
        return minimo

# minimo = obtener_minimo(lista_personajes, "fuerza")
# print(minimo)

'''
3.3 Crear la función 'obtener_dato_cantidad()' la cual recibira tres parámetros:

● La lista de héroes
● Un número que me indique el valor a buscar (puede ser la altura
máxima, la altura mínima o cualquier otro dato)
● Un string que representa la key del dato a calcular, por ejemplo: ‘altura’,
‘peso’, ‘edad’, etc.
La función deberá retornar una lista con el héroe o los heroes que cumplan
con la condición pedida. Reutilizar las funciones hechas en los puntos 3.1 y
3.2
Ejemplo de llamada:
mayor_altura = obtener_maximo(lista_heroes,”altura”)
lista_heroes_max_altura = 'obtener_dato_cantidad(lista_heroes,mayor_altura,”altura”)'
El objetivo de estás llamadas es obtener todos los superhéroes que tengan la altura
correspondiente a la altura máxima, y la misma función me podria servir tanto como
para altura menor, como la mayor o alguna altura que yo le especifique también.
'''

def obtener_dato_cantidad(lista:list,numero:int,key:str):
    if str(numero) == "maximo":
        mayor_dato = obtener_maximo(lista,key)
        return mayor_dato
    elif str(numero) == "minimo":
        menor_dato = obtener_minimo(lista,key)
        return menor_dato
    else: 
        dato_especifico_diccionario = obtener_nombre_y_dato(lista[numero],key)
        return dato_especifico_diccionario
    
# lista_heroes_max_altura = obtener_dato_cantidad(lista_personajes,"maximo","altura")
# print(lista_heroes_max_altura)

'''
3.4 Crear la función "stark_imprimir_heroes"; la cual recibirá un parametro:

● La lista de héroes

Validar que la lista de héroes no esté vacía para realizar sus acciones, caso
contrario no hará nada y retornara False
En caso de que la lista no este vacia imprimir la información completa de
todos los heroes de la lista que se le pase
Ejemplo de llamada:

mas_pesado = obtener_maximo(lista_heroes,”peso”)
lista_mas_pesados = 'obtener_dato_cantidad(lista_heroes,mas_pesado ,”peso”)
stark_imprimir_heroes(lista_mas_pesados)' Imprimo sólo los héroes más
pesados
stark_imprimir_heroes(lista_heroes)' Imprimo todos los héroes
'''
# def stark_imprimir_heroes(lista:list):
#     if len(lista) == 0:
#         booleano = False
#         return booleano
#     elif lista == lista_personajes:
#         stark_normalizar_datos(lista_personajes)
#         print(f"{nombre:20} {identidad:30} {empresa:15} {altura:10} {peso:10} {genero:7} {color_ojos:15} {color_pelo:15} {fuerza:10} {inteligencia:10}")
#         return lista
#     else:
#         print(lista)
        
# # mas_pesado = obtener_maximo(lista_personajes,"peso")
# # stark_imprimir_heroes(mas_pesado)

# # lista_mas_pesados = obtener_dato_cantidad(lista_personajes,"maximo","peso")
# # stark_imprimir_heroes(lista_mas_pesados)

# stark_imprimir_heroes(lista_personajes)

