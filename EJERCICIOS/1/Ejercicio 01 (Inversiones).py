'''
NOMBRE: FABRICIO
APELLIDO: DE SA TORRES
DIVISIÓN: B
EJERCICIO: Ejercicio 01 (Inversiones)
ESTADO: Ejercicio entregado
'''
'''
Ejercicio 01
Nos encargan el desarrollo de una aplicación que le permita a sus usuarios operar
en la bolsa de valores:
A) Para ello se cargarán los siguientes datos hasta que el usuario lo decida:
* Nombre
* Monto en pesos de la operación (no menor a $10000)
* Cantidad de instrumentos
* Tipo (CEDEAR, BONOS, MEP)
B) Luego del ingreso mostrar en pantalla todos los datos.
C) Realizar los siguientes informes:
1. Tipo de instrumento que más se operó.
2. Cantidad de usuarios que compraron entre 150 y 200 BONOS y que invirtieron
más de $50000.
3. Nombre y cantidad de instrumentos del usuario que compró BONOS o MEP,
que menos dinero invirtió. Puede ser más de uno.
4. Nombre de los usuarios que invirtieron en CEDEAR, cuya inversión supere el
monto promedio
5. Porcentaje de usuarios que no invirtieron en MEP, siempre y cuando el monto
no supere los $50000.
'''
#A CARGA DE DATOS
lista_nombres = ["Fabricio","Fernando","Ezequiel","Matías","Yanina","Yamila","Natalia","Airon","Diego","Sebastian"]
lista_montos = [60000,65000,40000,30000,20000,100000,150000,80000,90000,30000]
lista_cantidad_instrumentos = [160,180,100,50,200,250,303,45,155,180]
lista_tipo = ["bonos","bonos","mep","mep","cedear","cedear","bonos","mep","mep","bonos"]

# while True:
#     nombre = input("Ingrese un nombre: ")
#     while nombre.isalpha() == False:
#         nombre = input("Ingrese un nombre válido: ")
#     lista_nombres.append(nombre)

#     monto = input("Ingrese un monto: ")
#     while monto.isdigit() == False or int(monto) < 10000:
#         monto = input("Ingrese un monto válido: ")
#     lista_montos.append(monto)

#     cantidad_instrumentos = input("Ingrese cantidad de instrumentos: ")
#     while cantidad_instrumentos.isdigit() == False:
#         cantidad_instrumentos = input("Ingrese cantidad de instrumentos válida: ")
#     lista_cantidad_instrumentos.append(cantidad_instrumentos)

#     tipo = input("Ingrese un tipo (CEDEAR, BONOS, MEP): ").lower()
#     while tipo != "cedear" and tipo != "bonos" and tipo != "mep":
#         tipo = input("Ingrese un tipo válido (CEDEAR, BONOS, MEP): ").lower()
#     lista_tipo.append(tipo)

#     continuar = (input("¿Desea continuar?S/N: ")).lower()
#     while continuar != "s" and continuar != "n":
#         continuar = (input("¿Desea continuar?s/n: ")).lower() 
#     if continuar == "n":
#         break

#B MOSTRAR DATOS EN PANTALLA
bandera_x = True
for i in range(len(lista_nombres)):
    nombre = lista_nombres[i]
    monto = lista_montos[i]
    cantidad_instrumentos = lista_cantidad_instrumentos[i]
    tipo = lista_tipo[i]
    if bandera_x == True:
        print(f"{'Nombre':15}{'Monto'}\t{'Cantidad_instrumentos':20}\t{'Tipo':15}")
        bandera_x = False
    print(f"{nombre:15}{monto}\t{cantidad_instrumentos:20}\t{tipo:15}")

print("--------------------------------------------------------------------------")
#C) Realizar los siguientes informes:
#1. Tipo de instrumento que más se operó.

contador_bonos = 0
contador_mep = 0
contador_cedear = 0


for i in range(len(lista_nombres)):
    cantidad_instrumentos = lista_cantidad_instrumentos[i]
    tipo = lista_tipo[i]
    match tipo:
        case "bonos":
            contador_bonos += 1
        case "mep":
            contador_mep += 1
        case "cedear":
            contador_cedear += 1
        
print("Tipo de instrumento que más se operó: ")   
#print(f"bonos:{contador_bonos}\tmep:{contador_mep}\tcedear:{contador_cedear}")
#bonos y mep se operaron más: 4 veces, en el algoritmo tienen que aparecer ambos en este caso

