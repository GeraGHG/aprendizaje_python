"""
    Escriba un programa que contenga dos listas, a continuación cree las
    siguientes listas donde no debe haber datos repetidos.

        *Lista de palabras que aparecen en las dos listas
        *Lista de palabras que aparecen en solo la primera lista
        *Lista de palabras que aparecen en solo la segunda lista
        *Lista de palabras que aparecen en ambas listas
"""

def agregar_elementos():
    lista = list()
    while True:
        cantidad = input("¿Cuántos elementos desea agregar a la lista? ")
        if cantidad.isdigit():
            cantidad = int(cantidad)
            if 0 < cantidad < 51:
                for i in range(cantidad):
                    lista.append(input(f"Ingrese el dato {i + 1}: "))
                return lista
            return []
        else:
            print("Por favor ingrese un carácter númerico")




while True:
    print("¿A cuál lista deseas agregarle elementos (lista1 o lista2)? o presione 'q' para salir.")
    print("'1' lista1\n'2' lista2\n")
    lista_opcion = input("Ingrese su opción: ")
    if lista_opcion == "q":
        print("--- Bye ---")
        break
    elif lista_opcion == "1":
        lista1 = agregar_elementos()
        print("Los elementos agregados son", lista1)
    elif lista_opcion == "2":
        lista2 = agregar_elementos()
        print("Los elementos agregados son", lista2)
    else:
        print("La opción ingresada no es valída.")

lista1_set = set(lista1)
lista2_set = set(lista2)

union = list(lista1_set | lista2_set)
print("Todos los elementos que aparecen en ambas listas", union)

diferencia_lista1_lista2 = list(lista1_set - lista2_set)
print("Elementos que aparecen en la lista1 pero no en la lista2", diferencia_lista1_lista2)

diferencia_lista2_lista1 = list(lista2_set - lista1_set)
print("Elementos que aparecen en la lista2 pero no en la lista1", diferencia_lista2_lista1)

interseccion = list(lista1_set & lista2_set)
print("La interseción de la lista1 y la lista2", interseccion)



