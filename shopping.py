"""
Do this now - start with the Cart class
Create a shopping program that uses the classes Product and Cart
A Cart can store multiple products in it
- find out the current total price
- add and remove products
- display all products sorted by price
"""

from cart import Cart


def main():
    print("Welcome")
    products_as_lists = load_products('products.csv')
    # print(products_as_lists)
    cart = Cart()
    print(cart)
    cart.add_product_lists(products_as_lists)
    print(cart)
    print(cart.get_products_as_lists())


def load_products(filename):
    products = [["Phone", 340, False],
                ["PC", 1420.95, False],
                ["Plant", 24.5, True],
                ['Bottle', 420.95, True]]
    return products

    # with open(filename) as products_file:


if __name__ == '__main__':
    main()
