arreglo = [11, 65, 23, 3, 4, 5, 6, 77, 123, 54, 23, 90, 0]
def busqueda_lineal(dato, global: arreglo):
    for i in range(len(arreglo)):
        if arreglo[i] == dato:
            return i
    return None

def buscar(dato):
    if busqueda_lineal(dato) == None:
        return f"El dato {dato} no se encontroó en el arreglo"
    else:
        return f"El dato {dato} se encontró en el índice {busqueda_lineal(dato)}"