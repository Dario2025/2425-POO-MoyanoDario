from abc import ABC, abstractmethod

class Vehiculo(ABC):
    @abstractmethod
    def conducir(self):
        pass

class Coche(Vehiculo):
    def conducir(self):
        return "Conduciendo un coche"

class Bicicleta(Vehiculo):
    def conducir(self):
        return "Conduciendo una bicicleta"

# Uso
vehiculo1 = Coche()
vehiculo2 = Bicicleta()
print(vehiculo1.conducir())  # Salida: Conduciendo un coche
print(vehiculo2.conducir())  # Salida: Conduciendo una bicicleta