dict_contadores = {"bonos":contador_bonos,"mep":contador_mep,"cedear":contador_cedear}

flag_a = False
maximo_contadores = 0
for key in dict_contadores:
    if flag_a == False or ((dict_contadores["bonos"] or dict_contadores["mep"] or dict_contadores["cedear"]) > maximo_contadores):
        maximo_contadores = (dict_contadores["bonos"] or dict_contadores["mep"] or dict_contadores["cedear"])
        flag_a = True

for key in dict_contadores:
    if dict_contadores[key] == maximo_contadores:
        print(f"\t->{dict_contadores[key]}\t{key}")

print("--------------------------------------------------------------------------")

#2. Cantidad de usuarios que compraron entre 150 y 200 BONOS y que invirtieron más de $50000.

# lista_nombres = ["Fabricio","Fernando","Ezequiel","Matías","Yanina","Yamila","Natalia","Airon","Diego","Sebastian"]
# lista_montos = [60000,65000,40000,30000,20000,100000,150000,80000,90000,30000]
# lista_cantidad_instrumentos = [160,180,100,50,200,250,303,45,155,180]
# lista_tipo = ["bonos","bonos","mep","mep","cedear","cedear","bonos","mep","mep","bonos"]

contador = 0
for datos in range(len(lista_nombres)):
    tipo =  lista_tipo[datos]
    cantidad_instrumentos = lista_cantidad_instrumentos[datos]
    monto = lista_montos[datos] 
    if tipo == "bonos":
        if cantidad_instrumentos >= 150 and cantidad_instrumentos <= 200:
            if monto > 50000:
                contador += 1
print(f"Cantidad de usuarios que compraron entre 150 y 200 BONOS y que invirtieron más de $50000:\n\t->{contador}")

print("--------------------------------------------------------------------------")

#3. Nombre y cantidad de instrumentos del usuario que compró BONOS o MEP, que menos dinero invirtió. Puede ser más de uno.
#nombre-cantidad-tipo-monto(min)

flag_b = False
inversion_min = 0
for datos in range(len(lista_montos)):
    tipo = lista_tipo[datos]
    monto = lista_montos[datos]
    if tipo == "bonos" or tipo == "mep":
        if flag_b == False or monto < inversion_min:
            inversion_min = monto

print("Nombre y cantidad de instrumentos del usuario que compró BONOS o MEP, que menos dinero invirtió. Puede ser más de uno: ")

#nombre-cantidad-tipo-monto(min)

for datos in range(len(lista_montos)):
    nombre = lista_nombres[datos]
    cantidad_instrumentos = lista_cantidad_instrumentos[datos]
    monto = lista_montos[datos]
    if monto == inversion_min:
        print(f"\t->{nombre}\t{tipo}\t{cantidad_instrumentos}")

print("--------------------------------------------------------------------------")

#4. Nombre de los usuarios que invirtieron en CEDEAR, cuya inversión supere el monto promedio

#nombre-tipo(cedear)-monto>monto promedio(calculo)
#monto promedio(calculo): acumulador / len(lista_nombres)

acumulador_monto = 0
for datos in range(len(lista_cantidad_instrumentos)):
    monto = lista_montos[datos]
    acumulador_monto += monto

monto_promedio = acumulador_monto / len(lista_montos)

print("Nombre de los usuarios que invirtieron en CEDEAR, cuya inversión supere el monto promedio: ")

print(f"El monto promedio es: ${monto_promedio:0.2f}")

for datos in range(len(lista_cantidad_instrumentos)):
    nombre = lista_nombres[datos]
    monto = lista_montos[datos]
    tipo = lista_tipo[datos]
    if tipo == "cedear" and monto > monto_promedio:
        print(f"\t->{nombre}")

print("--------------------------------------------------------------------------")

#5. Porcentaje de usuarios que no invirtieron en MEP, siempre y cuando el monto no supere los $50000.
contador_no_mep = 0
for datos in range(len(lista_cantidad_instrumentos)):
    tipo = lista_tipo[datos]
    monto = lista_montos[datos]
    if tipo != "mep" and monto <= 50000:
        contador_no_mep += 1
porcentaje_no_mep_no_50000 = contador_no_mep * 100 / len(lista_cantidad_instrumentos)

print(f"Porcentaje de usuarios que no invirtieron en MEP, siempre y cuando el monto no supere los $50000:\n\t->{porcentaje_no_mep_no_50000}%")

print("--------------------------------------------------------------------------")

