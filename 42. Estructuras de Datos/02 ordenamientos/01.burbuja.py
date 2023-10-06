lista = [100, 50, 20, 10, 8, 4, 2]

# no es recomendable  Método de burbuja
for i in range(len(lista)): # Evalúa las pasadas
    for x in range(len(lista) - 1): # Evalúa dentro de cada pasada
        if lista[x] > lista[x + 1]:
            lista[x], lista[x + 1] = lista[x + 1], lista[x]
