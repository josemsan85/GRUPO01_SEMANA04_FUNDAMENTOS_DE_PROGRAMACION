# Definimos la primera función.
def funcion_a():
    valor = 100  # Variable local: solo existe y funciona dentro de 'funcion_a'.
    return valor # Devuelve el número 100.

# Definimos la segunda función.
def funcion_b():
    valor = 200  # Variable local: se llama igual, pero es independiente porque está dentro de 'funcion_b'.
    return valor # Devuelve el número 200.

# Se ejecutan ambas funciones dentro de 'print' para ver sus resultados juntos.
print(funcion_a(), funcion_b())  # Imprime: 100 200