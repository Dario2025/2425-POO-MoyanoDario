# Clase base
class Libro:
    def __init__(self, titulo, autor, anio_publicacion):
        self.__titulo = titulo  # Atributo privado
        self.__autor = autor    # Atributo privado
        self.__anio_publicacion = anio_publicacion  # Atributo privado

    # Métodos para obtener información del libro
    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_anio_publicacion(self):
        return self.__anio_publicacion

    # Método que será sobrescrito en la clase derivada
    def descripcion(self):
        raise NotImplementedError("Este método debe ser sobrescrito en la clase derivada")

# Clase derivada para libros de ficción
class LibroFiccion(Libro):
    def __init__(self, titulo, autor, anio_publicacion, genero):
        super().__init__(titulo, autor, anio_publicacion)  # Llamada al constructor de la clase base
        self.__genero = genero  # Atributo privado

    # Método sobrescrito
    def descripcion(self):
        return f"{self.get_titulo()} es una novela de {self.__genero} escrita por {self.get_autor()} en {self.get_anio_publicacion()}."

# Clase derivada para libros de no ficción
class LibroNoFiccion(Libro):
    def __init__(self, titulo, autor, anio_publicacion, tema):
        super().__init__(titulo, autor, anio_publicacion)  # Llamada al constructor de la clase base
        self.__tema = tema  # Atributo privado

    # Método sobrescrito
    def descripcion(self):
        return f"{self.get_titulo()} es un libro de no ficción sobre {self.__tema}, escrito por {self.get_autor()} en {self.get_anio_publicacion()}."

# Función para mostrar la descripción del libro
def mostrar_descripcion(libro):
    print(libro.descripcion())

# Creación de instancias de las clases con los nuevos libros
libro1 = LibroNoFiccion("Hábitos Atómicos", "James Clear", 2020, "mejora personal y hábitos")
libro2 = LibroFiccion("Alas de Hierro", "Rebecca Yarros", 2024, "romance y drama")

# Uso de los métodos
mostrar_descripcion(libro1)  # Salida: Hábitos Atómicos es un libro de no ficción sobre mejora personal y hábitos, escrito por James Clear en 2020.
mostrar_descripcion(libro2)  # Salida: Alas de Hierro es una novela de romance y drama escrita por Rebecca Yarros en 2024.