# st = set()
# st = {"item1", "item2", "item3", "item4"}
# st.add("item5")

# st.update(["item6", "item7", "item8"])
# st.remove("item2")
# print(st)

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(len(it_companies))
it_companies.add("Twitter")
it_companies.update(["Alphabet", "Intel", "Cisco System", "Orange"])
removed_item = it_companies.pop()

print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B), B.isdisjoint(A))
print(A.symmetric_difference(B))
del A, B

age = [22, 19, 24, 25, 26, 24, 25, 24]
age_set = set(age)
if len(age) > len(age_set):
    print("The list 'age' is bigger than the set 'age_set'")
else:
    print("The set 'age_set' is bigger than the list 'age'")


word = "I am a teacher and I love to inspire and teach people."
word_list = word.split()
word_set = set(word_list)
print(word_set)