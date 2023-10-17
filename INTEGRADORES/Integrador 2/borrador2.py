# lista_numeros2 = [2,4,20,20]
# # print(lista_numeros2[0])

# flag_a = False
# max_numero = 0
# for elementos in lista_numeros2:
#     if flag_a == False or elementos > max_numero:
#         max_numero = elementos
#         flag_a = True
# for elementos in lista_numeros2:
#     if elementos == max_numero:
#         print(elementos)
###########################################
# cadena = "Virginia"
# cadena_invertida = ""

# for letra in cadena:
#     cadena_invertida = letra + cadena_invertida
#     #iteracion 1 -> '' = 'V' + '' 
#     #iteracion 2 -> 'V' = 'i' + 'V'
#     #iteracion 3 -> 'iV' = 'r' + 'iV' 
#     #iteracion 4 -> 'riV' = 'g' + 'riV'
#     #iteracion 5 -> 'griV' = 'i' + 'griV'
#     #iteracion 6 -> 'igriV' = 'n' + 'igriV'
#     #iteracion 7 -> 'nigriV' = 'i' + 'nigriV'
#     #iteracion 8 -> 'inigriV' = 'a' + 'inigriV' -> ainigriV

# print(cadena_invertida)
###########################################
lista_palabras = ["Ana","Fernando","Ezequiel","Alejandro","Fabricio","Bianca","Roberto"]

lista_palabras.sort()
print(lista_palabras)