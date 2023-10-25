from data_stark import *

'''
NOMBRE: FABRICIO
APELLIDO: DE SA TORRES
DIVISIÓN: B
-----------
Ejercicio 01
'''
'''
Crear la función 'stark_normalizar_datos()' la cual recibirá por parámetro la
lista de héroes. La función deberá:
● Recorrer la lista y convertir al tipo de dato correcto las keys (solo con
las keys que representan datos numéricos) por ejemplo fuerza (int),
altura (float), etc
● Validar primero que el tipo de dato no sea del tipo al cual será
casteado. Por ejemplo si una key debería ser entero (ejemplo fuerza)
verificar antes que no se encuentre ya en ese tipo de dato.
● Si al menos un dato fue modificado, la función deberá retornar el valor
booleano True
● En caso de que la lista esté vacía o ya se hayan normalizado
anteriormente los datos se deberá retornar el valor booleano False
● Crear una opción en el menú que me permita normalizar los datos (No
se debería poder acceder a ninguna otra opción del menú hasta que
los datos esten normalizados)
● En caso de que la llamada a la función retorne True mostrar un
mensaje diciendo “Datos Normalizados” sino mostrar el mensaje
“Hubo un error al normalizar los datos. Verifique que la lista no este
vacía o que los datos ya no se hayan normalizado anteriormente”
'''

def stark_normalizar_datos(lista:list):
    if len(lista) == 0:
        booleano = False
    for datos in lista:
        fuerza = datos["fuerza"]
        altura = datos["altura"]
        peso = datos["peso"]
        if type(fuerza) == int and type(altura) == float and type(peso) == float:
            booleano = False
        else:
            fuerza = int(datos["fuerza"])
            altura = float(datos["altura"])
            peso = float(datos["peso"])
            booleano = True
    if booleano == True:
        print("Datos normalizados")
    elif booleano == False:
        print("Hubo un error al normalizar los datos. Verifique que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente")
    
    return booleano

# imprimir_booleano = stark_normalizar_datos(lista_vacia)
# print(imprimir_booleano)

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
    
# maximo = obtener_maximo(lista_personajes,"peso")
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
def stark_imprimir_heroes(lista:list):
    bandera_primera = True
    if len(lista) == 0:
        booleano = False
        return booleano
    elif lista == lista_personajes:
        for datos in lista:
            nombre = datos["nombre"]
            identidad = datos["identidad"]
            empresa = datos["empresa"]
            altura = float(datos["altura"])
            peso = float(datos["peso"])
            genero= datos["genero"]
            color_ojos= datos["color_ojos"]
            color_pelo = datos["color_pelo"]
            fuerza = int(datos["fuerza"])
            inteligencia = datos["inteligencia"]
            if bandera_primera == True:
                print(f"{'nombre':20} {'identidad':30} {'empresa':15} {'altura':10} {'peso':10} {'genero':7} {'color_ojos':15} {'color_pelo':15} {'fuerza':10} {'inteligencia':10}")
                bandera_primera = False
            print(f"{nombre:20} {identidad:30} {empresa:15} {altura:10} {peso:10} {genero:7} {color_ojos:15} {color_pelo:15} {fuerza:10} {inteligencia:10}")

    else:
        print(lista)
        
# mas_pesado = obtener_maximo(lista_personajes,"peso")
# stark_imprimir_heroes(mas_pesado)

# lista_mas_pesados = obtener_dato_cantidad(lista_personajes,"maximo","peso")
# stark_imprimir_heroes(lista_mas_pesados)

# stark_imprimir_heroes(lista_personajes)

'''
4.1 Crear la función 'sumar_dato_heroe' la cual recibirá como parámetro una lista de
héroes y un string que representara el dato/key de los héroes que se requiere sumar.
Validar que cada héroe sea tipo diccionario y que no sea un diccionario vacío antes
de hacer la suma. La función deberá retorna la suma de todos los datos según la key
pasada por parámetro
'''
def sumar_dato_heroe(lista:list,key:str):
    acumulador = 0
    if len(lista) == 0:
        return False
    for datos in lista:
        dato_a_sumar = float(datos[key])
        acumulador += dato_a_sumar
    return acumulador

# suma = sumar_dato_heroe(lista_personajes,"peso")
# print(suma)    

'''
4.2 Crear la función ‘dividir’ la cual recibirá como parámetro dos números
(dividendo y divisor). Se debe verificar si el divisor es 0, en caso de serlo, retornar
False, caso contrario realizar la división entre los parámetros y retornar el resultado
'''
def dividir(dividendo:float,divisor:float):
    if divisor == 0:
        return False
    else:
        resultado = dividendo / divisor
        return resultado
    
# resultado = dividir(10,0)
# print(resultado)

