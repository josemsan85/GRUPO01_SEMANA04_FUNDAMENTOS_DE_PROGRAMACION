# Nota: Las listas y diccionarios se pueden modificar (mutar) dentro de una función
# sin usar 'global', siempre que no intentemos reemplazar la lista completa con '='.

notas = []  # Lista global vacía.

def agregar_nota(n):
    # .append() modifica el contenido de la lista existente, así que no requiere 'global'.
    notas.append(n)

agregar_nota(95)  # Agrega el número 95 a la lista.
print(notas)      # Imprime: [95]