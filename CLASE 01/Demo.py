#Interpretado
#No es fuertemente tipado, no tengo que definir que tal cosa se guarde como entero, se asigna automaticamente el tipo de dato
#VARIABLES INMUTABLES

#dirección de memoria de una variable (id)
numero = 5
print(id(numero))
numero = "Hola"
print(id(numero))
lista = [1,2,3,4,5]
print(id(lista))
lista.append(6)
print(lista)
print(id(lista))