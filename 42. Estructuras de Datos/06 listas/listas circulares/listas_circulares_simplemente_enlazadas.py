class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class lista_circular_simplemente_enlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
        return not self.primero

    def agregar_inicio(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            





