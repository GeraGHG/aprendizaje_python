numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
# print([i for i in numbers if i < 1])

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

# print([i for row1 in list_of_lists for row2 in row1 for i in row2])

# print([(i, 1, i ** 2, i ** 3, i ** 4, i ** 5) for i in range(11)])

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
result = [[country[0][0].upper(), country[0][0][:3].upper(), country[0][1].upper()] for country in countries]

# print(result)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
r = [{"country": country[0][0].upper(), "city": country[0][1].upper()} for country in countries]
# print(r)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# print([tup[0] + " " + tup[1] for row1 in names for tup in row1])

nombres = [[("Miguel", "Sara")], [("Dona", "Daniel")], [("Mangel", "Roberta")]]
# print([[nombre[0][0], nombre[0][0][:3], nombre[0][1] ]for nombre in nombres])

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

# print([f"{name[0][0]} {name[0][1]}" for name in names])

# ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']


slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
print(slope(1, 2, 3, 4))
print((lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1))(1, 2, 3, 4))