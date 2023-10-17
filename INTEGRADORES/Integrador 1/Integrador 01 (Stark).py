from data_stark import lista_personajes

'''
NOMBRE: FABRICIO
APELLIDO: DE SA TORRES
EJERCICIO: Integrador 01 (Stark)
ESTADO: Integrador entregado
'''
'''
Luego de analizar el set de datos correspondiente resolver el Desafío #01:

A. Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe
B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor
fuerza (MÁXIMO)
C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo
(MÍNIMO)
D. Recorrer la lista y determinar el peso promedio de los superhéroes
masculinos (PROMEDIO)
E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier
género) los cuales su fuerza supere a la fuerza promedio de todas las
superhéroes de género femenino

NOTA: Se debe construir un menú en el que se sea posible acceder a cada una de
las opciones (A-E)
'''
while True:
    print("-----------------------------------------------------------------------------------------------------------")
    opcion = input("A.Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe\nB.Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor fuerza (MÁXIMO)\nC.Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo (MÍNIMO)\nD.Recorrer la lista y determinar el peso promedio de los superhéroes masculinos (PROMEDIO)\nE.Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier género) los cuales su fuerza supere a la fuerza promedio de todas las superhéroes de género femenino\nS.Salir\nSeleccione una opción: ")
    match opcion:
        case "A":
            bandera_primera = True
            for datos in lista_personajes: #los diccionarios no están definidos con nombres
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

        case "B":
            bandera_primera = False
            bandera_segunda = False
            mayor_fuerza = 0
            for datos in lista_personajes:
                fuerza = int(datos["fuerza"]) 
                if bandera_primera == False or fuerza > mayor_fuerza:
                    mayor_fuerza = fuerza
                    bandera_primera = True
            print(f"El máximo de fuerza es: {mayor_fuerza}")
            for datos in lista_personajes:
                identidad = datos["identidad"]
                peso = float(datos["peso"])
                fuerza = int(datos["fuerza"])
                if bandera_segunda == False:
                    print(f"{'identidad':30} {'peso':10} {'fuerza':10}")
                    bandera_segunda = True
                if fuerza == mayor_fuerza:
                    print(f"{identidad:30} {peso:10}{fuerza:10}")

        case "C":
            #1ro saber la altura más baja
            bandera_primera = False
            bandera_segunda = False
            mas_bajo= 0
            for datos in lista_personajes:
                altura = float(datos["altura"])
                if bandera_primera == False or altura < mas_bajo:
                    mas_bajo = altura
                    bandera_primera = True
            print(f"La altura más baja es: {mas_bajo}")
            #2do volver a recorrer la lista para ver a quienes corresponde ser los más bajos
            for datos in lista_personajes:
                altura = float(datos["altura"])
                nombre = datos["nombre"]
                identidad = datos["identidad"]
                if bandera_segunda == False:
                    print(f"{'nombre':20} {'identidad':30} {'altura':10}")
                    bandera_segunda = True
                if altura == mas_bajo:
                    print(f"{nombre:20} {identidad:30} {altura:10}")

        case "D":
            contador = 0
            acumulador = 0
            for datos in lista_personajes:
                peso = float(datos["peso"])
                genero = datos["genero"]
                if genero == "M":
                    contador += 1
                    acumulador += peso
            promedio = acumulador / contador
            print(f"Peso promedio de los superhéroes masculinos: {promedio:0.2f}")

        case "E":
            '''
            E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier
            género) los cuales su fuerza supere a la fuerza promedio de todas las
            superhéroes de género femenino
            '''
            #1ro Cálculo de la fuerza promedio de todas las superhéroes de género femenino
            bandera_primera = False
            contador = 0
            acumulador = 0
            for datos in lista_personajes:
                fuerza = int(datos["fuerza"])
                genero = datos["genero"]
                if genero == "F":
                    contador += 1
                    acumulador += fuerza
            promedio = acumulador / contador
            print(f"La fuerza promedio de todas las superhéroes de género femenino es: {promedio:0.2f}")
            #2do Mostrar nombre y peso de los superhéroes (cualquier género) los cuales su fuerza supere a la fuerza promedio de todas las superhéroes de género femenino
            for datos in lista_personajes:
                nombre = datos["nombre"]
                peso = float(datos["peso"])
                fuerza = int(datos["fuerza"])
                if fuerza > promedio:
                    if bandera_primera == False:
                        print(f"{'nombre':20} {'peso':10} {'fuerza':10} {'genero':7}")
                        bandera_primera = True
                    print(f"{nombre:20} {peso:10} {fuerza:10} {genero:7}")

        case "S":
            break
