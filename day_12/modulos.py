# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 11:15:29 2023

@author: Germanico
"""
import random
import string

# from my import generate_full_name
# print(generate_full_name("Asabeneh", "Yetayeh"))

# from my import generate_full_name, sum_two_nums, gravity
# print(generate_full_name("gerardo", "hernandez"))
# print(sum_two_nums(5, 2))
# print(50 * gravity())

# import os
# os.mkdir("directory_name")
# os.rmdir("directory_name")

#import sys
# print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
# print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))
#sys.exit()
# from statistics import mean, median, mode, stdev
# ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
# print(mean(ages))
# print(median(ages))
# print(mode(ages))
# print(stdev(ages))

# from math import pi as PI
# print(PI)

# import string
# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)

# from random import random, randint
# print(random())
# print(randint(5, 20)) # numero entero entre (5, 20) incluyendo el 20

import string
from random import choice
def user_id_gen_by_user():
    num_chars = int(input("Enter the number of characters: "))
    num_ID = int(input("Enter the number of IDs to will create: "))
    chars = string.ascii_letters + string.digits
    users = ["".join(choice(chars) for _ in range(num_chars)) for _ in range(num_ID)]
    return users

# print(user_id_gen_by_user())

def rgb_color_gen():
    rgb = tuple(random.randint(0, 255) for _ in range(3))
    return f"rgb{rgb}"
# print(rgb_color_gen())

def list_of_hexa_colors(num_colors):
    chars = string.ascii_uppercase[:6] + string.digits
    list_hexa = ["#"+"".join(choice(chars) for _ in range(6)) for _ in range(num_colors)]
    return list_hexa
# print(list_of_hexa_colors(5))

def list_of_rgb_colors(num_colors):
    rgb = ["rgb" + f"({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0,255)})" for _ in range(num_colors)]
    return rgb
# print(list_of_rgb_colors(5))

def generate_colors(hexa_rgb: str, num: int) -> list:
    return list_of_hexa_colors(num) if hexa_rgb == "hexa" else list_of_rgb_colors(num) if hexa_rgb == "rgb" else "Invalid data"

print(generate_colors('hexa', 3)) # ['#a3e12f','#03ed55','#eb3d2b']
print(generate_colors('hexa', 1)) # ['#b334ef']
print(generate_colors('rgb', 3))  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80']
print(generate_colors('rgb', 1))  # ['rgb(33,79, 176)']





def shuffle_list(lista_items: list):
    copy_items = lista_items.copy()
    random.shuffle(copy_items)
    return copy_items


def seven_random_numbers():
    return random.sample(range(10), 7)

print(seven_random_numbers())

