# def modificar_valor(x):
#     x = x +10

# numero = 5

# modificar_valor(numero)
# print(numero)

def modificar_valor(x):
    x = x +10
    return x #revolea x como 15

numero = 5 

numero = modificar_valor(numero) #es la única forma modificar algo inmutable (numero ataja el retorno) (numero = 15)
print(numero)

###CLAVEEEEE###
#las listas son mutables, entonces afecta directamente al parametro actual de la funcion
#pero si paso algo inmutable, no lo puedo modificar por afuera salvo con un return
def cargar_lista(lista):
    lista.append(45)

mi_lista = [45,9,9,44,3]
cargar_lista(mi_lista)
print(mi_lista)