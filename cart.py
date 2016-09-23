"""
A Cart can store multiple products in it
- find out the current total price
- add and remove products
- display all products sorted by price
"""
from product import Product


class Cart:
    def __init__(self, ):
        self.products = []

    def __str__(self):
        return str([str(product) for product in self.products])

    def __len__(self):
        return len(self.products)

    def add(self, product):
        self.products.append(product)

    def get_number_of_products(self):
        return len(self.products)


if __name__ == '__main__':
    c = Cart()
    print(c)

    p = Product("Water", 1.5, False)
    c.add(p)
    c.add(p)
    print(c)

    print(c.get_number_of_products())
    print(len(c))
