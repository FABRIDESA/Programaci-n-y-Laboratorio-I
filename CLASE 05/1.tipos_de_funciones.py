import random
from funciones import *

#1.FUNCIONES NULAS
#definiendo

def sumar1():
    primer_numero = int(input("Ingrese el primer numero: "))
    segundo_numero = int(input("Ingrese el segundo numero: "))

    suma = primer_numero + segundo_numero

    print(f"La suma es: {suma}")


#invocando 
sumar1()

#NO USAR ESTE TIPO DE FUNCIONES QUE NO PIDE NADA NI DEVUELVE NADA

#OBJETIVOS DE UNA FUNCION
#minificacion NO (pide numero, suma, muestra, pide 3 cosas!)
#reutilizacion OK
#depuracion +- (corregir un error en la funcion)
#modificacion +- (agregar algo o mantener algo en la funcion)
#independencia NO (no puedo sumar numeros aleatorios o notas, pido solo ingresar un numero)
#(tampoco puedo mostrar el resultado de la suma usando un text box con tkinter)
#(no puedo usar la suma para calcular un porcentaje, o guardarla en un archivo)

#2.
#difinir una funcion que reciba los parámetros(numeros en este caso)
#RECIBE PARAMETROS, PROCESA COSAS, PERO NO DEVUELVE NADA

def sumar2(un_numero, otro_numero):
    suma = un_numero + otro_numero
    print(f"La suma es: {suma}")

primer_numero = 7
segundo_numero = 5

#paso los numeros por parámetros
sumar2(primer_numero,segundo_numero)

#minificacion +- (sumo y muestro)
#reutilizacion OK
#depuracion +-
#modificacion +-
#independencia +- (mejoró, pero sigue mostrando solo por consola el resultado)

#3.
#NO RECIBE NADA, PROCESA Y DEVUELVE (REQUIERE QUE ALGUIEN ATAJE EL VALOR)

def sumar3():
    primer_numero = int(input("Ingrese el primer numero: "))
    segundo_numero = int(input("Ingrese el segundo numero: "))

    suma1 = primer_numero + segundo_numero

    return suma1

resultado = sumar3()
print(f"El resultado es: {resultado}")

#minificacion +-
#reutilizacion OK
#depuracion +-
#modificacion +-
#independencia +- (la función sigue atada a que el usuario ingrese los numeros en la funcion)

#4
#LA MEJOR FORMA DE INVOCAR UNA FUNCIÓN
#con parámetros de entrada y return

#definiendo
def sumar4(un_numero,otro_numero):
    suma2 = un_numero + otro_numero
    return suma2

#invocando
primer_numero = random.randint(1,60)
segundo_numero = random.randint(55,236)

resultado = sumar4(primer_numero,segundo_numero)

total = resultado * 0.8

print(f"El total: {total:0.2f}%")

#OBJETIVOS DE UNA FUNCIÓN
#minificacion OK
#reutilizacion OK
#depuracion OK
#modificacion OK
#independencia OK
