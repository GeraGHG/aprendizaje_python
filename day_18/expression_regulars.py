import re
# 1. match
texto = '''Hola Mundo.
Me gusta Python!!!!!
Mi primer número de la suerte es 987-654-321
Mi segundo número de la suerte es 876-543-210
Mi tercero número de la suerte es 765-432-100
Mi cuarto número de la suerte es 123-456-123-123-456
'''

# match(substring, string, re.T) si no hay coincidencia return None
#print(re.match("Hola", texto, re.T))

# buscar el primer emparejamiento
# print(re.search(r"", texto))

# buscar todos los emparejamientos
# print(re.findall(r"\s", texto))


# print(re.search(r"^Hola", texto))
# print(re.search(r"Mundo.$", texto, flags=re.M))

# +     (1 o mas)
# print(re.search(r"Python!+", texto))
# *     (0 o mas)
# print(re.search(r"Python!*", texto))
# ?     (0 o 1)
# print(re.search(r"Python!?", texto))

# {3}   (busqueda exacta)
# print(re.search(r"Python!{2}", texto))   re.Match object; span=(21, 29), match='Python!!'
# {2,}  (tomas cualquier número o mas)
# print(re.search(r"Python!{2,}", texto))    <re.Match object; span=(21, 32), match='Python!!!!!'>
# {2, 3} (rango entre un número a otro, da el valor más largo en este caso 3)
# print(re.search(r"Python!{3,4}", texto))  <re.Match object; span=(21, 31), match='Python!!!!'>


# print(re.findall(f"-.+-", texto))

# print(re.findall(f"-.+?-", texto))

print(re.findall("\d{3}-\d{3}-\d{3}", texto))

print(re.findall("(\d{3})-\d{3}-\d{3}", texto))

