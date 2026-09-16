# Definimos una fábrica que genera identificadores únicos.
def generador_id():
    ultimo_id = 0             # guarda el último ID generado.

    def nuevo_id():
        nonlocal ultimo_id     # 'nonlocal' permite MODIFICAR 'ultimo_id' en cada llamada.
        ultimo_id += 1         # Incrementamos el contador enclosing.
        return f"ID-{ultimo_id:04d}"  # 'return' entrega el ID formateado con ceros a la izquierda.

    return nuevo_id            # Devolvemos la función interna (closure) para usarla afuera.

# Creamos un generador y lo llamamos varias veces para ver los IDs generados.
gen = generador_id()
print(gen())  # Imprime: ID-0001
print(gen())  # Imprime: ID-0002
