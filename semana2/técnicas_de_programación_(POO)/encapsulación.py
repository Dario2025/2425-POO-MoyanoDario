class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  # Atributo privado

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad

    def obtener_saldo(self):
        return self.__saldo

# Uso
cuenta = CuentaBancaria(1000)
cuenta.depositar(5000)
print(cuenta.obtener_saldo())  # Salida: 1500
cuenta.retirar(1900)
print(cuenta.obtener_saldo())  # Salida: 1300