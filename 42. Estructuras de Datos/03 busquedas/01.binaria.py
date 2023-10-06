def busqueda_binaria(lista: list, dato: int) -> int:
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == dato:
            return medio

        elif lista[medio] > dato:
            der = medio - 1

        else:
            izq = medio + 1
    return None

def main():
    lista = input("Ingrese números: ")
    try:
        lista_integer = [int(n) for n in lista.strip("[]").split(",")]
        lista_integer.sort()
        dato = int(input("Ingrese el valor a buscara: "))
        resultado = busqueda_binaria(lista_integer, dato)
        if resultado is not None:
            print(f"Número '{dato}' su índice en la lista es:", resultado)
        else:
            print("No se encontro resultado del dato a buscar.")
    except:
        print("Entrada inválida. Asegúrate de ingresar una lista ordenada correctamente.")

if __name__ == "__main__":
    main()

