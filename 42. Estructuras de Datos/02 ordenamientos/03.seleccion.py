lista = [4, 2, 5, 1, 7, 8]
for i in range(len(lista)): # i = 0
    minimo = i             # minimo = 3
    for x in range(i, len(lista)):  # x = 5
        if lista[x] < lista[minimo]:    # 8 < 1
            minimo = x
    aux = lista[i]               # aux = 4
    lista[i] = lista[minimo]    #  lista[0] = lista[3]        en la posicion 0 va a quedar la posicion 3

                                                                                        # 0  1  2  3  4  5
    lista[minimo] = aux     # lista[3] = aux    en la posicion minima va a quedar el 4   [1, 2, 5, 4, 7, 8]

print(lista)