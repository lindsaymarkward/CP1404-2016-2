
# age = int(input("Age: "))
# while age < 0:
#     print("Invalid age")
#     age = int(input("Age: "))
#
# print("You are {} years old".format(age))


valid_age = False
while not valid_age:
    try:
        age = int(input("Age: "))
        if age < 0:
            print("Invalid age - must be non-negative")
        else:
            valid_age = True
    except ValueError:
        print("Invalid age - enter a number")

print("You are {} years old".format(age))
