# Definimos la función externa, que contiene una función anidada.
def externa():
    x = "Hola"                 # Variable del ámbito enclosing: pertenece a externa().

    def interna():
        print(x)               # 'interna' puede LEER 'x' porque es enclosing para ella.

    interna()                  # Llamamos a la función anidada desde dentro de externa().

# Ejecutamos la función externa para ver el resultado.
externa()                      # Imprime: Hola
