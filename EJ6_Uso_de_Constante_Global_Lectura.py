MODO_DEBUG = True  # Variable global usada como constante (valor Booleano: True o False).

def procesar(dato):
    # Si solo queremos LEER la variable global (no cambiarla), NO hace falta poner 'global'.
    if MODO_DEBUG:
        print(f"[DEBUG] Procesando: {dato}")
        
    return dato.upper()  # .upper() es un método de texto que convierte todo a mayúsculas.

# Probamos la función enviando la palabra "hola".
procesar("hola")  # Imprime: [DEBUG] Procesando: hola