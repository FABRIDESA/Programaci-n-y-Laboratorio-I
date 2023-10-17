#BURBUJEO
# lista = [5,7,3,6,5,4,2,1,3,6,9,8]
lista = ["Luis","Ana","Maria"]


# for i in range(len(lista)-1):#VERDE
#     print(i)
#     for j in range(i+1, len(lista)):#NARANJA
#         print(f"\t{j}")
        

###########################

for i in range(len(lista)-1):#VERDE
    for j in range(i+1, len(lista)):#NARANJA
        if lista[i] > lista[j]:
            auxiliar = lista[i]
            lista[i] = lista[j]
            lista[j] = auxiliar

for i in range(len(lista)):
    print(lista[i])