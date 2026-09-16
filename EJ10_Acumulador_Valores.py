# Función externa que sirve como plantilla para crear acumuladores.
def crear_acumulador():
    total = 0  # Variable de la función externa donde se guardará la suma.

    # Función interna que recibe un valor y lo acumula.
    def acumular(valor):
        nonlocal total  # Usamos 'nonlocal' para alterar la variable 'total' de la función superior.
        total += valor  # Suma el nuevo 'valor' al 'total' actual.
        return total    # Devuelve el valor acumulado.

    return acumular  # Retorna la función 'acumular'.

suma = crear_acumulador()  # Asignamos la función acumuladora a la variable 'suma'.
print(suma(10))            # Suma 10 al total original (0) -> Imprime: 10
print(suma(5))             # Suma 5 al total que ya era 10 -> Imprime: 15