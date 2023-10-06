import requests
import json

# Hacemos un pedido a la página de wikipedia
URL = 'https://es.wikipedia.org/'

# Guardamos el objeto que nos devuelve
respuesta = requests.get(URL)

# print(f'Tipo de Objeto: {type(respuesta)} \n')
# print(f'Código de estado: {respuesta.status_code} \n')
# print(f'Data: {respuesta.text} \n')


### Pedir una API
# Definimos los parametros de nuestra query
latitud = -34.6
longitud = -58.4
fecha = '1816-07-09' # AAAA-MM-DD

# Hacemos el pedido y guardamos la respuesta en una nueva variable
respuesta_sunset = requests.get(f'https://api.sunrise-sunset.org/json?lat={latitud}&lng={longitud}&date={fecha}')
type(respuesta_sunset)

# Para des-serializar el objeto (que era tipo 'HTTPResponse') y cargarlo como json
datos_sunset = respuesta_sunset.json()
# print(datos_sunset)
# print(type(datos_sunset))
# print(datos_sunset.keys())

sunset_status = datos_sunset["status"]
# print(f"Status: {sunset_status}")

# Podemos ver su contenido ya que son diccionarios anidados
sunset = datos_sunset["results"]["sunset"]
# print(f"El {fecha} el sol se ocultó a las {sunset} (UTF)")

# for element in datos_sunset["results"]:
    #print(element)


## Forma correcta de importar
from bs4 import BeautifulSoup
import bs4
import requests
# print("Versión de BeautifulSoup", bs4.__version__)
# print("Versión de requuest:", requests.__version__

# Empezamos el scraping

# 1. Obtener el HTML
URL_BASE = 'https://scrapepark.org/courses/spanish/'
pedido_obtenido = requests.get(URL_BASE)
html_obtenido = pedido_obtenido.text
# print(html_obtenido)

# 2. "Parsear" ese HTML
soup = BeautifulSoup(html_obtenido, "html.parser")
# print(type(soup))

# El método find()
primer_h2 = soup.find("h2")
# print(primer_h2) # <h2>¿Por qué comprar con nosotros?</h2>
# Solo el texto
# print(primer_h2.text)  # ¿Por qué comprar con nosotros?
# print(soup.h2.text)

# El método find_all()
h2_todos = soup.find_all('h2')
list_h2 = [seccion.text for seccion in h2_todos]
#print(list_h2)

# Podemos iterar sobre el objeto
#for seccion in list_h2:
    #print(seccion)

h2_uno_solo = soup.find_all('h2', limit=1)
#print(h2_uno_solo)

# get_text() para más funcionalidades es más concurrido las oraciones
#for elem in h2_todos:
  #print(elem.get_text(strip=True))



# Clase
divs = soup.find_all('div', class_ = "heading-container heading-center")

#for div in divs:
  #print(div)
  #print(" ")

# Todas las etiquetas que tengan el atributo "src"
src_todos = soup.find_all(src=True)
for elemento in src_todos:
    if elemento["src"].endswith(".jpg"):
        print(elemento)

#@title Ejercicio: Bajar todas las imagenes!
url_imagenes = []
# for i, imagen in enumerate(src_todos):
  # if imagen['src'].endswith('png'):
    # print(imagen['src'])
    # r = requests.get(f"https://scrapepark.org/courses/spanish/{imagen['src']}")
    # with open(f'imagen_{i}.png', 'wb') as f:
      # f.write(r.content)







