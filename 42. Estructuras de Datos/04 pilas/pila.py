class Pila:
    def __init__(self, size):
        self.lista = []
        self.tope = 0
        self.size = size

    def empty(self):
        if self.tope == 0:
            return True
        return False

    def push(self, dato):
        if self.tope < self.size:
            self.lista.append(dato)
            self.tope += 1
        else:
            self.size += 5
            self.lista.append(dato)
            self.tope += 1

    def pop(self):
        if self.empty():
            print("La pila está vacía no puedes eliminar ningun dato.")
        else:
            self.tope -= 1
            self.lista = [self.lista[x] for x in range(self.tope)]

    def show(self):
        i = self.tope - 1
        while i > -1:
            print(f"{i} => {self.lista[i]}")
            i -= 1

    def top(self):
        return self.lista[-1]

if __name__ == "__main__":
    opcion = 0
    pila = Pila(5)
    while opcion != 7:
        print("--- Pilas ---\n 1. Agregar dato\n 2. Eliminar\n 3. ¿Está vacía la pila?\n 4. Mostrar la pila\n 5. Mostrar la cima de la pila\n 6. Salir")
        opcion = int(input("Ingrese una opción: "))
        match opcion:
            case 1:
                dato = int(input("Ingrese un número: "))
                pila.push(dato)
            case 2:
                pila.pop()
            case 3:
                if pila.empty():
                    print("La pila está vacia")
                else:
                    print("La pila \"no\" está vacia")
            case 4:
                pila.show()
            case 5:
                print("El top de la pila es", pila.top())
            case 6:
                break
            case _:
                print("Opción invalida")