'''
4.3 Crear la función ‘calcular_promedio’ la cual recibirá como parámetro una lista de
héroes y un string que representa el dato del héroe que se requiere calcular el
promedio. La función debe retornar el promedio del dato pasado por parámetro
IMPORTANTE: hacer uso de las las funciones creadas en los puntos 4.1 y 4.2
'''
def calcular_promedio(lista:list,key:str):
    contador = 0
    suma_datos = sumar_dato_heroe(lista,key)
    for datos in lista:
        dato = float(datos[key])
        contador += 1
    promedio = dividir(suma_datos,contador)
    return promedio

# promedio = calcular_promedio(lista_personajes,"peso")
# print(promedio)

'''
4.4 Crear la función ‘mostrar_promedio_dato’ la cual recibirá como parámetro una
lista de héroes y un string que representa la clave del dato
● Se debe validar que el dato que se encuentra en esa clave sea de tipo int o
float. Caso contrario retornaria False
● Se debe validar que la lista a manipular no esté vacía , en caso de que esté
vacía se retornaria también False
'''
def mostrar_promedio_dato(lista:list,key:str):
    if len(lista) == 0:
        return False
    for datos in lista:
        if type(datos[key]) == int or type(datos[key]) == float:
            return True
        else:
            return False

# booleano = mostrar_promedio_dato(lista_personajes,"altura") 
# print(booleano)

'''
5.1 Crear la función 'imprimir_menu' que imprima el menú de opciones por pantalla,
el cual permite utilizar toda la funcionalidad ya programada.
'''
def imprimir_menu():
    while True:
        opcion = int(input("1.Normalizar Datos\n2.Obtener Dato\n3.Obtener nombre\n4.Obtener nombre y dato\n5.Obtener maximo\n6.Obtener minimo\n7.Obtener dato cantidad\n8.Imprimir heroes\n9.Sumar dato heroe\n10.Dividir\n11.Calcular promedio\n12.Mostrar promedio dato\n13.Salir\nSeleccione una opción: "))
        match opcion:
            case 1:
                print("--------------------------------------------")
                booleano = stark_normalizar_datos(lista_personajes)
                print("--------------------------------------------")
        if booleano == True: 
            match opcion:
                case 2:
                    print("--------------------------------------------")
                    booleano = obterner_dato(lista_personajes[0],"nombre")
                    print(booleano)
                    print("--------------------------------------------")
                case 3:
                    print("--------------------------------------------")
                    nombre = obtener_nombre(lista_personajes[0],"nombre")
                    print(nombre)
                    print("--------------------------------------------")
                case 4:
                    print("--------------------------------------------")
                    nombre_y_dato = obtener_nombre_y_dato(lista_personajes[0],"peso")
                    print(nombre_y_dato)
                    print("--------------------------------------------")
                case 5:
                    print("--------------------------------------------")
                    maximo = obtener_maximo(lista_personajes,"fuerza")
                    print(maximo)
                    print("--------------------------------------------")
                case 6:
                    print("--------------------------------------------")
                    minimo = obtener_minimo(lista_personajes, "fuerza")
                    print(minimo)
                    print("--------------------------------------------")
                case 7:
                    print("--------------------------------------------")
                    lista_heroes_max_altura = obtener_dato_cantidad(lista_personajes,"maximo","altura")
                    print(lista_heroes_max_altura)
                    print("--------------------------------------------")
                case 8:
                    print("--------------------------------------------")
                    stark_imprimir_heroes(lista_personajes)
                    print("--------------------------------------------")
                case 9:
                    print("--------------------------------------------")
                    suma = sumar_dato_heroe(lista_personajes,"peso")
                    print(suma)
                    print("--------------------------------------------")
                case 10:
                    print("--------------------------------------------")
                    resultado = dividir(10,0)
                    print(resultado)
                    print("--------------------------------------------")
                case 11:
                    print("--------------------------------------------")
                    promedio = calcular_promedio(lista_personajes,"peso")
                    print(promedio)
                    print("--------------------------------------------")
                case 12:
                    print("--------------------------------------------")
                    booleano = mostrar_promedio_dato(lista_personajes,"altura") 
                    print(booleano)
                    print("--------------------------------------------")
                case 13:
                    break

#imprimir_menu()

'''
5.2 Crear la función “validar_entero” la cual recibirá por parámetro un string de
número el cual deberá verificar que sea sea un string conformado únicamente por
dígitos. Retornara True en caso de serlo, False caso contrario
'''
def validar_entero(numero:str):
    if numero.isdigit() == True:
        return True
    else:
        return False
# validar = validar_entero("5")
# print(validar)

'''
5.3 Crear la función 'stark_menu_principal' la cual se encargará de imprimir el menú
de opciones y le pedirá al usuario que ingrese el número de una de las opciones
elegidas y deberá validarlo. En caso de ser correcto dicho número, lo retornara
casteado a int , caso contrario retorna False. Reutilizar las funciones del ejercicio 5.1
y 5.2
'''
def stark_menu_principal():
    opcion = input("1.Normalizar Datos\n2.Obtener Dato\n3.Obtener nombre\n4.Obtener nombre y dato\n5.Obtener maximo\n6.Obtener minimo\n7.Obtener dato cantidad\n8.Imprimir heroes\n9.Sumar dato heroe\n10.Dividir\n11.Calcular promedio\n12.Mostrar promedio dato\n13.Salir\nSeleccione una opción: ")
    if validar_entero(opcion) and int(opcion) > 0 and int(opcion) < 14:
        opcion = int(opcion)
        return opcion
    else:
        return False
    
