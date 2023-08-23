with open("obama.txt", "r") as f:
    lines = f.readlines()
    suma_lineas = sum(1 for line in lines if len(line.strip()) != 0)
    suma_total_words = 0
    for line in lines:
        lista_linea = line.split()
        suma_total_words += len(lista_linea)
    print(suma_lineas, suma_total_words)

with open("obama.txt", "r") as f:
    lines = f.readlines()
    suma_lineas = sum(1 for line in lines if len(line.strip()) != 0)

    suma_total_words = 0
    for line in lines:
        lista_linea = line.split()
        suma_total_words += len(lista_linea)

print("Total non-empty lines:", suma_lineas)
print("Total words in non-empty lines:", suma_total_words)


