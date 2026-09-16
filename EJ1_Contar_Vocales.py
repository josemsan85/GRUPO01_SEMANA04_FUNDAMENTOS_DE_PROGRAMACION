# 'def' sirve para definir/crear una función. 'texto' es el parámetro que recibe.
def contar_vocales(texto):
    vocales = "aeiouAEIOU"  # Variable local: guarda la cadena con las vocales a buscar.
    conteo = 0             # Variable local: contador que inicia en cero.
    
    # 'for' es un bucle que recorre la cadena 'texto' letra por letra.
    for letra in texto:
        # 'if' es un condicional. 'in' verifica si la letra actual está dentro de la cadena 'vocales'.
        if letra in vocales:
            conteo += 1    # '+= 1' le suma 1 al contador cada vez que encuentra una vocal.
            
    return conteo  # 'return' devuelve el valor final del contador.

# Llamamos a la función pasando "Hola Mundo" y 'print' muestra el resultado en pantalla.
print(contar_vocales("Hola Mundo"))  # Imprime: 4