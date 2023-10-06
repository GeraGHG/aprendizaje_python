class Nodo:
    def __init__(self, valor = None, padre = None, es_raiz = False, es_izquierda = False, es_derecha = False):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.padre = padre
        self.es_raiz = es_raiz
        self.es_izquierda = es_izquierda
        self.es_derecha = es_derecha

class arbol_binario_busqueda:
    def __init__(self):
        self.raiz = None

    def vacia(self):
        return not self.raiz

    def agregar(self, valor):
        if self.vacia():
            self.raiz = Nodo(valor = valor, es_raiz = True)
        else:
            nodo = self.__obtener_lugar(valor)
            if valor <= nodo.valor:
                nodo.izquierda = Nodo(valor = valor, padre = nodo, es_izquierdo = True)
            else:
                nodo.derecha = Nodo(valor = valor, padre = nodo, es_derecha = True)