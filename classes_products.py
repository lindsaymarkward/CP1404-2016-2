from product import Product

__author__ = 'Lindsay Ward'

products = [Product("Phone", 340, False),
            Product("PC", 1420.95, False),
            Product("Plant", 24.5, True),
            Product('Bottle', 420.95, True)]

print([str(product) for product in products])

on_sale_products = [product for product in products if product.is_on_sale]
print([str(product) for product in on_sale_products])

