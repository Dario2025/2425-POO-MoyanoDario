class Animal:
    """Clase base que representa un animal."""

    def __init__(self, nombre):
        """Inicializa el animal con un nombre."""
        self.nombre = nombre

    def hacer_sonido(self):
        """Método que debe ser implementado por las subclases."""
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

class Perro(Animal):
    """Clase que representa un perro, que hereda de Animal."""

    def hacer_sonido(self):
        """Implementación del método hacer_sonido para un perro."""
        return "Guau!"

class Gato(Animal):
    """Clase que representa un gato, que hereda de Animal."""

    def hacer_sonido(self):
        """Implementación del método hacer_sonido para un gato."""
        return "Miau!"

# Ejemplo de uso
animales = [Perro("Max"), Gato("Garfiel")]
for animal in animales:
    print(f"{animal.nombre} dice: {animal.hacer_sonido()}")