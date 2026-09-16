# Definimos una "fábrica" de contadores que devuelve una función interna.
def contador_fabrica():
    cuenta = 0               # pertenece a contador_fabrica().

    def incrementar():
        nonlocal cuenta       # 'nonlocal' permite MODIFICAR 'cuenta', no solo leerla.
        cuenta += 1           # Aumentamos la variable enclosing en cada llamada.
        return cuenta         # 'return' entrega el nuevo valor de 'cuenta'.

    return incrementar        # Devolvemos la función interna (closure) para usarla afuera.

# Creamos un contador y lo llamamos varias veces para ver que recuerda su estado.
cont = contador_fabrica()
print(cont())  # Imprime: 1
print(cont())  # Imprime: 2
print(cont())  # Imprime: 3
