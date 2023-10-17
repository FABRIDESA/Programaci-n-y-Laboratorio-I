from data import lista_bzrp
from funciones import *


while True:
    opcion = int(input("1.Tema mas visto\n2.Duracion Promedio\n3.Lista de temas que superan el promedio\n4.Temas mas largos\n5.Salir\nSeleccione una opción: "))
    match opcion:
        case 1:
            buscar_temas_maximos_key(lista_bzrp,"views","El maximo de views es")

        case 2:
            promedio = calcular_promedio(lista_bzrp)

            print(f"La duracion promedio es: {promedio:0.2f}")
        case 3: 
            promedio = calcular_promedio(lista_bzrp)

            print(f"La duracion promedio es: {promedio:0.2f}")
            for video in lista_bzrp:
                duracion = video['length']
                titulo = video['title']
                if duracion > promedio:
                    print(f"\t{titulo}")
        case 4:
            buscar_temas_maximos_key(lista_bzrp,"length","Duracion mas larga")
        case 5:
            break