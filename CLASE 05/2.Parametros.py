##################PARAMETROS POR POSICION################################

def calcular_precio_venta1(precio_costo,porcentaje):
    precio_venta = precio_costo * (1+porcentaje/100)
    return precio_venta

total = calcular_precio_venta1(1000,20)

print(f"El precio de venta es: {total}")

##################PARAMETROS POR NOMBRE################################

def calcular_precio_venta2(precio_costo,porcentaje):
    """_summary_ calcula el precio de venta de un producto, aplicando el porcentaje correspondiente

    Args:
        precio_costo (float): el precio de compra del producto
        porcentaje (int,optional): porcentaje de ganancia. Defaults to 20.

    Returns:
        float: precio de venta de un producto
    """
    precio_venta = precio_costo * (1+porcentaje/100)
    return precio_venta

total = calcular_precio_venta2(porcentaje=20,precio_costo=1000)

print(f"El precio de venta es: {total}")

##################PARAMETROS OPCIONALES (+ tipos -> tipo en retorno)################################
#La regla es ponerlos al final los opcionales y al comienzo los obligatorios

def calcular_precio_venta3(precio_costo:float, porcentaje:int = 20)-> float: #20 es el porcentaje por defecto si no le asigno nada abajo
    #Summary: calcula el precio de venta de un producto, aplicandoel porcentaje correspondiente
    #Parameters:
        #precio_costo: (float)
        #porcentaje: (int)
    #Returns: precio de venta de un producto

    precio_venta = precio_costo * (1+porcentaje/100)
    return precio_venta

# precio_venta = calcular_precio_venta3(1000,30)
precio_venta = calcular_precio_venta3(1000)
print(f"El precio de venta es: {precio_venta}")