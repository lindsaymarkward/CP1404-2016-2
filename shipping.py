__author__ = 'Lindsay Ward'

total = 0
number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    price = float(input("Price of item: "))
    total += price
if total > 100:
    total *= 0.9
print("Total price for {} items is ${:.2f}".format(number_of_items, total))
