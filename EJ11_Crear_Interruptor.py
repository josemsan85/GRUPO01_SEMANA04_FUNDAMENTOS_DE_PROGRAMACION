# Función externa para crear el comportamiento de un interruptor.
def crear_interruptor():
    estado = False  # Variable de la función externa (False representa APAGADO).

    # Función interna que cambia el estado cada vez que se llama.
    def cambiar():
        nonlocal estado      # Avisa que modificará 'estado' de la función contenedora.
        estado = not estado  # 'not' invierte el valor booleano (si es False cambia a True, y si es True a False).
        
        # Operador ternario: si 'estado' es True devuelve "ON", si no devuelve "OFF".
        return "ON" if estado else "OFF"

    return cambiar  # Retorna la función interna.

switch = crear_interruptor()  # Creamos nuestro interruptor.
print(switch())               # Cambia de False a True -> Imprime: ON
print(switch())               # Cambia de True a False -> Imprime: OFF
print(switch())               # Cambia de False a True -> Imprime: ON