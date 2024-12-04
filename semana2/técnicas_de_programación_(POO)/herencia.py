class Animal:
    def hacer_sonido(self):
        return "Sonido de animal"

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

# Uso
perro = Perro()
gato = Gato()
print(perro.hacer_sonido())  # Salida: Guau
print(gato.hacer_sonido())    # Salida: Miau