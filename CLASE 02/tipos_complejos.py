'''
listas, diccionarios, tuplas, sets
2 en principio:
- lista
    pensarla como un vector, permite manejar distintos tipos de datos
    toda colección puede ser indexada, o sea puedo llegar a los elementos a través del índice
    EJEMPLOS: lista de números, imágenes, de lo que sea
- tupla
    similar a la lista, pero no se pueden modificar
    se puede usar para definir el tamaño de la pantalla del jueguito que vamos a hacer, ancho y alto
    se definen entre paréntesis
    EJEMPLOS: sets de valores inmutables, no necesarios de modificación
- diccionario
    colecciones que se manejan por un par de elementos, las claves o llaves por un lado y los valores por 
el otro (KEY,VALUE)
    se definen entre llaves
    la clave se separa del valor a través de :
    EJEMPLO: representar datos de un alumno, empleado etc
- set (conjuntos)
    no contiene elementos repetidos, duplicados.
    si convierto una lista a un set, el set elimina los duplicados por ej
    se define con llaves
    no respetan el orden de declaración de elemntos
    los elementos son inmutables
    EJEMPLO: crear un set a partir de un iterable
DEFINICIONES DE TIPOS DE DATOS
    - ENTERO(int): Permite representar números enteros, es decir, positivos y negativos no decimales.
    - FLOTANTE(float): Permite representar un número positivo o negativo con decimales
    - COMPLEJOS(complex): Los números complejos son aquellos que tienen dos partes:
una parte real y otra imaginaria
        EJ
        c = 3 + 5j
        print(c) # (3+5j)
        print(c.real) # 3.0
        print(c.imag) # 5.0
        print(type(c)) # <class 'complex'>
    - BOOLEANO(True,False): Es un tipo de dato que permite almacenar dos valores True o False.
    - CADENA DE CARACTERES(str): Los strings son un tipo INMUTABLE que permite almacenar
secuencias de caracteres.
Para crear una, es necesario incluir el texto entre comillas.
    - LISTAS(list): Son uno de los tipos más versátiles del lenguaje, ya que permiten almacenar
un conjunto arbitrario de datos
    - TUPLAS(tuple): Las tuplas son muy similares a las listas, pero son inmutables, lo que
significa que no pueden ser modificadas una vez declaradas.
    - DICCIONARIOS(dict): Un diccionario es una colección de elementos, donde cada uno tiene
una clave(key) y un valor(value).
    - CONJUNTOS(set): Los elementos de un set son únicos, no contiene elementos duplicados.
Los set no respetan el orden que tenían al ser declarados. Sus elmentos son inmutables.
Un set se puede crear haciendo uso de {}. Un set también se puede crear haciendo uso de la 
palabra reservada set la cual permite transformar cualquier objeto iterable en un set
'''
#LISTA
lista = [1, "Hola", 3.67]
print(type(lista))
print(type(lista[2]))
print(lista)
lista.append("Chau")
print(lista)
#TUPLAS
tupla = tuple([5, "Adios", 6.67])
print(tupla)
#DICCIONARIOS
diccionario = {"nombre" : "Juan", "edad" : 21}
print(diccionario["nombre"])
print(diccionario["edad"]) #me devuelve el valor asociado a las claves
#CONJUNTOS(SET)
s = {2, 4, 7, 1, 8, 1}
print(s) # {1, 2, 4, 7, 8}
print(type(s)) #<class 'set'>
otra_lista = [1, 3, 6, 3, 2, 1]
f = set(otra_lista)
print(f) # {1, 2, 3, 6}
print(type(f)) # <class 'set'>