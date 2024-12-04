class Ave:
    def volar(self):
        return "El ave vuela"

class Murcielago:
    def volar(self):
        return "El murciélago vuela"

def hacer_volar(ave):
    print(ave.volar())

# Uso
pajaro = Ave()
murcielago = Murcielago()
hacer_volar(pajaro)      # Salida: El ave vuela
hacer_volar(murcielago)  # Salida: El murciélago vuela