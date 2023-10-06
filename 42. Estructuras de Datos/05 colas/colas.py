class Cola:
    def __init__(self):
        self.cola = []
        self.size = 0

    def empty(self):
        return not self.cola

    def push(self, dato):
        self.cola.append(dato)
        self.size += 1

    def pop(self):
        if self.empty():
            print("La cola está vacía no puedes eliminar ningún dato")
        else:
            self.cola.pop(0)
            self.size -= 1

    def show(self):
        for i in range(self.size - 1, -1, -1):
            print(f"[{i}] => {self.cola[i]}")

    def front(self):
        print("La cola está vacía no puedes mostrar ningún dato") if self.empty() else print("Primer dato", self.cola[0])


    # [1, 2, 3, 4, 5]


if __name__ == "__main__":
    cola = Cola()
    while True:
        print("\n--- Colas ---\n 1. Agregar dato\n 2. Elimninar dato\n 3. Mostrar cola\n 4. Primer elemento de la cola\n 5. Salir\n")
        opcion = int(input("Ingrese una opción: "))
        match opcion:
            case 1:
                dato = int(input("Ingrese un dato: "))
                cola.push(dato)
            case 2:
                cola.pop()
            case 3:
                cola.show()
            case 4:
                cola.front()
            case 5:
                print("¡¡Gracias por usar el programa!! :)")
                break
            case _:
                print("La opción ingresda es invalida")
