countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
# print(fin, sw, nor, rest)
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
# print(one, middle, last)

def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'
dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
# print(unpacking_person_info(**dct))

def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
# print(sum_all(1, 2, 3, 4))
# print(sum_all(1, 2, 3, 4, 5, 6, 7))


lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
# print(lst)
country_lst_one = ["Finland", "Sweden", "Norway"]
country_lst_two = ["Denmark", "Iceland"]
nordic_countries = [*country_lst_one, *country_lst_two]
# print(nordic_countries)

# for index, item in enumerate([20, 30, 40]):
    # print(index, item)



fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
# if len(fruits) == len(vegetables):
    #for f, v in zip(fruits, vegetables):
        # fruits_and_veges.append({"fruit": f, "vegetable": v})
    #print(fruits_and_veges)





def nombre_apellidos(nombre, apellidos):
    return f"nombre: {nombre} apellidos: {apellidos}"

datos = {
    "nombre": "Gerardo",
    "apellidos": "Hernández"
}

# print(nombre_apellidos(**datos))
from collections import Counter
notas = [5, 1, 7, 9, 7, 4, 3, 6, 0, 5, 8, 3, 7, 6, 10, 9, 6, 7, 5, 4]

dict_counter = dict(Counter(notas))
print(dict_counter)

dict_count_notas = {}
for elem in notas:
    dict_count_notas[elem] = dict_count_notas.get(elem, 0) + 1
print(dict_count_notas)
dict_order = dict(sorted(dict_count_notas.items(), key=lambda item: item))
print(dict_order)























