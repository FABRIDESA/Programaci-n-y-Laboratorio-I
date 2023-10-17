#Es un error no controlado en tiempo de ejecución

# a = 10
# b = 0
###
# a = int(input("Ingrese un numero: "))

# print(a)
###

#Excepción en particular
# try: #intentar: acá van las partes de nuestro código que pueden rompen
#     c = a/b
#     print(c)
# except: #capturar la excepción para darle tratamiento, cambiar el flujo del programa, mostrar al usuario un mensaje etc.
#     print("Error, intento dividir por cero")

#Excepción general
# try:
#     a = 5
#     b = 0
#     c = a/b
#     print(c)
# except Exception as ex: #Exception representa todos los tipos de errores que nos puede tirar
#     print(ex)

