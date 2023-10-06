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

#
# print(re.findall("\d{3}-\d{3}-\d{3}", texto))

# Grupos () parentesis
# print(re.findall("(\d{3})-\d{3}-\d{3}", texto))

# Agregar característica en este caso todo lo que este dentro de los corchetes
# print(re.findall(r"[a-zA-Z0-9]", texto))

# Negación []
# print(re.findall(r"[^0-9]", texto))

# print(re.findall(r"[^\w\s]", texto))

texto = """
13-04-2021
2021-13-04
2021-04-13
"""
# print(re.findall(r"\d{2}-\d{2}-\d{4}", texto))

# 3 Validar un usuario
# 4-14 y solo o números o letras
usuarios = """usuario10 abc 10
"""
list_usuarios = usuarios.split()
for usuario in list_usuarios:
    if re.match(r"[a-z0-9]{4,14}", usuario) is not None:
        print(f"Usuario: \"{usuario}\" valido.")
    else:
        print(f"Usuario \"{usuario}\" invalido.")

paragraph = "I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."
paragraph_2 = re.sub(r"[^\w\s]", "", paragraph, flags=re.M)

words = paragraph_2.split()
list_set_word = [re.findall(word, paragraph_2) for word in words]

new_list_with_tuple = list(set((len(min_list), min_list[0]) for min_list in list_set_word))
list_orded_descend = sorted(new_list_with_tuple, key=lambda tup: (-tup[0], tup[1]))
# print(list_orded_descend)

points = ['-12', '-4', '-3', '-1', '0', '4', '8']
sorted_points_my = sorted(map(int, points))
distance_my = max(sorted_points_my) - min(sorted_points_my)

sorted_points = [-12, -4, -3, -1, -1, 0, 2, 4, 8]
distance = 8 -(-12) # 20

# print(distance_my)

import re
def is_valid_variable(string: str):
    coincide = r"[^A-Z0-9][a-zA-Z0-9_]*$"
    return re.match(coincide, string) is not None



import re

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. 
There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. 
;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

sentence_clear = re.sub(r'[^\w\s.]', '', sentence, flags=re.M)
print(sentence_clear)

from collections import Counter

oracion = "I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher"
palabras = oracion.split()
frecuencia_words = Counter(palabras)
# print(frecuencia_words)
list_tuples = [(count, word) for word, count in frecuencia_words.items()]
# print(list_tuples)
orded_tuples_descen = sorted(list_tuples, key=lambda tup: (-tup[0], tup[1]))[:3]
# print(orded_tuples_descen)

txt = """
I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which 
can give you all the capabilities to develop an application what else can you love
"""
new_txt = re.sub(r"[^\w\s]", "", txt)
new_txt_split = new_txt.split()
list_word_txt = [re.findall(word, txt) for word in new_txt_split]
list_count_tuples = list(set((len(item), item[0]) for item in list_word_txt))
orded = sorted(list_count_tuples, key=lambda tup: (-tup[0], tup[1]))

# print(orded)