# numero = stark_menu_principal()
# print(numero)
        
'''
6.Crear la función 'stark_marvel_app'; la cual recibirá por parámetro la lista de héroes
y se encargará de la ejecución principal de nuestro programa.
Utilizar if/elif o match según prefiera. Debe informar por consola en caso de
seleccionar una opción incorrecta y volver a pedir el dato al usuario. Reutilizar las
funciones con prefijo 'stark' donde crea correspondiente.
'''
def stark_marvel_app(lista:list):
    while True:
        opcion = input("1.Normalizar Datos\n2.Obtener Dato\n3.Obtener nombre\n4.Obtener nombre y dato\n5.Obtener maximo\n6.Obtener minimo\n7.Obtener dato cantidad\n8.Imprimir heroes\n9.Sumar dato heroe\n10.Dividir\n11.Calcular promedio\n12.Mostrar promedio dato\n13.Salir\nSeleccione una opción: ")
        if validar_entero(opcion) and int(opcion) > 0 and int(opcion) < 14:
            opcion = int(opcion)
            match opcion:
                case 1:
                    print("--------------------------------------------")
                    booleano = stark_normalizar_datos(lista_personajes)
                    print("--------------------------------------------")
            if booleano == True: 
                match opcion:
                    case 2:
                        print("--------------------------------------------")
                        booleano = obterner_dato(lista_personajes[0],"nombre")
                        print(booleano)
                        print("--------------------------------------------")
                    case 3:
                        print("--------------------------------------------")
                        nombre = obtener_nombre(lista_personajes[0],"nombre")
                        print(nombre)
                        print("--------------------------------------------")
                    case 4:
                        print("--------------------------------------------")
                        nombre_y_dato = obtener_nombre_y_dato(lista_personajes[0],"peso")
                        print(nombre_y_dato)
                        print("--------------------------------------------")
                    case 5:
                        print("--------------------------------------------")
                        maximo = obtener_maximo(lista_personajes,"fuerza")
                        print(maximo)
                        print("--------------------------------------------")
                    case 6:
                        print("--------------------------------------------")
                        minimo = obtener_minimo(lista_personajes, "fuerza")
                        print(minimo)
                        print("--------------------------------------------")
                    case 7:
                        print("--------------------------------------------")
                        lista_heroes_max_altura = obtener_dato_cantidad(lista_personajes,"maximo","altura")
                        print(lista_heroes_max_altura)
                        print("--------------------------------------------")
                    case 8:
                        print("--------------------------------------------")
                        stark_imprimir_heroes(lista_personajes)
                        print("--------------------------------------------")
                    case 9:
                        print("--------------------------------------------")
                        suma = sumar_dato_heroe(lista_personajes,"peso")
                        print(suma)
                        print("--------------------------------------------")
                    case 10:
                        print("--------------------------------------------")
                        resultado = dividir(10,0)
                        print(resultado)
                        print("--------------------------------------------")
                    case 11:
                        print("--------------------------------------------")
                        promedio = calcular_promedio(lista_personajes,"peso")
                        print(promedio)
                        print("--------------------------------------------")
                    case 12:
                        print("--------------------------------------------")
                        booleano = mostrar_promedio_dato(lista_personajes,"altura") 
                        print(booleano)
                        print("--------------------------------------------")
                    case 13:
                        break
        else:
            print("--------------------------------------------")
            print("Seleccione una opción válida")
            print("--------------------------------------------")
            continue

#stark_marvel_app(lista_personajes)

'''
7. Una vez realizadas y probadas las funciones resolver en un menú los siguientes
puntos.
Buenas
Les recomiendo que agreguen la siguiente función al stark 02 (Para los puntos C,D,E,F)

def obtener_superheroes_por_genero(lista_personajes:list,genero:str)

La misma retorna una lista con los heroes de un determinado género
'''

'''
A. Normalizar datos (No se debe poder acceder a los otros puntos)
'''

'''
B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
género NB
'''

'''
C. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
'''

# def obtener_superheroes_por_genero(lista:list,genero:str):
#     for diccionario in lista_personajes:
#         if diccionario["genero"] == genero:
#             max = obtener_maximo(lista,"altura")
#             print(max)

# obtener_superheroes_por_genero(lista_personajes,"F")


'''
D. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
'''

'''
E. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
'''

'''
F. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
'''

'''
G. Recorrer la lista y determinar la fuerza promedio de los superhéroes de
género NB
'''

'''
H. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
'''

'''
I. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
'''

'''
J. Listar todos los superhéroes agrupados por color de ojos.
'''

'''
K. Listar todos los superhéroes agrupados por tipo de inteligencia
'''