# Definimos la función que recibe los grados Celsius en la variable 'c'.
def celsius_a_fahrenheit(c):
    factor = 9 / 5                # Variable local: calcula el factor decimal (1.8) dividiendo 9 entre 5.
    fahrenheit = c * factor + 32  # Variable local: aplica la fórmula matemática de conversión.
    return fahrenheit             # 'return' entrega el valor final convertido.

# Ejecutamos la función con 100 y con 0 para probar si funciona.
print(celsius_a_fahrenheit(100))  # Imprime: 212.0
print(celsius_a_fahrenheit(0))    # Imprime: 32.0