#IMPORTANTE: Hoy día en lo laboral en cuanto archivos se labura con jason
#Fer data analyst

#es como copiar un diccionario y meterlo en un archivo
#necesitamos un set de funciones diferentes, importar modulo json

###ESCRIBIRLO###
import json

# data = {} #datos que voy a guardar
# data["clientes"] = [] #va a tener una única clave
# data["clientes"].append({"nombre":"Luis","edad":24})
# data["clientes"].append({"nombre":"Maria","edad":33})
# data["clientes"].append({"nombre":"Juan","edad":22})

# with open("clientes.json","w") as archivo: #si no existe el archivo lo crea, si existe lo pisa, ésto en modo w digamos, osea
#     json.dump(data,archivo,indent=4) #indent es opcional, por cada jerarquía haceme 4 espacios
#############

###LEERLO###
with open("clientes.json","r") as archivo:
    data = json.load(archivo)

lista = data["clientes"]
print(lista)
