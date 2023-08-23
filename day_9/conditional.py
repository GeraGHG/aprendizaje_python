# age = int(input("Enter your age: "))
# print("You are old enough to learn to drive.") if age >= 18 else print(f"You need {18 - age} more years to learn to drive.")

# your_age = int(input("Enter your age: "))
# my_age = 25
# age_diference = abs(your_age - my_age)
# year = "years" if age_diference != 1 else "year"
# comparation = "older" if your_age > my_age else "younger"
# if your_age == my_age:
#     print(f"Your age and my age are the same {your_age} years.")
# else:
#     print(f"You are {age_diference} {year} {comparation} than me.")

# num1 = int(input("Enter number one: "))
# num2 = int(input("Enter number two: "))
# print(f"{num1} is equal to {num2}") if num1 == num2 \
#     else print(f"{num1} is greater than {num2}") if num1 > num2 \
#     else print(f"{num1} is smaller than {num2}")
# code = int(input("Enter a range code from 0 to 100: "))
# print("A" if code in range(90, 101) else "B" if code in range(70, 90) \
#     else "C" if code in range(60, 70) else "D" if code in range(50, 60) \
#     else "F")

# month = input("Enter a month of the year: ").capitalize()

# # Autumn, Winter, Spring or Summer
# auntumn = ["September", "October", "November"]
# winter = ["December", "January", "February"]
# spring = ["March", "April", "May"]
# summer = ["June", "July", "August"]
# print("Auntumn" if month in auntumn else "Winter" if month in winter else "Spring" if month in spring else "Summer", "hola")

# fruits = ['banana', 'orange', 'mango', 'lemon']

# new_fruit = input("Enter a fruit: ").lower()
# print('That fruit already exist in the list') if new_fruit in fruits else (fruits.append(new_fruit), print("List of modified fruit: ", fruits)) 

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python', "C++"],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if "skills" in person: 
    middle = len(person["skills"]) // 2
    if len(person["skills"]) % 2 == 0:
        print(person['skills'][middle - 1], person["skills"][middle])
    else: print(person["skills"][middle])

if "Python" in person['skills']:
    print("The person has the skill")

'''
st2.issubset(st1) # True
st1.issuperset(st2) # True
'''
skill = set(person.get("skills", []))
if {"JavaScript", "Node", "MongoDB", "React"}.issubset(skill):
    print("He is a fullstack developer")
elif {"Node", "Python", "MongoDB"}.issubset(skill):
    print("He is a backend developer")
elif {"JavaScript", "React"}.issubset(skill):
    print("He is a front end developer")
else:
    print('Unknown title')

if person["is_marred"] and person["country"] == "Finland":
    # Asabeneh Yetayeh lives in Finland. He is married.
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married")

