"""
Cree un script en python, en el cual genere un json con dos diferentes razas para un video juego,
las razas son: HUMANOS y ORCOS.

Los HUMANOS tienen diferentes roles de batalla (Guerrero, Jinete, Mago, Recolector y Observador) y los
ORCOS cuentan con (Guerrero, Chamán y Jinete); cada uno de estos cuenta con un nivel de vida, id, ataque,
defensa y poder mágico.
"""

raza = {
    "HUMANOS":  [
        {
            "Guerrero": {
                "vida": 150,
                "id": 123,
                "ataque": 45,
                "defensa": 34,
                "poder mágico": 0
            }
        },
        {
            "Jinete": {
                "vida": 150,
                "id": 345,
                "ataque": 58,
                "defensa": 70,
                "poder mágico": 15
            }
        },
        {
            "Mago": {
                "vida": 100,
                "id": 234,
                "ataque": 67,
                "defensa": 23,
                "poder mágico": 100
            }
        },
        {
            "observador": {
                "vida": 120,
                "id": 877,
                "ataque": 0,
                "defensa": 90,
                "poder mágico": 40
            }
        }
    ],
    "ORCOS": [
        {
            "Guerrero": {
                "vida": 150,
                "id": 123,
                "ataque": 45,
                "defensa": 34,
                "poder mágico": 0
            }
        },
        {
            "Chama": {
                "vida": 60,
                "id": 111,
                "ataque": 37,
                "defensa": 12,
                "poder mágico": 10
            }
        },
        {
            "Jinete": {
                "vida": 160,
                "id": 143,
                "ataque": 55,
                "defensa": 44,
                "poder mágico": 10
            }
        }
    ]

}

"""
import json

# Convertir un diccionario en una cadena JSON
json_string = json.dumps(data)

# Convertir una cadena JSON en un diccionario
parsed_data = json.loads(json_string)

"""