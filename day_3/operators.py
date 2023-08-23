# # Point 1 2 3
# age = 21
# height_me = 79.5
# complex_number = 5 + 2j

# # Point 4
# base = int(input("Enter a base: "))
# height = int(input("Enter a height: "))
# print(f"The area of the trangle is {0.5 * base * height}")

# # Point 5
# side_a = int(input("Enter the side a: "))
# side_b = int(input("Enter the side b: "))
# side_c = int(input("Enter the side c: "))
# print(f"The perimeter of the triangel is {side_a + side_b + side_c}")

# # Point 6
# lenght_rectangle = int(input("Enter the lenght of a rectangle: "))
# width_rectangle = int(input("Enter the width of a rectangle: "))
# print(f"The area of the rectangle is {lenght_rectangle * width_rectangle}")
# print(f"The perimeter of the rectangle is {2 * (lenght_rectangle + width_rectangle)}")

# # Point 7
# radius = float(input("Enter the radius of a circle: "))
# print(f"The are of the circle is {3.14 * radius ** 2}")
# print(f"The circumference of the circle is {2 * 3.14 * radius}")

# # Point 8
# # y = m * x + b
# m = 2
# b = - 2

# # y = m * 0 + b
# y = m * 0 + b

# # 0 = m * x + b
# x = (-1 * b) / m
# print(f"x-intercept: ({int(x)}, 0)")
# print(f"y-intercept: (0, {y})")

# # Point 9
# # m = y2 - y1 / x2 - x1
# point1 = (2, 2)
# point2 = (6, 10)
# x1, y1 = point1
# x2, y2 = point2
# print(f"The slope is: {int((y2 - y1) / (x2 - x1))}")

# Point 10 
# slope exercise 8 and 9 are equales

# Point 11
# y = x^2 + 6x + 9
# for x in range(-10, 11):
#     if x ** 2 + 6 * x + 9 == 0:
#         y = x ** 2 + 6 * x + 9
#         print(f"The value of x: {x} and the value of y: {y}")
#         break

# import math
# # x = (-b ± √(b^2 - 4ac)) / 2a
# a = 1
# b = 6
# c = 9
# discri = b ** 2 - 4 * a * c
# if discri > 0:
#     x1 = (-b + math.sqrt(discri)) / (2 * a)
#     x2 = (-b - math.sqrt(discri)) / (2 * a)
#     print(f"Las soluciones de x son: {x1} y {x2}")
# elif discri == 0:
#     x = -b / (2 * a)
#     print(f"La solución doble de x es: {int(x)}")
# else:
#     print("No hay soluciones posibles")

# # Point 12 13 14 15 16
# len_python = len("python")
# len_dragon = len("dragon")
# print(len_python > len_dragon)
# print("on" in "python" and "on" in "dragon")
# print("jargon" in "I hope this course is not full of jargon.")
# print(not("on" in "python" and "on" in "dragon"))

# len_p = len("python")
# print(type(str(float(len_p))).__name__)

# # point 17 18 19 20
# num = 10
# if num % 2 == 0:
#     print(str(num) + " is divisible in two")

# print((7 // 3) == int(7 / 3))

# print('10' == 10)
# print(int(9.8) == 10)

# # Point 21
# hours = int(input("Enter hours: "))
# rate_per_hour = int(input("Enter rate per hour: "))
# print(f"Your weekly earning is {hours * rate_per_hour}")

# seconds_in_hour = 3600
# seconds_in_day = 24 * seconds_in_hour
# seconds_in_year = 365 * seconds_in_day
# age = int(input("How old are you? "))
# print(f"You have lived for {age * seconds_in_year} seconds")


# Point 22
# for i in range(1, 6):
#     for j in range(4):
#         if j == 0: print(i, end=" ")
#         print(i ** j, end=" ")
#     print()
