#Inicializacion 

# mi_cadena = "         esto es una cadena           "
# print(f"Aca empieza:{mi_cadena}:Aca termina")
##################Strip#########################
#sin_espacios = mi_cadena.strip()
#sin_espacios = mi_cadena.lstrip()
# sin_espacios = mi_cadena.rstrip()

# print(f"Aca empieza:{sin_espacios}:Aca termina")

###############################################
mi_cadena = "esto es una - cadena 123" 

mayuscula = mi_cadena.upper()

minuscula = mi_cadena.lower()

capital = mi_cadena.capitalize()

titulo = mi_cadena.title()#mayúscula a cada palabra de la cadena

print(mayuscula)
print(minuscula)
print(capital)
print(titulo)

#####################REPLACE##########################
mi_cadena = mi_cadena.replace("cadena","***")
print(mi_cadena)

####################SPLIT#############################
#devuelve una lista de strings, indicando el delimitador para separar
mi_cadena = "Mario,Giovanni,Fausto,Mariano,German"
lista_split = mi_cadena.split(",")

for nombre in lista_split:
    if nombre != "Mariano":
        print(nombre)

###########JOIN################################
#convierte una lista a una cadena
dia = "20"
mes = "10"
año = "1987"
separador = "/"

fecha = separador.join([dia,mes,año])

print(fecha)
#######ZFILL##################
#Completa una cadena con ceros a la izquierda
#como requisito el formato de legajo tiene que tener 6 digitos
legajo = "555"
legajo = legajo.zfill(6)

print(legajo)
#######################
mi_cadena = "holadivBD"
print(mi_cadena.isalpha())

mi_cadena = "holadiv1BD"
print(mi_cadena.isalnum())

mi_cadena = "123"
print(mi_cadena.isdigit())
###################
mi_cadena = "123pepe"
print(len(mi_cadena))

print(mi_cadena.count("pe"))
#encuentra la cantidad de incidencias de una subcadena dentro de una cadena principal

###############################

cadena = "hola hola hola chau hola"
print(cadena.find("hola",6)) #6 es parametro opcional, buscar desde cual caracter
print(cadena.rfind("hola")) #busca de derecha a izquierda

###############################SLICES#####

cadena = "Hola mundo 1BD"

print(cadena[5:10]) #tomé una subcadena de una cadena
print(cadena[5:10:2])#salta de 2 en dos
print(cadena[5:]) #desde el 5 hasta el final
print(cadena[:5]) #o cadena[0:5]
