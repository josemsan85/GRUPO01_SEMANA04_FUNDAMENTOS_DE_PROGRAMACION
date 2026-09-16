inventario = [] # global


def agregar(producto):
 global inventario
 inventario.append(producto)

def mostrar():
 global p; 
 for p in inventario:
  print( str (p))

agregar("Laptop")
agregar("Mouse")
mostrar()
# - Laptop