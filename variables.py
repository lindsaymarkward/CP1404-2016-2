from random import *

__author__ = 'Lindsay Ward'
#
# x = randint(1, 10)
# while 3 > x > 7:
#     pass

number_of_times = int(input("How many numbers: "))

for i in range(number_of_times):
    x = randint(1, 10)
    print(i, x)
    if x < 5:
        print("low")
    else:
        print("high")

    # x = randint(1, 10)
# print(x)
print("Finished")


invalid_age = True
while invalid_age:
    try:
        age = int(input("Age: "))
        if age < 0:
            print("Invalid age")
        else:
            invalid_age = False
    except:
        print("Invalid age")

print("You are {} years old".format(age))