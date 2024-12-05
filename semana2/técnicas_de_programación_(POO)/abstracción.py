from abc import ABC, abstractmethod

class Vehiculo(ABC):
    """Clase abstracta que representa un vehículo."""

    @abstractmethod
    def conducir(self):
        """Método abstracto que debe ser implementado por las subclases."""
        pass

class Coche(Vehiculo):
    """Clase que representa un coche, que es un tipo de vehículo."""

    def conducir(self):
        """Implementación del método conducir para un coche."""
        return "Conduciendo un coche."

class Bicicleta(Vehiculo):
    """Clase que representa una bicicleta, que es un tipo de vehículo."""

    def conducir(self):
        """Implementación del método conducir para una bicicleta."""
        return "Conduciendo una bicicleta."

# Ejemplo de uso
vehiculos = [Coche(), Bicicleta()]
for vehiculo in vehiculos:
    print(vehiculo.conducir())