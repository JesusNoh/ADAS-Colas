class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            raise IndexError("La cola está vacía")

    def tamaño(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

def sumar_colas(cola_a, cola_b):
    cola_resultado = Cola()
    
    # Aseguramos que ambas colas tengan el mismo tamaño
    if cola_a.tamaño() != cola_b.tamaño():
        raise ValueError("Las colas deben tener el mismo tamaño para ser sumadas.")
    
    # Sumar los elementos de las colas uno a uno
    while not cola_a.esta_vacia() and not cola_b.esta_vacia():
        suma = cola_a.desencolar() + cola_b.desencolar()
        cola_resultado.encolar(suma)
    
    return cola_resultado

if __name__ == "__main__":
    # Crear las colas A y B
    cola_a = Cola()
    cola_b = Cola()

    # Agregar elementos a la Cola A
    cola_a.encolar(3)
    cola_a.encolar(4)
    cola_a.encolar(2)
    cola_a.encolar(8)
    cola_a.encolar(12)

    # Agregar elementos a la Cola B
    cola_b.encolar(6)
    cola_b.encolar(2)
    cola_b.encolar(9)
    cola_b.encolar(11)
    cola_b.encolar(3)

    # Almacenar los elementos en listas para imprimir después
    lista_a = []
    lista_b = []
    
    # Almacenar los elementos de las colas A y B en listas sin desencolarlas
    for item in cola_a.items:
        lista_a.append(item)

    for item in cola_b.items:
        lista_b.append(item)

    # Sumar las colas (creando nuevas instancias para no perder datos originales)
    resultado = sumar_colas(Cola(), Cola())  # Crear nuevas colas para sumar

    # Almacenar los resultados en una lista
    lista_resultado = []
    
    while not resultado.esta_vacia():
        lista_resultado.append(resultado.desencolar())

    # Mostrar resultado en formato tabular
    print(f"{'Cola A':<10} {'Cola B':<10} {'Cola Resultado':<15}")

    for i in range(len(lista_a)):
        a = lista_a[i]
        b = lista_b[i]
        r = a + b  # Calcular la suma directamente aquí
        
        print(f"{a:<10} {b:<10} {r:<15}")