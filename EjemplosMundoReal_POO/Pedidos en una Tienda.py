# Clase para representar un producto
class Producto:
    def __init__(self, nombre, precio, stock):
        """
        Representa un producto con nombre, precio y stock disponible.
        """
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def reducir_stock(self, cantidad):
        """
        Reduce el stock del producto si hay suficiente cantidad.
        """
        if cantidad <= self.stock:
            self.stock -= cantidad
            return True
        return False

# Clase para representar un cliente
class Cliente:
    def __init__(self, nombre):
        """
        Representa un cliente con un nombre.
        """
        self.nombre = nombre

# Clase para representar un pedido
class Pedido:
    def __init__(self, cliente):
        """
        Representa un pedido realizado por un cliente.
        """
        self.cliente = cliente
        self.items = []
        self.total = 0

    def agregar_producto(self, producto, cantidad):
        """
        Agrega un producto al pedido si hay stock suficiente.
        """
        if producto.reducir_stock(cantidad):
            self.items.append((producto.nombre, cantidad, producto.precio * cantidad))
            self.total += producto.precio * cantidad
        else:
            print(f"No hay suficiente stock de {producto.nombre}.")

    def mostrar_pedido(self):
        """
        Muestra los detalles del pedido.
        """
        print(f"Pedido de {self.cliente.nombre}:")
        for item in self.items:
            print(f"- {item[0]} x{item[1]} = ${item[2]}")
        print(f"Total: ${self.total}")

# Pruebas del sistema
if __name__ == "__main__":
    # Crear productos
    laptop = Producto("Laptop MacBook Pro", 1599, 5)
    auriculares = Producto("Airpods Max", 679, 20)

    # Crear cliente
    cliente = Cliente("Dario Moyano")

    # Crear pedido
    pedido = Pedido(cliente)

    # Agregar productos al pedido
    pedido.agregar_producto(laptop, 2)  # Laptop x2
    pedido.agregar_producto(auriculares, 3)  # Auriculares x3

    # Mostrar detalles del pedido
    pedido.mostrar_pedido()
