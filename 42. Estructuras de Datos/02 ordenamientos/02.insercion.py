# Más eficiente el método de inserción
lista = [5, 10, 3, 12, 10, 6]
for i in range(1, len(lista)): # i = 2
    aux = lista[i] # aux = 3
    j = i - 1       # j = 1
    while j >= 0 and aux < lista[j]:
        lista[j + 1] = lista[j]
        lista[j] = aux
        j -= 1
print(lista)


def insercion_sort(lista):
    for i in range(1, len(lista)):
        valor_actual = lista[i]   # 11
        posicion = i    # 1
        while posicion > 0 and valor_actual < lista[posicion - 1]:
            lista[posicion] = lista[posicion - 1]
            posicion -= 1
        lista[posicion] = valor_actual


lista_desordenada = [12, 11, 13, 5, 6]
insercion_sort(lista_desordenada)
print("Lista ordenada:", lista_desordenada)
