__author__ = 'Lindsay Ward'


class User:
    def __init__(self, name=''):
        self.name = name
        self.number_of_tacos = 5
        self.score = 0
        self.__status = 9

    def __str__(self):
        return "{self.name}, {self.score} points, {self.number_of_tacos} tacos left".format(self=self)

    def give_tacos(self, tacos_given, recipient):
        """
        Give tacos to ... up to maximum of self.number_of_tacos
        :param recipient: User object to give tacos to
        :param tacos_given: number to try and give
        :return:
        """
        # adjust my number of tacos
        if self.number_of_tacos < tacos_given:
            tacos_given = self.number_of_tacos
        self.number_of_tacos -= tacos_given

        # adjust recipient's score
        recipient.receive_tacos(tacos_given)

    def receive_tacos(self, tacos_received):
        self.score += tacos_received

    def dance(self):
        print("I'm a dancing user")


class SuperUser(User):
    def give_tacos(self, tacos_given, recipient):
        recipient.receive_tacos(tacos_given)

    def level_up(self):
        pass

    def dance(self):
        print("I'm a dancing super user")


if __name__ == '__main__':
    print("Hi CP1404")
    u1 = User()
    u2 = SuperUser()
    users = [u1, u2, "Hi"]

    for user in users:
        user.dance()
