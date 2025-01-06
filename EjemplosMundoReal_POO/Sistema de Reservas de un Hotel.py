# Clase base para una persona
class Persona:
    def __init__(self, nombre, email, telefono):
        """
        Clase que representa a una persona genérica.
        :param nombre: Nombre completo de la persona.
        :param email: Dirección de correo electrónico.
        :param telefono: Número de teléfono de contacto.
        """
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Email: {self.email}, Teléfono: {self.telefono}"


# Clase para un huésped
class Huesped(Persona):
    def __init__(self, nombre, email, telefono, dni):
        """
        Clase que representa a un huésped del hotel.
        :param dni: Documento Nacional de Identidad del huésped.
        """
        super().__init__(nombre, email, telefono)
        self.dni = dni

    def mostrar_informacion(self):
        return f"{super().mostrar_informacion()}, DNI: {self.dni}"


# Clase para una habitación del hotel
class Habitacion:
    def __init__(self, numero, tipo, precio_por_noche):
        """
        Clase que representa una habitación del hotel.
        :param numero: Número de la habitación.
        :param tipo: Tipo de habitación (e.g., "Simple", "Doble", "Suite").
        :param precio_por_noche: Precio por noche de la habitación.
        """
        self.numero = numero
        self.tipo = tipo
        self.precio_por_noche = precio_por_noche
        self.disponible = True

    def reservar(self):
        if self.disponible:
            self.disponible = False
            return True
        return False

    def liberar(self):
        self.disponible = True

    def mostrar_informacion(self):
        estado = "Disponible" if self.disponible else "Reservada"
        return f"Habitación {self.numero} ({self.tipo}) - Precio: ${self.precio_por_noche} - Estado: {estado}"


# Clase para gestionar una reserva
class Reserva:
    def __init__(self, huesped, habitacion, noches):
        """
        Clase que representa una reserva en el hotel.
        :param huesped: Objeto Huesped que realiza la reserva.
        :param habitacion: Objeto Habitacion reservada.
        :param noches: Número de noches que se hospedará.
        """
        self.huesped = huesped
        self.habitacion = habitacion
        self.noches = noches
        self.total = self.calcular_total()

    def calcular_total(self):
        return self.habitacion.precio_por_noche * self.noches

    def mostrar_detalles(self):
        return (f"Reserva de {self.huesped.nombre} para la habitación {self.habitacion.numero} "
                f"({self.habitacion.tipo}) por {self.noches} noche(s). Total: ${self.total}")


# Clase para el Hotel Madison
class HotelMadison:
    def __init__(self, nombre):
        """
        Clase que representa el hotel.
        :param nombre: Nombre del hotel.
        """
        self.nombre = nombre
        self.habitaciones = []
        self.reservas = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones_disponibles(self):
        disponibles = [hab.mostrar_informacion() for hab in self.habitaciones if hab.disponible]
        return "\n".join(disponibles) if disponibles else "No hay habitaciones disponibles."

    def realizar_reserva(self, huesped, numero_habitacion, noches):
        for habitacion in self.habitaciones:
            if habitacion.numero == numero_habitacion and habitacion.disponible:
                if habitacion.reservar():
                    reserva = Reserva(huesped, habitacion, noches)
                    self.reservas.append(reserva)
                    return reserva.mostrar_detalles()
        return "La habitación seleccionada no está disponible."


# Pruebas del sistema
if __name__ == "__main__":
    # Crear el hotel
    hotel = HotelMadison("Hotel Madison")

    # Agregar habitaciones
    hotel.agregar_habitacion(Habitacion(101, "Simple", 50))
    hotel.agregar_habitacion(Habitacion(102, "Doble", 80))
    hotel.agregar_habitacion(Habitacion(103, "Suite", 150))

    # Mostrar habitaciones disponibles
    print("Habitaciones disponibles:")
    print(hotel.mostrar_habitaciones_disponibles())

    # Crear un huésped
    huesped1 = Huesped("Dario Moyano", "dario@gmail.com", "123456789", "DNI123456")

    # Realizar una reserva
    print("\nRealizando una reserva...")
    print(hotel.realizar_reserva(huesped1, 102, 3))

    # Mostrar habitaciones disponibles después de la reserva
    print("\nHabitaciones disponibles después de la reserva:")
    print(hotel.mostrar_habitaciones_disponibles())
