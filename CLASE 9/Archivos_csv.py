# nombres = ["José","Cárlos","Ana"]
# apellidos = ["Gómez","Ruiz","Perez"]
# edades = [20,19,34]
# delimitador = ","

# #whit para abrir y no tener que cerrar después
# with open("agenda.csv","w",encoding= "UTF8") as archivo: #retorna un objeto que representa la conexión entre mi programa y un archivo que está o no en el disco
#     for i in range(len(nombres)):
#         mensaje = f"{nombres[i]};{apellidos[i]};{edades[i]}\n"
#         #mensaje = delimitador.join([nombres[i],apellidos[i],str(edades[i]),"\n"]) #mala opción esta, el delimitador termina con coma
#         archivo.write(mensaje)

###usando split###
# with open("agenda.csv","r") as archivo:
#     for linea in archivo:
#         registro = linea.split(",")
#         print(f"{registro[0]}-{registro[1]}-{registro[2]}", end = "")

###usando regets###(MEJOR ESTA OPCIÓN, más pro)
# import re

# def parsear_agenda(path:str)->list:
#     agenda = []
#     with open(path,"r",encoding="UTF8") as archivo:
#         for linea in archivo:
#             registro = re.split(",|\n", linea)
#             contacto = {}
#             contacto["nombre"] = registro[0]
#             contacto["apellido"] = registro[1]
#             contacto["edad"] = registro[2]
#             agenda.append(contacto)
    
#     return agenda

# ######MAIN######
# mi_agenda = parsear_agenda("agenda.csv")
# if len(mi_agenda) != 0:
#     for contacto in mi_agenda:
#         print(f"{contacto['nombre']:20}{contacto['apellido']:20}{contacto['edad']}")