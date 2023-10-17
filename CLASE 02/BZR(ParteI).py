from data import lista_bzrp

# bandera_primero = False
# maximo_vistas = 0
# for video in lista_bzrp:
#     vistas = video["views"]
#     if bandera_primero == False or vistas > maximo_vistas:
#         maximo_vistas = vistas
#         bandera_primero = True

# print(f"El maximo de vistas es: {maximo_vistas}")

# for video in lista_bzrp:
#     vistas = video["views"]
#     titulo = video["title"]
#     if vistas == maximo_vistas:
#         print(f"\t{titulo}")

# #Tiempo promedio

# acumulador = 0
# for video in lista_bzrp:
#     duracion = video["length"]
#     acumulador += duracion

# promedio = acumulador / len(lista_bzrp)

# print(f"La duracion promedio es: {promedio:0.2f}")

# #Lista de temas que superan la duración promedio
# for video in lista_bzrp:
#     duracion = video['length']
#     titulo = video['title']
#     if duracion > promedio:
#         print(f"\t{titulo}")

#int(input("1.Tema mas visto\n2.Duracion Promedio\n3.Lista de temas sobre el promedio\n4.Salir\nSeleccione una opción: "))

while True:
    opcion = int(input("1.Tema mas visto\n2.Duracion Promedio\n3.Lista de temas que superan el promedio\n4.Salir\nSeleccione una opción: "))
    match opcion:
        case 1:
            bandera_primero = False
            maximo_vistas = 0
            for video in lista_bzrp:
                vistas = video["views"]
                if bandera_primero == False or vistas > maximo_vistas:
                    maximo_vistas = vistas
                    bandera_primero = True

            print(f"El maximo de vistas es: {maximo_vistas}")

            for video in lista_bzrp:
                vistas = video["views"]
                titulo = video["title"]
                if vistas == maximo_vistas:
                    print(f"\t{titulo}")
        case 2:
            acumulador = 0
            for video in lista_bzrp:
                duracion = video["length"]
                acumulador += duracion

            promedio = acumulador / len(lista_bzrp)

            print(f"La duracion promedio es: {promedio:0.2f}")
        case 3: 
            acumulador = 0
            for video in lista_bzrp:
                duracion = video["length"]
                acumulador += duracion

            promedio = acumulador / len(lista_bzrp)

            print(f"La duracion promedio es: {promedio:0.2f}")
            for video in lista_bzrp:
                duracion = video['length']
                titulo = video['title']
                if duracion > promedio:
                    print(f"\t{titulo}")
        case 4:
            break