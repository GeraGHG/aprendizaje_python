# empty_dict = {}
# dct = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
# dct["key1"] = "value-one"
# print(dct)
# person = {
#     'first_name':'Asabeneh',
#     'last_name':'Yetayeh',
#     'age':250,
#     'country':'Finland',
#     'is_marred':True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street':'Space street',
#         'zipcode':'02210'
#             }
#     }

# dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
# dct.pop('key1') # removes key1 item
# dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
# dct.popitem() # removes the last item
# del dct['key2'] # removes key2 item

# print(dct.items())

empty_dict = {}
dog_dict = {}
dog_dict["name"] = "winy"
dog_dict["color"] = "white and brown"
dog_dict["breed"] = "mestizo"
dog_dict["legs"] = "medium"
dog_dict["age"] = 13
#print(dog_dict)

# name_dict{
# key: value,
# key: value
# }
student_dict = {
    "first_name": "Rodrigo",
    "last_name": "Marquez",
    "gender": "M",
    "age": 23,
    "marital_status": False,
    "skills": ["writing", "speaking", "listening"],
    "country": "México",
    "city": "CDM",
    "address": "Calle 24"
}


# print(len(student_dict))
# print(student_dict["skills"])
student_dict["skills"].extend(["running", "singer"])
# print(student_dict)

# print(student_dict.keys())
# values_std = student_dict.values()

del student_dict["address"]
#del dog_dict
print(student_dict)
print(dog_dict)
