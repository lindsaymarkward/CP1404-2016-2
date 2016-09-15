__author__ = 'Lindsay Ward'

class User:
    def __init__(self, name=''):
        self.name = name
        self.number_of_tacos = 5
        self.score = 0

    def __str__(self):
        return "{self.name}, {self.score} points, {self.number_of_tacos} tacos left".format(self=self)

    def give_taco(self, tacos_given):
        """
        Give tacos to ... up to maximum of self.number_of_tacos
        :param tacos_given: number to try and give
        :return:
        """
        # attempt to give...
        if self.number_of_tacos < tacos_given:
            tacos_given = self.number_of_tacos
        self.number_of_tacos -= tacos_given
