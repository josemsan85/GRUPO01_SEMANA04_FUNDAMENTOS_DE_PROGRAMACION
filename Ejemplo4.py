# Definimos la función que cuenta cuántas vocales tiene un texto.
def contar_vocales(texto):
    vocales = "aeiouAEIOU"      # guarda las letras consideradas vocales.
    conteo = 0                  # acumula la cantidad de vocales encontradas.
    for letra in texto:         # Recorremos cada letra del texto recibido.
        if letra in vocales:    # Verificamos si la letra actual es una vocal.
            conteo += 1         # Si lo es, aumentamos el contador local.
    return conteo               # 'return' entrega el total de vocales encontradas.

# Ejecutamos la función con "Hola Mundo" para probar si funciona.
print(contar_vocales("Hola Mundo"))  # Imprime: 4
