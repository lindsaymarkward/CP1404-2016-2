__author__ = 'Lindsay Ward'

ages_dict = {"Bill": 21, "Jane": 34, "Jack": 56}

# print(ages_dict["Bill"])
# print(ages_dict.get("Bob", -1))
# ages_dict['Bob'] = ages_dict.get("Bob", 0) + 1
# print(ages_dict.get("Bob"))
# print(ages_dict)

# name = input("Name: ")
# age = int(input("Age: "))
#
# ages_dict[name] = age
# print(ages_dict)

for name in ages_dict:
    print("{} - {}".format(name, ages_dict[name]))

for name, age in ages_dict.items():
    print("{} - {}".format(name, age))
