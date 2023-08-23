# tpl = ("item1", "item2", "item3")
# fruits = ("banana", "orange", "mango", "lemon", "orange")
# print(fruits.count("orange"))

# tpl1 = ('item1', 'item2', 'item3')
# tpl2 = ('item4', 'item5','item6')
# tpl3 = tpl1 + tpl2
# print(tpl3)

# 1 2 3 4 5
empty_tuple = tuple()
brothers_names = ("michael", "nana", "paquine", "saque")
# print(len(brothers_names))
sisters_names = ("marta", "teresa", "maquina", "paque")
# print(len(sisters_names))
family = brothers_names + sisters_names
# print(len(family))
family_members = family + ("dad", "mom")
# print(family_members)

brothers = family_members[0:4]
sisters = family_members[4:8]
mom_dad = family_members[8:]

fruits = ("apple", "pineapple", "tune", "lemon", "avocado", "melon")
vegetables = ("carrot", "tomato", "corn", "onion")
animal = ("cow", "dog", "cat", "horse", "snake")
food_stuff_tp = fruits + vegetables + animal
food_stuff_lt = list(food_stuff_tp)
print(len(food_stuff_lt))
print(food_stuff_lt[len(food_stuff_lt) // 2])
first_three_items = food_stuff_lt[0:3]
last_three_items = food_stuff_lt[-3:]
del food_stuff_tp
#print(food_stuff_tp)
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)




