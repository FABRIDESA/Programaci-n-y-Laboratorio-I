from data import *

#"title":'QUEVEDO || BZRP Music Sessions #52'

# def prueba_1():
#     titulo = 'QUEVEDO || BZRP Music Sessions #52'
#     parte1 = titulo.split("||")
#     artista = parte1[0].strip()
#     parte2 = parte1[1].split("#")
#     tipo = parte2[0].strip()
#     numero = parte2[1].strip()
#     print(f"{numero}-{tipo}-{artista}")

# prueba_1()

def prueba_2(titulo:str):
    parte1 = titulo.split("||")
    artista = parte1[0].strip()
    parte2 = parte1[1].split("#")
    tipo = parte2[0].strip()
    numero = parte2[1].strip()
    print(f"{numero}-{tipo}-{artista}")

for tema in lista_bzrp:
    if tema["title"].find("||") >= 0 and tema["title"].find("#") >= 0: #si find no encuentra devuelve -1
        prueba_2(tema["title"])

##DESPUES TENEMOS QUE VER COMO LLEGAMOS A IMPRIMIR LOS OTROS FORMATOS, TIPO REMIX, COLABORACIONES, ETC

'''
#ejemplo find -1 (significa q no está la palabra)
cadena = "Pepe amigo"
indice = cadena.find("Perro")
print(indice)
'''

#'https://youtube.com/watch?v=h7U8TqOVyxc'
def prueba3(url:str, lista:list):
    #con slice
    codigo = url[28:]
    print(codigo)
    lista.append(codigo)
    
lista = []
for tema in lista_bzrp:
    prueba3(tema['url'],lista)

print(len(lista))
