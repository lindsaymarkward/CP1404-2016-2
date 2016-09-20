__author__ = 'Lindsay Ward'

from user import User

u1 = User("Lindsay")
u2 = User("Dereka")

print(u1)
u1.give_tacos(3, u2)
print(u1)
print(u2)
u1.give_tacos(7, u2)
print(u1)
print(u2)

