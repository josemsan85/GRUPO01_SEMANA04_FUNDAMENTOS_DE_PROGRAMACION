visitas = 0  # Variable global: creada fuera de cualquier función.

def registrar_visita():
    global visitas  # 'global' le dice a Python que modifique la variable 'visitas' de afuera.
    visitas += 1    # Le suma 1 al contador global cada vez que se llama a la función.
    
    # La 'f' antes de las comillas (f-string) permite meter variables directo en el texto entre {}.
    print(f"Visita #{visitas} registrada")

# Llamamos a la función dos veces para incrementar el contador global.
registrar_visita()  # Imprime: Visita #1 registrada
registrar_visita()  # Imprime: Visita #2 registrada

# Imprime el valor final que le quedó a la variable global.
print(f"Total: {visitas}")  # Imprime: Total: 2