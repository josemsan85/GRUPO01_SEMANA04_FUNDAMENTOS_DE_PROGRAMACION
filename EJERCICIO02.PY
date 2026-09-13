def promedio(numeros):
    total = sum(numeros) # local
    n = len(numeros) # local
    return total / n if n else 0
print(promedio([40,67, 23])) # 20.0
#Se utilizaron variables locales (total y n) dentro de la función para almacenar temporalmente los datos del cálculo del promedio