# Definimos la función que calcula el área de un rectángulo.
def calcular_area(base, altura):
    area = base * altura       # Solo existe mientras se ejecuta la función.
    return area                 # 'return' entrega el valor calculado a quien llamó la función.

# Ejecutamos la función con base=5 y altura=3 para probar si funciona.
resultado = calcular_area(5, 3)
print(resultado)                # Imprime: 15

# print(area)                   # Esto daría NameError: 'area' no existe fuera de la función.
