# Función contenedora (la de afuera).
def generador_id():
    ultimo_id = 0  # Variable dentro de la función externa.

    # Función anidada (una función dentro de otra).
    def nuevo_id():
        nonlocal ultimo_id  # 'nonlocal' permite modificar la variable 'ultimo_id' de la función externa.
        ultimo_id += 1      # Le suma 1 al ID cada vez que se ejecuta.
        
        # ':04d' le da formato al número para que siempre tenga 4 dígitos (llena con ceros a la izquierda).
        return f"ID-{ultimo_id:04d}"

    return nuevo_id  # Devuelve la función interna para poder usarla después.

gen = generador_id()  # Guardamos la función en 'gen'.
print(gen())          # Primera llamada -> Imprime: ID-0001
print(gen())          # Segunda llamada (recuerda el valor anterior) -> Imprime: ID-0002