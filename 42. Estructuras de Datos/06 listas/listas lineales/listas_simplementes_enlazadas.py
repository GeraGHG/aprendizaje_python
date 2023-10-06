class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Lista_enlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0

    def vacia(self):
        return self.cabeza is None  # Usar 'is' en lugar de '==' para comprobar None

    def agregar_ultimo(self, dato):
        nodo = Nodo(dato)
        if self.vacia():
            self.cabeza = self.cola = nodo
        else:
            aux = self.cola
            self.cola = aux.siguiente = nodo

    def recorrido(self):
        aux = self.primero
        while aux is not None:  # Usar 'is not' en lugar de '!=' para comprobar None
            print(aux.dato)
            aux = aux.siguiente

    def eliminar_ultimo(self):
        if self.vacia():
            print("La lista está vacía, no puedes eliminar el último elemento.")
            return

        if self.primero == self.ultimo:
            self.primero = self.ultimo = None
            return

        aux = self.primero
        while aux.siguiente != self.ultimo:
            aux = aux.siguiente
        aux.siguiente = None
        self.ultimo = aux

    def agregar_inicio(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero = aux

    def eliminar_inicio(self):
        if self.vacia():
            print("La lista está vacía, no puedes eliminar el primer elemento.")
            return

        if self.primero == self.ultimo:
            self.primero = self.ultimo = None
            return

        self.primero = self.primero.siguiente

