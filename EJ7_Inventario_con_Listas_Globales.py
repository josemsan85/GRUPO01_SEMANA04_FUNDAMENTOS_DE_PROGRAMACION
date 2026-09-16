inventario = []  # Variable global: inicia como una lista vacía.

def agregar(producto):
    global inventario           # Avisa que usará la lista global.
    inventario.append(producto) # .append() sirve para agregar un nuevo elemento al final de la lista.

def mostrar():
    # Recorremos la lista 'inventario' elemento por elemento guardándolo en la variable 'p'.
    for p in inventario:
        print(f"- {p}")

# Agregamos elementos a la lista y luego la mostramos.
agregar("Laptop")
agregar("Mouse")
mostrar()
# Imprime:
# - Laptop
# - Mouse