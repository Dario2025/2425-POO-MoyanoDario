# Programación Tradicional: Cálculo del promedio semanal del clima

# Función para ingresar datos diarios (temperaturas)
def ingresar_datos_diarios():
    """
    Ingresar temperaturas diarias para el cálculo del promedio semanal.

    Retorna:
        list: Lista de temperaturas diarias.
    """
    temperaturas_diarias = []
    for dia in range(7):
        temperatura = float(input(f"Ingrese la temperatura del día {dia + 1}: "))
        temperaturas_diarias.append(temperatura)
    return temperaturas_diarias


# Función para calcular el promedio semanal
def calcular_promedio_semanal(temperaturas_diarias):
    """
    Calcular el promedio semanal de las temperaturas diarias.

    Parámetros:
        temperaturas_diarias (list): Lista de temperaturas diarias.

    Retorna:
        float: Promedio semanal de las temperaturas.
    """
    return sum(temperaturas_diarias) / len(temperaturas_diarias)


# Función principal
def main():
    print("Cálculo del promedio semanal del clima")
    temperaturas_diarias = ingresar_datos_diarios()
    promedio_semanal = calcular_promedio_semanal(temperaturas_diarias)
    print(f"El promedio semanal de las temperaturas es: {promedio_semanal:.2f}°C")


if __name__ == "__main__":
    main()