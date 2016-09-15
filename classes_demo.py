"""
Classes and objects demo for CP1404
"""
__author__ = 'Lindsay Ward'

class Product:
    def __init__(self, name="", price=0.0, on_sale=False):
        self.name = name
        self.price = price
        self.is_on_sale = on_sale

    def __str__(self):
        if self.is_on_sale:
            on_sale_str = "(on sale)"
        else:
            on_sale_str = ""
        # return "{}, ${:.2f} {}".format(self.name, self.price, on_sale_str)
        return "{}, ${:.2f} {}".format(self.name, self.price, "(on sale)" if self.is_on_sale else "")

    def put_on_sale(self):
        self.is_on_sale = True
        self.price *= 0.9
        self.what = ""

item = Product("iPhone 6", 200, False)

print(item)
item.put_on_sale()
print(item)

item.nothing = "What?"

print(item.nothing)

another = Product()

print(another)
print(another.name)


class Person:
    def __init__(self, name="", age=0):
        # print("making a new Person")
        self.name = name
        self.age = age

    def __str__(self):
        return "{} is {} years old".format(self.name, self.age)


me = Person("Lindsay", 23)
you = Person("Derek", 45)

class Student(Person):
    def check(self):
        pass

class Mentor(Student):
    def c(self):
        pass

# print(me)
# print(me.__class__)




