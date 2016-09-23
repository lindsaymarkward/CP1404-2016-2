__author__ = 'Lindsay Ward'


class User:
    def __init__(self, name=''):
        """ Create User object with name """
        self.name = name
        self.number_of_tacos = 5
        self.score = 0
        self.__status = 9

    def __str__(self):
        return "{self.name}, {self.score} points, {self.number_of_tacos} tacos left".format(self=self)

    def __eq__(self, other):
        return self.score == other.score

    def __gt__(self, other):
        return self.score > other.score

    def give_tacos(self, tacos_given, other):
        """
        Give tacos to ... up to maximum of self.number_of_tacos
        :param other: User object to give tacos to
        :param tacos_given: number to try and give
        :return:
        """
        if self is other or not isinstance(other, User):
            return False
        # adjust my number of tacos
        if self.number_of_tacos < tacos_given:
            tacos_given = self.number_of_tacos
        self.number_of_tacos -= tacos_given

        # adjust recipient's score
        other.receive_tacos(tacos_given)
        return True

    def receive_tacos(self, tacos_received):
        self.score += tacos_received

    def dance(self):
        print("I'm a dancing user")


class SuperUser(User):
    def give_tacos(self, tacos_given, other):
        other.receive_tacos(tacos_given)

    def level_up(self):
        pass

    def dance(self):
        print("I'm a dancing super user")
        return self


if __name__ == '__main__':
    # print("Hi CP1404")
    u1 = User("Bob")
    u2 = User("Wendy")
    u3 = SuperUser("Rolly")
    print(type(u1), type(u3))
    print(isinstance(u3, User))
    print(type(u1) == type(u3))

    if u1.give_tacos(30, u2):
        print("Success")
    else:
        print("You sneak or dafty...")

    print(u1, u2, sep="\n")
    print("{0} == {1} is {2}, {0} > {1} is {3}, {0} < {1} is {4}".format(u1.score, u2.score, u1 == u2, u1 > u2, u1 < u2))

    # users = [u1, u2]
    #
    # for user in users:
    #     user.dance()
