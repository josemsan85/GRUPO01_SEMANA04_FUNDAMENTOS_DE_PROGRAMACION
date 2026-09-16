# Definimos la función que muestra un saludo por pantalla.
def saludo():
    mensaje = "Hola"      # Variable local: solo existe dentro de saludo().
    print(mensaje)        # Usamos la variable local para imprimirla.

# Ejecutamos la función para ver el resultado.
saludo()                  # Imprime: Hola

# print(mensaje)          # Esto daría NameError: 'mensaje' no existe fuera de la función.
