import random

__author__ = 'Lindsay Ward'

name = "Lindsay"
print(name.upper())
print(type(name))

full_name = "Lindsay"
print(full_name)

value = random.randint(1, 10)

if value > 5:
    print("high")
else:
    print("low")
print("number was", value)

for char in full_name:
    print(char)

for number in range(10, 100, 7):
    print(number, end=" ")
