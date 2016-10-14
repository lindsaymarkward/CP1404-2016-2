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

    def add_product_lists(self, products_as_lists):
        """
        Add all products to products list
        :param products_as_lists: product details in the form of lists (list of lists)
        :return: None
        """
        for product_as_list in products_as_lists:
            p = Product(*product_as_list)
            # print(p)
            self.products.append(p)

    def get_products_as_lists(self):
        """
        Get internal Products in the form of lists
        :return:  product details in the form of lists (list of lists)
        """
        products_as_lists = []
        for product in self.products:
            products_as_lists.append([product.name, product.price, product.is_on_sale])
        return products_as_lists

def main():
    print("name is: ")
    print(__name__)

    c = Cart()
    print(c)

    p = Product("Water", 1.5, False)
    c.add(p)
    c.add(p)
    print(c)

    print(c.get_number_of_products())
    print(len(c))


def test():
    print("Hello test")


if __name__ == '__main__':
    main()
    # test()
