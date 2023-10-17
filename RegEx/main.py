from data import *
import re
from datetime import datetime
'QUEVEDO || BZRP Music Sessions #52'

# def regex_titulo(titulo:str):
#     lista = re.split("[\|#]+| - ", titulo)
#     if len(lista)>=3 and lista[1].strip() == "BZRP Music Sessions":
#         print(f"{lista[0]:20} {lista[2]}")

# for tema in lista_bzrp:
#     regex_titulo(tema["title"])
'2018-06-15 00:00:00'

# def regex_fecha(fecha:str):
    
#     cuatro = "([0-9]{4})"
#     dos = "([0-9]{2})" 
#     lista = re.split(f"{cuatro}-{dos}-{dos} {dos}:{dos}:{dos}", fecha)
    
#     # lista_purgada = [elemento for elemento in lista if elemento != ""]
    
#     lista_enteros = [int(elemento) for elemento in lista if elemento != ""]
    
#     fecha = datetime(lista_enteros[0], lista_enteros[1], lista_enteros[2])
#     print(fecha)

# for tema in lista_bzrp:
#     regex_fecha(tema["date"])

############################################################

def format_date(fecha:str)->datetime:
    cuatro = "([0-9]{4})"
    dos = "([0-9]{2})" 
    lista = re.split(f"{cuatro}-{dos}-{dos} {dos}:{dos}:{dos}", fecha)
    lista_enteros = [int(elemento) for elemento in lista if elemento != ""]
    
    fecha = datetime(lista_enteros[0], lista_enteros[1], lista_enteros[2])
    
    return fecha


def show_sessions_by_date(titulo:str, fecha:datetime):
    lista = re.split("[\|#]+| - ", titulo)
    if len(lista)>=3 and lista[1].strip() == "BZRP Music Sessions":
        print(f"{lista[0]:20} {lista[2]:10}{fecha.day}/{fecha.month}/{fecha.year}")

def filter_sessions_by_date(tema:dict, fecha_filtro:str):
    fecha_formato = format_date(tema["date"])
    fecha_inicio = datetime.strptime(fecha_filtro, "%Y-%m-%d")
    if fecha_formato < fecha_inicio:
        show_sessions_by_date(tema["title"], fecha_formato)

for tema in lista_bzrp:
    filter_sessions_by_date(tema, "2020-10-29")