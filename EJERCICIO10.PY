# Definimos una fábrica que crea un acumulador de sumas.
def crear_acumulador():
    total = 0                  # guarda la suma acumulada.

    def acumular(valor):
        nonlocal total          # 'nonlocal' permite MODIFICAR 'total' en cada llamada.
        total += valor          # Sumamos el nuevo valor al total acumulado.
        return total            # 'return' entrega el total actualizado.

    return acumular             # Devolvemos la función interna (closure) para usarla afuera.

# Creamos un acumulador y lo llamamos varias veces para ver cómo va sumando.
suma = crear_acumulador()
print(suma(10))  # Imprime: 10
print(suma(5))   # Imprime: 15
