import json
import os

def add_favorito():
    lista = list()
    diccionarios = {}
    titulo = input("\Ingrese el título: ")
    url = input("Ingrese la URL: ")
    comentario = input("Ingresa el comentario: ")

    # Agregando la URL y el comentario a la lista
    lista.append(url)
    lista.append(comentario)