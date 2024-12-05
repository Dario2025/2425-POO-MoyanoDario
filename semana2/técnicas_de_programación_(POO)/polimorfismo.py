class Appliance:
    """Clase base para electrodomésticos."""

    def turn_on(self):
        """Método genérico para encender un electrodoméstico."""
        print("El electrodoméstico está encendido.")


class WashingMachine(Appliance):
    """Clase que representa una lavadora."""

    def turn_on(self):
        print("La lavadora está ahora lavando ropa.")


class Refrigerator(Appliance):
    """Clase que representa un refrigerador."""

    def turn_on(self):
        print("El refrigerador está enfriando alimentos.")


# Uso
def use_appliance(appliance):
    """Función que enciende cualquier electrodoméstico."""
    appliance.turn_on()


appliances = [WashingMachine(), Refrigerator(), Appliance()]
for appliance in appliances:
    use_appliance(appliance)
