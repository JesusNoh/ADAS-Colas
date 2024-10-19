class Cola:
    def __init__(self):
        self.cola = []

    def agregar(self, cliente):
        self.cola.append(cliente)

    def atender(self):
        if not self.cola:
            return None
        return self.cola.pop(0)

    def esta_vacia(self):
        return len(self.cola) == 0

    def __str__(self):
        return ', '.join(self.cola)


class SistemaColas:
    def __init__(self):
        self.colas = {
            '1': Cola(),  # Cola para servicio 1
            '2': Cola(),  # Cola para servicio 2
            '3': Cola()   # Cola para servicio 3
        }

    def agregar_cliente(self, numero_servicio):
        if numero_servicio in self.colas:
            cliente_id = f"C{len(self.colas[numero_servicio].cola) + 1}"
            self.colas[numero_servicio].agregar(cliente_id)
            print(f"Cliente {cliente_id} agregado a la cola {numero_servicio}.")
        else:
            print("Número de servicio no válido.")

    def atender_cliente(self, numero_servicio):
        if numero_servicio in self.colas:
            cliente_atendido = self.colas[numero_servicio].atender()
            if cliente_atendido:
                print(f"Atendiendo al cliente: {cliente_atendido} de la cola {numero_servicio}.")
            else:
                print(f"No hay clientes en la cola {numero_servicio}.")
        else:
            print("Número de servicio no válido.")

    def mostrar_colas(self):
        for numero, cola in self.colas.items():
            print(f"Cola {numero}: {cola}")


def main():
    sistema = SistemaColas()
    
    while True:
        # Preguntar al usuario si desea agregar o atender un cliente
        accion = input("¿Desea (C)gregar un cliente o (A) atender un cliente? (Q para salir): ").upper()
        
        if accion == 'C':
            numero_servicio = input("Ingrese el número de servicio para agregar el cliente (1, 2 o 3): ")
            sistema.agregar_cliente(numero_servicio)
        
        elif accion == 'A':
            numero_servicio = input("Ingrese el número de servicio para atender al cliente (1, 2 o 3): ")
            sistema.atender_cliente(numero_servicio)
        
        elif accion == 'Q':
            print("Saliendo del sistema.")
            break
        
        else:
            print("Opción no reconocida. Intente nuevamente.")
        
        # Mostrar el estado actual de las colas después de cada acción
        sistema.mostrar_colas()


if __name__ == "__main__":
    main()