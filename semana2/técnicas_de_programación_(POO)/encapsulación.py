class WaterBottle:
    """
    Clase que representa una botella de agua.
    Protege el nivel de agua mediante encapsulación.
    """

    def __init__(self, capacity):
        self.__capacity = capacity  # Capacidad máxima (privado)
        self.__current_level = 0  # Nivel actual de agua (privado)

    def fill(self, amount):
        """Llena la botella con una cantidad específica de agua."""
        if amount > 0:
            self.__current_level = min(self.__capacity, self.__current_level + amount)
            print(f"La botella tiene ahora {self.__current_level} ml de agua.")
        else:
            print("La cantidad debe ser positiva.")

    def drink(self, amount):
        """Bebe una cantidad específica de agua."""
        if 0 < amount <= self.__current_level:
            self.__current_level -= amount
            print(f"Bebiste {amount} ml. Quedan {self.__current_level} ml.")
        else:
            print("No hay suficiente agua o la cantidad es inválida.")


# Uso
bottle = WaterBottle(1000)
bottle.fill(500)
bottle.drink(200)
