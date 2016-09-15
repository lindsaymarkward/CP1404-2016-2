__author__ = 'Lindsay Ward'


class Product:
    def __init__(self, name='', price=0.0, is_on_sale=False):
        self.name = name
        self.price = price
        self.is_on_sale = is_on_sale

    def __str__(self):
        return "{}, ${:.2f}{}".format(self.name, self.price, " (on sale!)" if self.is_on_sale else "")

    def put_on_sale(self, percentage):
        """
        Put product on sale, reducing its price by percentage passed in
        :param percentage: like 15 for 15%
        :return: None
        """

