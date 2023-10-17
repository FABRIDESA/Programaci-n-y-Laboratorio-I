import re

##SPLIT

# print(re.split(" ","hola mundo 1c"))
# print(re.split("[a-z ]+","hola mundo 125c")) #con el + toma una o más ocurrencias
# print(re.split("[0-9 ]+","hola mundo 125c"))
# print(re.split(("hola |chau"),"hola chau"))
# print(re.split(("[a-z]|[0-9| ]"),"hola mundo @@ 1253 chau"))

##SEARCH

# print(re.search(" ","hola")) #devuelve None porque no encontró la expresión regular que yo le pasé " " dentro de la cadena "hola"
# print(re.search(" ","hola como están?")) #me devuelve un objeto del tipo Match

# print(re.search(" ","hola como están?").span()) #tupla de q indice a q indice va la coincidencia
# print(re.search(" ","hola como están?").start()) #en qué indice comienza la coincidencia
# print(re.search(" ","hola como están?").end()) #en qué indice termina la coincidencia

# print(re.search("[0-9]+","texto con numeros: 123 y letras: aaa").group()) #.group te pasa directamente la coincidencia BUENÍSIMO
#otra forma de encontrar la coincidencia exacta

# texto = "texto con numeros: 123 y letras: aaa"

# span = re.search("[0-9]+",texto).span()
# print(span)
# print(texto[span[0]:span[1]])

##FINDALL (contracara del split)

# texto = "Un 1 Dos 239 Tres 3 Cuatro 44"
# print(re.findall(" ", texto))
# print(re.findall("[0-9]+", texto))
# print(re.findall("[a-z]+", texto))
# print(re.findall("[a-zA-Z]{3,6}", texto)) #si quiero incluir mayúsculas/la llave al contrario del + dice q traigas como mínimo 3 y max 6caracteres

##SUB (reemplaza una cosa por otra)

# texto = "abc abc ccc ddd        abc aaa"
# result = re.sub("abc","xyz",texto)
# print(result)

# result = re.sub('\\s+', " ", texto) #reemplazar los espacios duplicados por un solo espacio
# print(result)

#para no poner doble barra, puedo usar 'r' indicando q a continuación se viene una expresión regular
# texto = "abc abc ccc ddd        abc aaa"
# result = re.sub(r'\s+', " ", texto) #reemplazar los espacios duplicados por un solo espacio
# print(result)

#extra contrabarras (son secuencias de escape)
#\t tabulación
#\n salto de línea
#\s espacio (no se escribe asi nomas en el texto)