# Exercise: Level 2
'''
Create a folder named day_1 inside 30DaysOfPython folder. 
Inside day_1 folder, create a python file helloworld.py and repeat questions 1, 2, 3 and 4. Remember to use print() when you are working on a python file. 
Navigate to the directory where you have saved your file, and run it.
'''
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 % 4)
print(3 / 4)
print(3 ** 4)
print(3 // 4)
print("Gera")
print("Her")
print("Gon")
print("MX")
print("I'm enjoying 30 days of python")
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(["Asabeneh", "Python", "Finland"]))
print(type("Ger"))
print(type("H"))
print(type("MX"))

# Exercise: Level 3
'''
Write an example for different Python data types such as Number (Integer, Float, Complex), 
String, Boolean, List, Tuple, Set and Dictionary.
'''
print(5)
print(8.2)
print(4 + 7j)
print("Hola")
print(False)
print([1, 2, 3, 4])
print(("Earth", "Sun", "Moon"))
print({8.3, 23.3, 1, 5, "elefante", "1 + 4j"})

# Find an Euclidian distance between (2, 3) and (10, 8)
from math import sqrt
A = (2, 3)
B = (10, 8)
def distancia(punto1: tuple, punto2: tuple) -> float:
    x1, y1 = punto1
    x2, y2 = punto2
    print(round(sqrt((pow(x2 - x1, 2) + pow(y2 - y1, 2))), 2))
distancia(A, B)
