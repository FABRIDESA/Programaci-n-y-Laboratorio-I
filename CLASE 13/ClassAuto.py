from ClassTransporte import Transporte

#TENER UN ARCHIVO POR CADA CLASE PARA TENER BIEN SEPARADO
class Auto(Transporte): #Auto está heredando de Transporte, el auto ya sabe avanzar, frenar y mostrarse
    def __init__(self,cantidad,velocidad,ruedas):
        #super() es como el self pero de la clase padre
        super().__init__(cantidad,velocidad)
        self.cantidad_ruedas = ruedas