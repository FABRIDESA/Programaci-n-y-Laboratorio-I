from Class_Personaje import Personaje

personaje = Personaje(5,"Ironman",True,150,True)

# print(personaje.retornar_descripcion())

otro_personaje = Personaje(6,"Thor",True,190,False)

# print(otro_personaje.retornar_descripcion())

personaje.luchar(otro_personaje) #Relacion de colaboración

tercer_personaje = Personaje(7,"Capitan America",False,200,False)

otro_personaje.luchar(tercer_personaje)

######################


personaje.set_nombre("          superior ironman       ")

print(personaje.get_nombre())




















'''
def inicializar(diccionario, id, nombre, puede_volar, usa_nano):
    diccionario["id"] = id
    diccionario["nombre"] = nombre
    diccionario["puede_volar"] = puede_volar
    diccionario["usa_nano"] = usa_nano

def mostrar_personaje(diccionario):
    print(f"{diccionario['id']} - {diccionario['nombre']} - {diccionario['puede_volar']} -\
          {diccionario['usa_nano']}")

personaje = {}

inicializar(personaje, 1, "IronMan", True, True)

mostrar_personaje(personaje)
'''
