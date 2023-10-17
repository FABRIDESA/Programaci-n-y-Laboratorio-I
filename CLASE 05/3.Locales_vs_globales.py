def estableces_valor_local(valor):
    # global mi_variable #no usarlo
    # mi_variable = 5 #variable local a la función
    print(f"Valor de la variable dentro de la funcion: {valor}")
    print(f"Id de la variable dentro de la funcion: {id(valor)}")

mi_variable = 55 #variable global por fuera de la función
estableces_valor_local(mi_variable)
print(f"Valor de la variable dentro de la funcion: {mi_variable}")
print(f"Id de la variable fuera de la funcion: {id(mi_variable)}")
