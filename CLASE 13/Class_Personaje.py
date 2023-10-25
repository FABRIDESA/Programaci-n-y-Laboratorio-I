#métodos constructores __...__
#self: es la instancia actual de la clase con la que estoy trabajando (PROX CUATRIMESTRE) (una de las galletitas por ej)
#en este caso self sería uno de todos los personajes creados, luego representará a otro etc.

class Personaje:
    def __init__ (self, id_personaje:int, nombre_personaje:str, puede_volar:bool, poder:int, usa_nano): #Constructores
        self.__id = id_personaje #PUBLICO #self.id define la característica, id define el valor
        self.__nombre = nombre_personaje #PRIVADO
        self.__puede_volar = puede_volar
        self.__usa_nano = usa_nano
        self.__poder = poder

        #PROTEGIDO _id cuando no queremos que se pueda usar desde afuera de la clase
        #PRIVADO __id
        #PUBLICO id

        #self.id -> atributo del personaje

    def retornar_descripcion(self) -> str:
        descripcion = f"{self.__id} - {self.__nombre} - {self.__puede_volar} -\
        {self.__usa_nano}"
        return descripcion
    
    def luchar(self, otro_personaje):
        print(f"{self.__nombre} VS {otro_personaje.__nombre}")
        if(self.__poder > otro_personaje.__poder):
            print(f"Gano: {self.__nombre}")
        elif(self.__poder < otro_personaje.__poder):
            print(f"Gano: {otro_personaje.__nombre}")
        else:
            print("Hubo empate")

    #GETTERS y SETTERS
    #getter me devolvería el valor del volumen del control
    #setters me deja cambiar el volumen

    def get_nombre(self): #LEER
        return self.__nombre
    
    def set_nombre(self,nombre): #ESCRIBIR
        self.__nombre = nombre.strip().title()

    def set_id(self,id):
        if id > 0:
            self.__id = id