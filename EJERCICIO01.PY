def contar_vocales(texto):
    vocales = "aeiouAEIOU"
    conteo = 0 # local
    for letra in texto:
        if letra in vocales:
            conteo += 1
    return conteo
print(contar_vocales("parangaricutirimiacuaro")) # 4
#En el ejercicio se cuantan las volaceles del texto solicitado mediante la funcion contar_vocales