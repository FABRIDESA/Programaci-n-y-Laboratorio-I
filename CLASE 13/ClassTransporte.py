#una clase con un constructor y 2 metodos
class Transporte:
    def __init__(self,cantidad,velocidad):
        self.cantidad_pasajeros = cantidad
        self.velocidad = velocidad
    
    def avanzar(self):
        print(f"Avanza a {self.velocidad}")

    def frenar(self):
        print("Esta frenando")
#sigue
    def mostrar(self):
        print(f"Pasajeros:{self.cantidad_pasajeros}- Velocidad:{self.velocidad}")