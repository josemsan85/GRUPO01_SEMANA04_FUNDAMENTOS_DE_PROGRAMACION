# Definimos dos funciones distintas que usan el mismo nombre de variable.
def funcion_a():
    valor = 100         # independiente de la de funcion_b().
    return valor         # 'return' entrega el valor calculado en esta función.

def funcion_b():
    valor = 200         # no interfiere con la de funcion_a().
    return valor         # 'return' entrega el valor calculado en esta función.

# Ejecutamos ambas funciones para comprobar que son independientes entre sí.
print(funcion_a(), funcion_b())  # Imprime: 100 200
