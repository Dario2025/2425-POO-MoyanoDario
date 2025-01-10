# Programa para convertir el peso de una persona de libras a kilogramos.
# El usuario ingresa su peso en libras, y el programa realiza la conversión.

def convertir_libras_a_kilogramos(peso_libras: float) -> float:
    """
    Convierte el peso de libras a kilogramos.
    :param peso_libras: Peso en libras (float).
    :return: Peso en kilogramos (float).
    """
    return peso_libras * 0.453592


# Solicitar el peso en libras al usuario
peso_libras = float(input("Ingrese su peso en libras: "))

# Convertir a kilogramos
peso_kilogramos = convertir_libras_a_kilogramos(peso_libras)

# Mostrar el resultado
print(f"Su peso en libras es {peso_libras:.2f} lb.")
print(f"Su peso en kilogramos es {peso_kilogramos:.2f} kg.")

# Verificación adicional (booleano)
es_peso_valido = peso_libras > 0
print(f"¿El peso ingresado es válido? {es_peso_valido}")
