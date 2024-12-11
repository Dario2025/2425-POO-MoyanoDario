# Programación Orientada a Objetos (POO): Cálculo del promedio semanal del clima

class Clima:
    """
    Clase que representa la información diaria del clima.
    """

    def __init__(self):
        """
        Inicializar la lista de temperaturas diarias.
        """
        self.temperaturas_diarias = []

    def ingresar_datos_diarios(self):
        """
        Ingresar temperaturas diarias para el cálculo del promedio semanal.
        """
        for dia in range(7):
            temperatura = float(input(f"Ingrese la temperatura del día {dia + 1}: "))
            self.temperaturas_diarias.append(temperatura)

    def calcular_promedio_semanal(self):
        """
        Calcular el promedio semanal de las temperaturas diarias.

        Retorna:
            float: Promedio semanal de las temperaturas.
        """
        return sum(self.temperaturas_diarias) / len(self.temperaturas_diarias)

    def mostrar_resultado(self):
        """
        Mostrar el resultado del cálculo del promedio semanal.
        """
        promedio_semanal = self.calcular_promedio_semanal()
        print(f"El promedio semanal de las temperaturas es: {promedio_semanal:.2f}°C")


# Función principal
def main():
    print("Cálculo del promedio semanal del clima")
    clima = Clima()
    clima.ingresar_datos_diarios()
    clima.mostrar_resultado()


if __name__ == "__main__":
    main()