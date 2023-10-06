import json
"""
json_str = '{"nombre": "Oscar", "edad": 28, "pais": "Perú"}'
print(json_str)
print(type(json_str))

python_dict = json.loads(json_str)
print(python_dict)
print(type(python_dict))
print(python_dict["nombre"])
print(python_dict["edad"])
"""

"""
data = {
    "youtuber": "Gerardo",
    "nombre": "Oscar",
    "edad": 29,
    "cursos": ["PHP", "Python", "JavaScript", "C#", "Node.js"]
}
json_data = json.dumps(data, indent=4, separators=(", ", " : "), sort_keys=True)
print(json_data)
"""
json_data = json.JSONEncoder().encode({"lenguajes": ["Python", "JavaScript"]})
print(json_data)
print(type(json_data))

