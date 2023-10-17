#BURBUJEO
# lista = [5,7,3,6,5,4,2,1,3,6,9,8]
lista = [{"nombre":"Juan", "edad":25},{"nombre":"Eduardo", "edad":66},{"nombre":"Ana", "edad":32}]

for i in range(len(lista)-1):#VERDE
    for j in range(i+1, len(lista)):#NARANJA
        if lista[i]["edad"] > lista[j]["edad"]:
            auxiliar = lista[i]
            lista[i] = lista[j]
            lista[j] = auxiliar

for i in range(len(lista)):
    print(f"{lista[i]['nombre']:20}{lista[i]['edad']:20}")