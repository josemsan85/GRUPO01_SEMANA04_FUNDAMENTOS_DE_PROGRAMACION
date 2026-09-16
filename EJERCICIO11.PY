# Definimos una fábrica que crea un interruptor ON/OFF.
def crear_interruptor():
    estado = False              # guarda si está encendido o apagado.

    def cambiar():
        nonlocal estado          # 'nonlocal' permite MODIFICAR 'estado' en cada llamada.
        estado = not estado      # Invertimos el valor booleano (True <-> False).
        return "ON" if estado else "OFF"  # 'return' entrega el texto según el nuevo estado.

    return cambiar               # Devolvemos la función interna (closure) para usarla afuera.

# Creamos un interruptor y lo llamamos varias veces para ver cómo alterna.
switch = crear_interruptor()
print(switch())  # Imprime: ON
print(switch())  # Imprime: OFF
print(switch())  # Imprime: ON
