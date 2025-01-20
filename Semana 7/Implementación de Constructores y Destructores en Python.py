class Libro:
    def __init__(self, titulo, autor):
        """
        Constructor de la clase Libro.

        :param titulo: Título del libro.
        :param autor: Autor del libro.
        """
        self.titulo = titulo
        self.autor = autor
        print(f"Libro '{self.titulo}' de {self.autor} ha sido creado.")

    def __del__(self):
        """
        Destructor de la clase Libro.
        Se llama cuando un objeto de la clase Libro es destruido.
        """
        print(f"Libro '{self.titulo}' de {self.autor} ha sido destruido.")


# Ejemplo de uso de la clase Libro
if __name__ == "__main__":
    # Creando objetos de la clase Libro con los títulos solicitados
    libro1 = Libro("Alas de ónix", "Cristina López Barrio")
    libro2 = Libro("48 leyes del poder", "Robert Greene")
    libro3 = Libro("El príncipe cruel", "Holly Black")
    libro4 = Libro("Fuego y sangre", "George R. R. Martin")

    # Eliminando los objetos manualmente
    del libro1
    del libro2
    del libro3
    del libro4


    # Para demostrar que el destructor se llama automáticamente,
    # podemos crear un objeto dentro de un bloque de código
    # y dejar que se destruya al salir del bloque.
    def crear_libro_temporal():
        libro_temporal = Libro("El Principito", "Antoine de Saint-Exupéry")


    crear_libro_temporal()