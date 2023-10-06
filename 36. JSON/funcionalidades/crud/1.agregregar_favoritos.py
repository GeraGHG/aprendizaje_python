import json
import os

def add_favorito():
    lista = list()
    diccionario = {}
    titulo = input("\Ingrese el título: ")
    url = input("Ingrese la URL: ")
    comentario = input("Ingresa el comentario: ")

    # Agregando la URL y el comentario a la lista
    lista.append(url)
    lista.append(comentario)

    filename = r"36.JSON/funcionalidades/crud/1.agregregar_favoritos.json"
    if os.path.isfile(filename):
        archivo = open("1.agregregar_favoritos.py", "r")
        datos = json.load(archivo)
        archivo.close()

        datos[titulo] = lista

        archivo = open("favoritos.json", "w")
        json.dump(datos, archivo)
        archivo.close()
    else:
        archivo = open("favoritos.json", "w")

        # Agregando el favorito en el archivo
        diccionario[titulo] = lista

        # Escribiendo los datos en el archivo
        json.dump(diccionario, archivo)
        archivo.close()


