# Definimos la función 'promedio' que recibe como parámetro una lista llamada 'numeros'.
def promedio(numeros):
    total = sum(numeros)  # sum() es una función integrada de Python que suma los elementos de la lista. (Variable local)
    n = len(numeros)      # len() cuenta cuántos elementos hay en la lista. (Variable local)
    
    # 'return' devuelve la división total / n.
    # 'if n else 0' es un condicional simple para evitar dividir entre 0 si la lista está vacía.
    return total / n if n else 0

# Pasamos una lista con [10, 20, 30] a la función e imprimimos la respuesta.
print(promedio([10, 20, 30]))  # Imprime: 20.0