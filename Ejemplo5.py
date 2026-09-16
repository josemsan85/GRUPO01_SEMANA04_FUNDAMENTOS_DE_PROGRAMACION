# Definimos la función que calcula el promedio de una lista de números.
def promedio(numeros):
    total = sum(numeros)        # suma todos los números de la lista.
    n = len(numeros)            # cuenta cuántos números hay en la lista.
    return total / n if n else 0  # 'return' entrega el promedio (o 0 si la lista está vacía).

# Ejecutamos la función con [10, 20, 30] para probar si funciona.
print(promedio([10, 20, 30]))   # Imprime: 20.0
